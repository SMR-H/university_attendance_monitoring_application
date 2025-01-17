from rest_framework import serializers
from rest_framework.serializers import ValidationError

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from rest_framework_simplejwt.tokens import AccessToken

from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# Models
from blog.models import Article
from professor.models import Professor
from course.models import Course
from course_offering.models import CourseOffering
from semester.models import Semester
from course_holding.models import CourseHolding
from account.models import User



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    pass


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "The email address is not registered with us.")
        return value

    def save(self):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        # access_token = AccessToken.for_user(user)
        password_reset_token = PasswordResetTokenGenerator().make_token(user)
        password_reset_link = self.context['request'].build_absolute_uri(
            f'/api/password-reset/{urlsafe_base64_encode(force_bytes(user.pk))}/{password_reset_token}/')
        # password_reset_link = self.context['request'].build_absolute_uri(f'/api/password-reset/{urlsafe_base64_encode(force_bytes(user.pk)).decode()}/{password_reset_token}/')
        print(password_reset_link)
        # Send the password reset link to the user's email
        # Mailer.send_password_reset_mail(email, password_reset_link)
        return {'message': 'Password reset link has been sent to your registered email.'}


class PasswordResetConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        uidb64 = self.context['uidb64']
        token = self.context['token']
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except:
            user = None
        if user is None or not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError(
                'The password reset link is invalid or expired.')
        return data

    def save(self):
        password = self.validated_data['password']
        uidb64 = self.context['uidb64']
        token = self.context['token']
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        user.set_password(password)
        user.save()
        return {'message': 'Password has been reset successfully.'}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_superuser', 'is_staff',
                   'date_joined', 'groups', 'user_permissions']
        read_only_fields = ['last_login']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_user_role(self, value):
        if value in [User.UserRoleChoices.UNIVERSITY, User.UserRoleChoices.GENERAL_MANAGER, User.UserRoleChoices.ADMIN]:
            raise serializers.ValidationError("This user role is not allowed.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if password:
            hashed_password = make_password(password)
            validated_data['password'] = hashed_password
        validated_data['university_id'] = self.context['request'].user.university_id
        return super().create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            hashed_password = make_password(password)
            validated_data['password'] = hashed_password
        validated_data.pop('university_id')
        return super().update(instance, validated_data)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    allowed_course_detail = serializers.SerializerMethodField()

    class Meta:
        model = Professor
        fields = '__all__'

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_allowed_course_detail(self, obj):
        return [{'id': c.id, 'name': c.name} for c in obj.allowed_course_id.all()]

    def validate_user(self, user):
        # check if the professor's university_id matches the request user's university_id
        user_university_id = self.context['request'].user.university_id
        if user.university_id != user_university_id:
            raise serializers.ValidationError(
                "The professor does not belong to your university.")
        if not user.is_active:
            raise serializers.ValidationError("The user is not active.")
        if user.user_role != User.UserRoleChoices.PROFESSOR:
            raise serializers.ValidationError(
                "The user must have 'PROFESSOR' role.")
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        if request and (request.method == 'GET'):
            data.pop('allowed_course_id', None)
        if request and (request.method != 'GET'):
            data.pop('allowed_course_detail', None)
        return data


class CourseOfferingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseOffering
        fields = '__all__'


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'
        read_only_fields = ['university_id']
        # extra_kwargs = {
        #     'id': {'read_only': True}
        # }

    def validate(self, data):
        user_university_id = self.context['request'].user.university_id
        instance = getattr(self, 'instance', None)  # get instance if exists
        if instance and instance.semester_code == data.get('semester_code'):
            # skip duplicate check for the same instance being updated
            pass
        elif Semester.objects.filter(university_id=user_university_id, semester_code=data['semester_code']).exists():
            raise serializers.ValidationError(
                'A semester with this code already exists for this university')
        # if Semester.objects.filter(university_id=user_university_id, semester_code=data['semester_code']).exists():
        #     raise serializers.ValidationError('A semester with this code already exists for this university')

        if str(data['semester_code'])[-1] != str(data['semester_type']):
            raise ValidationError(
                'Semester code does not match the semester type')

        if data['end_date'] < data['start_date']:
            raise ValidationError('End date cannot be before start date')

        return data

    def create(self, validated_data):
        user_university_id = self.context['request'].user.university_id
        validated_data['university_id'] = user_university_id
        return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)


class CourseHoldingSerializer(serializers.ModelSerializer):
    allowed_professor = serializers.SerializerMethodField()

    class Meta:
        model = CourseHolding
        fields = '__all__'

    def get_allowed_professor(self, obj):
        return [{'id': p.id, 'name': f"{p.user.first_name or ''} {p.user.last_name or ''}"} for p in obj.offered_course.professor_id.all()]
    # TODO: check bshe ke professor_id model courseHolding ba yki az ostadhayi ke toye professor_id model courseOffering hast por bshe
    # masalan: 2 ta ostad dare ye darsi, emroz ostad dovom omade baraye tashkil class
    # aghar ham tak ostadiye, faghat on ostad btone entkhab she bara professor_id model CourseHolding


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class FullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BasicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['is_superuser', 'user_permissions',
                            'groups', 'date_joined', 'last_login']
