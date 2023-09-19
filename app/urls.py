from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views


urlpatterns = [
    path('', views.admin.as_view()),
    path('logout/',views.LogoutView.as_view()),
    path('currentuser/', views.MyView.as_view()),
    path('Create_admins', views.Createadmins.as_view()),
    path('Create_admins/<int:pk>/', views.CreateadminsDetail.as_view()),
    
    path('Login_adins', views.LoginView.as_view()),
    path('DepartmentList/', views.DepartmentList.as_view()),
    path('DepartmentList/<int:pk>/', views.DepartmentDetail.as_view()),
    path('CollegeList/', views.CollegeList.as_view()),
    path('CollegeList/<int:pk>/', views.CollegeDetail.as_view()),
    path('FacultyList/', views.FacultyList.as_view()),
    path('FacultyList/<int:pk>/', views.FacultyDetail.as_view()),
    path('EventList/', views.EventList.as_view()),
    path('EventList/<int:pk>/', views.EventDetail.as_view()),
    
    path('EventListUpcooming/', views.EventListUpcooming.as_view()),
    
    path('EventListImages/', views.EventImage.as_view()),
    path('EventListUpcooming/<int:pk>/', views.EventImagesDetails.as_view()),
    
    path('GalleryList/', views.GalleryList.as_view()),
    path('GalleryList/<int:pk>/', views.GalleryDetail.as_view()),
    path('AchievementsList/', views.AchievementsList.as_view()),
    path('AchievementsList/<int:pk>/', views.AchievementsDetail.as_view()),
    path('CanteenList/', views.CanteenList.as_view()),
    path('CanteenList/<int:pk>/', views.CanteenDetail.as_view()),
    
    
    path('BusesList/', views.BusesList.as_view()),
    path('BusesList/<int:pk>/', views.BusesDetail.as_view()),
    
    path('SportImagesList/', views.SportImagesList.as_view()),
    path('SportImagesList/<int:pk>/', views.SportImagesDetail.as_view()),
    
    path('SubcollegeList/', views.SubcollegeList.as_view()),
    path('SubcollegeList/<int:pk>/', views.SubcollegeDetail.as_view()),
    
    
    path('CourseList/', views.CourseList.as_view()),
    path('CourseList/<int:pk>/', views.CourseDetail.as_view()),
    path('CourseImageList/', views.CourseImageList.as_view()),
    path('CoursCourseImageListeList/<int:pk>/', views.CourseImageDetail.as_view()),
    
    
    
    path('YearStudentList/', views.YearStudentList.as_view()),
    path('YearStudentList/<int:pk>/', views.YearStudentDetail.as_view()),
    
    
    path('StudentPlacementList/', views.StudentPlacementList.as_view()),
    path('StudentPlacementList/<int:pk>/', views.StudentPlacementDetail.as_view()),
    
    
    
    path('forgot-password/',views.ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password/<str:uidb64>/<str:token>/',views.PasswordResetView.as_view(), name='password_reset'),
    path('userqueries/',views.UserQueryView.as_view(), name='UserQueryView'),
    
    
    path('Addmision_quarie/',views.StudentAdmissionListCreateView.as_view(),name='Addmision_quarie'),
    
    
    
]