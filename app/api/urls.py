from django.urls import path
from .views import *

urlpatterns = [
    # path('', ArticleListAPI.as_view(), name='article_list_API'),
    # path('<int:pk>', ArticleDetailAPI.as_view(), name='article_detail_API'),



    path('login', CustomTokenObtainPairAPI.as_view(), name='token_obtain_pair'),

    # path('login/refresh', CustomTokenRefreshAPI.as_view(), name='token_refresh'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    path('logout', LogoutAPI.as_view(), name='logout'),
    path('password-reset', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/<str:uidb64>/<str:token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('user/list/', UserListAPI.as_view(), name='user_list_API'),
    path('user/<int:pk>/', UserRetrieveAPI.as_view(), name='user_retrieve_API'),
    path('user/create/', UserCreateAPI.as_view(), name='user_create_API'),
    path('user/update/<int:pk>/', UserUpdateAPI.as_view(), name='user_update_API'),
    path('user/delete/<int:pk>/', UserDestroyAPI.as_view(), name='user_delete_API'),
    path('user/<str:username>/', UserRetriveUsername.as_view(), name='user_retrieve_username_API'),

    path('course/list/', CourseListAPI.as_view(), name='course_list_API'),
    path('course/<int:pk>/', CourseRetrieveAPI.as_view(), name='course_retrieve_API'),
    path('course/create/', CourseCreateAPI.as_view(), name='course_create_API'),
    path('course/delete/<int:pk>/', CourseDestroyAPI.as_view(), name='course_delete_API'),

    path('professor/list/', ProfessorListAPI.as_view(), name='professor_list_API'),
    path('professor/<int:pk>/', ProfessorRetrieveAPI.as_view(), name='professor_retrieve_API'),
    path('professor/create/', ProfessorCreateAPI.as_view(), name='professor_create_API'),
    path('professor/update/<int:pk>/', ProfessorUpdateAPI.as_view(), name='professor_update_API'),
    path('professor/delete/<int:pk>/', ProfessorDestroyAPI.as_view(), name='professor_delete_API'),

    path('semester/list/', SemesterListAPI.as_view(), name='semester_list_API'),
    path('semester/<int:pk>/', SemesterRetrieveAPI.as_view(), name='semester_retrieve_API'),
    path('semester/create/', SemesterCreateAPI.as_view(), name='semester_create_API'),
    path('semester/update/<int:pk>/', SemesterUpdateAPI.as_view(), name='semester_update_API'),
    path('semester/delete/<int:pk>/', SemesterDestroyAPI.as_view(), name='semester_delete_API'),

    path('courseoffering/list/', CourseOfferingListAPI.as_view(), name='course_offering_list_API'),
    path('courseoffering/<int:pk>/', CourseOfferingRetrieveAPI.as_view(), name='course_offering_retrieve_API'),
    path('courseoffering/create/', CourseOfferingCreateAPI.as_view(), name='course_offering_create_API'),
    path('courseoffering/update/<int:pk>/', CourseOfferingUpdateAPI.as_view(), name='course_offering_update_API'),
    path('courseoffering/delete/<int:pk>/', CourseOfferingDestroyAPI.as_view(), name='course_offering_delete_API'),

    path('courseofferingfileupload/create/', CourseOfferingFileUploadAPI.as_view(),
        name='course_offering_file_upload_API'),

    path('courseholding/list/', CourseHoldingListAPI.as_view(), name='course_holding_list_API'),
    path('courseholding/<int:pk>/', CourseHoldingRetrieveAPI.as_view(), name='course_holding_retrieve_API'),
    path('courseholding/create/', CourseHoldingCreateAPI.as_view(), name='course_holding_create_API'),
    path('courseholding/update/<int:pk>/', CourseHoldingUpdateAPI.as_view(), name='course_holding_update_API'),
]
handler500 = 'rest_framework.exceptions.server_error'
# handler400 = 'rest_framework.exceptions.bad_request'
