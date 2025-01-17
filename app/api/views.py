from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.contrib.auth import get_user_model
from rest_framework import status
from django.core.exceptions import PermissionDenied

from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from rest_framework.generics import *
from .serializers import *

from .permissions import *
# Mpdels
from blog.models import Article
from course.models import Course
from professor.models import Professor
from course_offering.models import CourseOffering
from semester.models import Semester
from account.models import User
from classroom.models import Classroom
from university.models import University, Faculty, Department
from major.models import MajorList

from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import OutstandingToken, BlacklistedToken

from rest_framework import exceptions
from rest_framework_simplejwt.exceptions import InvalidToken

import pandas as pd
from django.http import JsonResponse
from django.core.validators import FileExtensionValidator
from rest_framework.parsers import MultiPartParser, FormParser


class CustomTokenObtainPairAPI(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshAPI(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer


class PasswordResetView(GenericAPIView):
    serializer_class = PasswordResetSerializer
    # permission_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        response = serializer.save()
        return Response(response)


class PasswordResetConfirmView(GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = [AllowAny]

    def post(self, request, uidb64, token):
        serializer = self.get_serializer(data=request.data, context={
                                        'uidb64': uidb64, 'token': token})
        serializer.is_valid(raise_exception=True)
        response = serializer.save()
        return Response(response)

# TODO: """bayad bahs Error handleing ro camel conam (toye poshe handlers) va /
#  LogoutAPI nabayad injori bmone"""


class LogoutAPI(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            if not refresh_token:
                raise ValidationError(
                    "The 'refresh_token' field cannot be empty.")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except InvalidToken:
            return Response({"error": {"code": 401, "message": "Invalid token."}}, status=status.HTTP_401_UNAUTHORIZED)
        except KeyError:
            return Response({"error": {"code": 400, "message": "The 'refresh_token' field is required."}}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({"error": {"code": 400, "message": str(e)}}, status=status.HTTP_400_BAD_REQUEST)


class UserListAPI(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        university_id = self.request.user.university_id
        queryset = User.objects.filter(university_id=university_id)
        return queryset


class UserRetrieveAPI(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        university_id = self.request.user.university_id
        queryset = User.objects.filter(university_id=university_id)
        return queryset


class UserCreateAPI(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPI(UpdateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        university_id = self.request.user.university_id
        queryset = User.objects.filter(university_id=university_id)
        return queryset


class UserDestroyAPI(DestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        university_id = self.request.user.university_id
        queryset = User.objects.filter(university_id=university_id)
        return queryset


class UserRetriveUsername(RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_queryset(self):
        return User.objects.filter(username=self.kwargs['username'])


class ProfessorListAPI(ListAPIView):
    serializer_class = ProfessorSerializer

    def get_queryset(self):
        university_id = self.request.user.university_id
        queryset = Professor.objects.filter(user__university_id=university_id)
        return queryset


class ProfessorRetrieveAPI(RetrieveAPIView):
    serializer_class = ProfessorSerializer

    def get_queryset(self):
        university_id = self.request.user.university_id
        queryset = Professor.objects.filter(user__university_id=university_id)
        return queryset


class ProfessorCreateAPI(CreateAPIView):
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all()


class ProfessorUpdateAPI(UpdateAPIView):
    serializer_class = ProfessorSerializer

    def get_queryset(self):
        university_id = self.request.user.university_id
        queryset = Professor.objects.filter(user__university_id=university_id)
        return queryset


class ProfessorDestroyAPI(DestroyAPIView):
    serializer_class = ProfessorSerializer

    def get_queryset(self):
        university_id = self.request.user.university_id
        queryset = Professor.objects.filter(user__university_id=university_id)
        return queryset


class CourseListAPI(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveAPI(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseCreateAPI(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDestroyAPI(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseOfferingListAPI(ListAPIView):
    queryset = CourseOffering.objects.all()
    serializer_class = CourseOfferingSerializer


class CourseOfferingRetrieveAPI(RetrieveAPIView):
    queryset = CourseOffering.objects.all()
    serializer_class = CourseOfferingSerializer


class CourseOfferingCreateAPI(CreateAPIView):
    queryset = CourseOffering.objects.all()
    serializer_class = CourseOfferingSerializer


class CourseOfferingUpdateAPI(UpdateAPIView):
    queryset = CourseOffering.objects.all()
    serializer_class = CourseOfferingSerializer


class CourseOfferingDestroyAPI(DestroyAPIView):
    queryset = CourseOffering.objects.all()
    serializer_class = CourseOfferingSerializer


class SemesterListAPI(ListAPIView):
    serializer_class = SemesterSerializer

    def get_queryset(self):
        university_id = self.request.user.university_id
        queryset = Semester.objects.filter(university_id=university_id)
        return queryset


class SemesterRetrieveAPI(RetrieveAPIView):
    serializer_class = SemesterSerializer

    def get_queryset(self):
        university_id = self.request.user.university_id
        queryset = Semester.objects.filter(university_id=university_id)
        return queryset


class SemesterCreateAPI(CreateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class SemesterUpdateAPI(UpdateAPIView):
    serializer_class = SemesterSerializer

    def get_queryset(self):
        university_id = self.request.user.university_id
        queryset = Semester.objects.filter(university_id=university_id)
        return queryset


class SemesterDestroyAPI(DestroyAPIView):
    serializer_class = SemesterSerializer

    def get_queryset(self):
        university_id = self.request.user.university_id
        queryset = Semester.objects.filter(university_id=university_id)
        return queryset


class CourseHoldingListAPI(ListAPIView):
    queryset = CourseHolding.objects.all()
    serializer_class = CourseHoldingSerializer


class CourseHoldingRetrieveAPI(RetrieveAPIView):
    queryset = CourseHolding.objects.all()
    serializer_class = CourseHoldingSerializer


class CourseHoldingCreateAPI(CreateAPIView):
    serializer_class = CourseHoldingSerializer

    def perform_create(self, serializer):
        course_holding = serializer.instance
        selected_professor_id = serializer.validated_data.get(
            'professor_id').id
        allowed_professors_id = course_holding.offered_course.professor_id.values_list(
            'id', flat=True)

        if selected_professor_id not in allowed_professors_id:
            raise ValidationError(
                {'msg': 'Selected professor is not allowed for this course holding.'})
        serializer.save()

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as ex:
            return Response(ex.message_dict, status=400)


class CourseHoldingUpdateAPI(UpdateAPIView):
    queryset = CourseHolding.objects.all()
    serializer_class = CourseHoldingSerializer

    def perform_update(self, serializer):
        course_holding = serializer.instance
        selected_professor_id = serializer.validated_data.get(
            'professor_id').id
        allowed_professors_id = course_holding.offered_course.professor_id.values_list(
            'id', flat=True)

        if selected_professor_id not in allowed_professors_id:
            raise ValidationError(
                {'msg': 'Selected professor is not allowed for this course holding.'})
        serializer.save()

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValidationError as ex:
            return Response(ex.message_dict, status=400)


class CourseHoldingDestroyAPI(DestroyAPIView):
    queryset = CourseHolding.objects.all()
    serializer_class = CourseHoldingSerializer


class CourseOfferingFileUploadAPI(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        university_id = request.user.university_id_id
        file = request.FILES['file']
        if not file:
            return Response({'error': 'Please upload a file.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the file size is less than or equal to 5 MB
        max_size = 5 * 1024 * 1024  # 5 MB in bytes
        if file.size > max_size:
            return Response({'error': 'File size should not exceed 5 MB.'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate file type
        file_ext_validator = FileExtensionValidator(
            allowed_extensions=['xls', 'xlsx'])
        try:
            file_ext_validator(file)
        except:
            raise ValidationError(
                {'error': 'File extension is not allowed. Allowed extensions are: xls, xlsx.'})

        dtype = {
            'course_code': str,
            'professor_code': str,
            'professor_code': str,
        }

        df = pd.read_excel(
            file, dtype={'course_code': str, 'professor_code': str, 'professor_code': str, })
        # Check required columns
        required_columns = ['course_code', 'professor_code', 'class_number', 'faculty_code', 'weekday',
                            'start_time', 'end_time', 'offering_course_code', 'major_code', 'aggregate', 'course_gender']
        if not all(column in df.columns for column in required_columns):
            return Response({'error': 'Missing required columns.'}, status=status.HTTP_400_BAD_REQUEST)

        errors = []
        duplicates = []
        print(df)
        print(set(df['course_code']))

        print(df['course_code'])
        print(df['professor_code'])
        print(df['class_number'])
        print(df['faculty_code'])
        print(df['weekday'])
        print(df['start_time'])
        print(df['end_time'])
        print(df['offering_course_code'])
        print(df['major_code'])
        print(df['aggregate'])
        print(df['course_gender'])

        professor_codes = set()
        for index, row in df.iterrows():
            codes = str(row['professor_code']).replace(' ', '').split('_')
            professor_codes.update(codes)
        professor_codes.discard('')
        # print(professor_codes)

        courses = Course.objects.filter(course_code__in=set(df['course_code']))
        professor_codes = Professor.objects.filter(
            professor_code__in=professor_codes, user__university_id=university_id)
        class_numbers = Classroom.objects.filter(class_number__in=set(
            df['class_number']), faculty_id__university_id=university_id)
        faculties = Faculty.objects.filter(faculty_code__in=set(
            df['faculty_code']), university_id=university_id)
        offerings = CourseOffering.objects.filter(
            offering_course_code__in=set(df['offering_course_code']))
        # majors =
        # print('---------------------------------------')
        # print(class_numbers)
        # print(professor_codes)
        # print(faculties)
        # print('---------------------------------------')
        # Check duplicates
        # duplicates = df[df.duplicated(keep=False)]
        # if not duplicates.empty:
        #     duplicate_indices = ', '.join(str(index) for index in duplicates.index)
        #     return Response({'error': f'Duplicate rows found at indices: {duplicate_indices}'}, status=status.HTTP_400_BAD_REQUEST)

        # Check duplicates
        duplicates = df[df.duplicated(keep=False)]
        if not duplicates.empty:
            grouped = duplicates.groupby(list(duplicates.columns))
            duplicate_indices = []
            for group, indices in grouped.groups.items():
                if len(indices) > 1:
                    duplicate_indices.append(tuple(indices))
            if duplicate_indices:
                error_message = 'Duplicate rows found: {}'.format(
                    ' , '.join(str(tuple_) for tuple_ in duplicate_indices))
                return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

        for index, row in df.iterrows():
            course_code = row['course_code']
            class_number = row['class_number']
            faculty_code = row['faculty_code']
            offering_course_code = row['offering_course_code']

            professor_code = str(row['professor_code']
                                 ).replace(' ', '').split('_')
            # print(professor_code)
            major_code = row['major_code']

            if not courses.filter(course_code=course_code):
                errors.append(
                    f"Row number: {index + 2} -Course with code {course_code} does not exist.")
            for code in professor_code:
                if not professor_codes.filter(professor_code=code):
                    errors.append(
                        f"Row number: {index + 2} -Professor with code {code} does not exist or dose not belong to this university.")

            if not class_numbers.filter(class_number=class_number, faculty_id__faculty_code=faculty_code):
                errors.append(
                    f"Row number: {index + 2} -Classroom with number {class_number} does not exist.")
            if not faculties.filter(faculty_code=faculty_code):
                errors.append(
                    f"Row number: {index + 2} -Semester with code {faculty_code} does not exist.")
            if offerings.filter(offering_course_code=offering_course_code):
                duplicates.append(
                    f"Row number: {index + 2} -Course offering with code {offering_course_code} already exists.")

        if errors or duplicates:
            return JsonResponse({'errors': errors, 'duplicates': duplicates})

        # # If there are no errors or duplicates, save the data
        # for index, row in df.iterrows():
        #     course_code = row['course_code']
        #     class_number = row['class_number']
        #     faculty_code = row['faculty_code']
        #     offering_course_code = row['offering_course_code']

        #     # Note: You may need to modify this code to match your specific model and field names
        #     course_offering = CourseOffering.objects.create(
        #         course_id_id=course_id,
        #         semester_id_id=semester_id,
        #         class_id_id=class_id,
        #         offering_course_code=offering_course_code,
        #         weekday=row['weekday'],
        #         start_time=row['start_time'],
        #         end_time=row['end_time'],
        #         course_gender=row['course_gender'],
        #     )
        #     course_offering.major_id.set(row['major_id'])
        #     course_offering.professor_id.set(row['professor_id'])

        # return JsonResponse({'success': True})

################################################
# class ArticleListAPI(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
# class ArticleDetailAPI(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (IsAuthorOrReadOnly,)
#     lookup_field = 'pk'
# class RevokeToken(APIView):

#     permission_classes = (IsAuthenticated,)

#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)
#         return Response({'msg':'sd'},status=204)
