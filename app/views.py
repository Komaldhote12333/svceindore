from django.shortcuts import render
from .models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from rest_framework import generics
from datetime import datetime, timedelta
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from rest_framework import viewsets
from django.conf import settings
from django.template.loader import render_to_string

from rest_framework import permissions

class MyView(APIView):

    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        serializer = CustomUserSerializer(current_user)
        return Response(serializer.data)

class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True  # Allow unauthenticated access for GET requests
        
        user = request.user
        if user and user.is_authenticated and user.role == "admin":
            return True  # Allow access for authenticated users with "admin" role
            
        return False
    
class CustomPermissionfortpo(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True  # Allow unauthenticated access for GET requests
        
        user = request.user
        if user and user.is_authenticated and user.role == "tpo":
            return True  # Allow access for authenticated users with "admin" role
            
        return False
    
class CustomPermissionforsuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and user.role == "tpo":
            return True  # Allow access for authenticated users with "admin" role
            
        return False
    

class admin(APIView):
    pass

class Createadmins(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
class CreateadminsDetail(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = [permissions.IsAdminUser]
        queryset = CustomUser.objects.all()
        serializer_class = CustomUserSerializer    


class LoginView(APIView):
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request,username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user is not None :
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid login credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Invalidate the user's token
        request.auth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class DepartmentList(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer    
    
    
class CollegeList(generics.ListCreateAPIView):

    permission_classes = [CustomPermission]
    
    
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class CollegeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    
    queryset = College.objects.all()
    serializer_class = CollegeSerializer        
    
    
class FacultyList(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer    
    
    
    
class EventList(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    
    queryset = Event.objects.all()
    serializer_class = EventSerializer    
    
 
 



class EventImage(APIView):
   parser_classes = (MultiPartParser, FormParser)
   
   
   
   
   def get(self, request, format=None):
        snippets = EventImages.objects.all()
        serializer = EventImgSerializer(snippets, many=True)
        return Response(serializer.data)
   
   
   
   def post(self, request, *args, **kwargs):
        event_id = request.data.get('Events')
        images = request.FILES.getlist('image')
        print(event_id)
        if not images:
            return Response({'message': 'No images provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return Response({'message': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

        for image in images:
            serializer = EventImgSerializer(data={'Events': event.id, 'image': image})

            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       
        return Response({'message': 'Images uploaded successfully'}, status=status.HTTP_201_CREATED)
    
    
    
class EventImagesDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    
    queryset = EventImages.objects.all()
    serializer_class = EventImgSerializer    
    
 
 
 
 
 
class EventListUpcooming(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        current_date = datetime.now().date()

        end_date = current_date + timedelta(days=10)

        queryset = Event.objects.filter(event_date__range=(current_date, end_date))

        return queryset
       
class GalleryList(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class GalleryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer    
    
    
class AchievementsList(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer


class AchievementsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer        
    
    
class CanteenList(generics.ListCreateAPIView):
    permission_classes = [CustomPermissionfortpo]
    queryset = Canteen.objects.all()
    serializer_class = CanteenSerializer


class CanteenDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermissionfortpo]

    
    queryset = Canteen.objects.all()
    serializer_class = CanteenSerializer           
    
    
    
class BusesList(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    
    queryset = Buses.objects.all()
    serializer_class = BusesSerializer


class BusesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    
    queryset = Buses.objects.all()
    serializer_class = BusesSerializer               
    
    
    
class SportImagesList(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    
    queryset = SportImages.objects.all()
    serializer_class = SportImagesSerializer


class SportImagesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    
    queryset = SportImages.objects.all()
    serializer_class = SportImagesSerializer               
    
    
class SubcollegeList(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    
    queryset = Subcollege.objects.all()
    serializer_class = SubcollegeSerializer


class SubcollegeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    
    queryset = Subcollege.objects.all()
    serializer_class = SubcollegeSerializer               
    
    
    
    
class CourseList(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer         
    



class CourseImageList(APIView):
    permission_classes = [CustomPermission] 
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        snippets = CourseImage.objects.all()
        serializer = CourseImageSerializer(snippets, many=True)
        return Response(serializer.data)
   
    
    
    
    def post(self, request, *args, **kwargs):
        cource_id = request.data.get('course')
        images = request.FILES.getlist('image')
        print(cource_id)
        if not images:
            return Response({'message': 'No images provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            courceitem = Course.objects.get(pk=cource_id)
        except Course.DoesNotExist:
            return Response({'message': 'cource  not found'}, status=status.HTTP_404_NOT_FOUND)

        for image in images:
            serializer = CourseImageSerializer(data={'course': cource_id, 'image': image})

            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       
        return Response({'message': 'Images uploaded successfully'}, status=status.HTTP_201_CREATED)
    
    
    
    
    
    


class CourseImageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    
    queryset = CourseImage.objects.all()
    serializer_class = CourseImageSerializer 
    
    
    
    
    
    
       

class YearStudentList(generics.ListCreateAPIView):
    permission_classes = [CustomPermissionfortpo]
    
    queryset = YearStudent.objects.all().order_by("year")
    serializer_class = YearStudentSerializer


class YearStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermissionfortpo]
    
    queryset = YearStudent.objects.all()
    serializer_class = YearStudentSerializer                           
    
    

class StudentPlacementList(generics.ListCreateAPIView):
    permission_classes = [CustomPermissionfortpo]
    queryset = StudentPlacement.objects.all()
    serializer_class = StudentPlacementSerializer
   
class StudentPlacementDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermissionfortpo]
    queryset = StudentPlacement.objects.all()
    serializer_class = StudentPlacementSerializer
       
        
    
    
class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = CustomUser.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
            
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = f'https://http://127.0.0.1:8000//reset-password/{uid}/{token}/'

            # Send an email with the reset URL
            subject = 'Password Reset Request'
            message = f'Click the following link to reset your password: {reset_url}'
            from_email = 'cs20.komaldhote@svceindore.ac.in'
            recipient_list = [email]

            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                return Response({'message': 'Password reset email sent successfully.'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': 'Failed to send email.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    
    
    
class PasswordResetView(GenericAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, uidb64, token):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            password = serializer.validated_data['password']

            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = CustomUser.objects.get(pk=uid)

                if default_token_generator.check_token(user, token):
                    user.set_password(password)
                    user.save()
                    return Response({'message': 'Password reset successfully.'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    
    
    
    
class UserQueryView(APIView):
    def post(self, request, format=None):
        serializer = UserQuerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            student_name=serializer.validated_data["name"]
            phone=serializer.validated_data["phone_number"]
            query=serializer.validated_data["query"]
            student_email=serializer.validated_data["email"]
            
            html_message = render_to_string('email_templateTWO.html', {'student_name': student_name,'phone':phone,'student_email':student_email,'query':query ,})
            # Send an email
            send_mail(
                'New User Query',
                from_email = settings.DEFAULT_FROM_EMAIL,
                message = 'StudentDetails',
                
                recipient_list = ['komaldhote9165@gmail.com'], # Replace with your email address
                fail_silently=False,
                html_message=html_message
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class StudentAdmissionListCreateView(generics.ListCreateAPIView):
    queryset = StudentAdmission.objects.all()
    serializer_class = StudentAdmissionSerializer

    def post(self, request, *args, **kwargs):
        serializer = StudentAdmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Send an email confirmation to the student
            student_email = serializer.validated_data['email']
            student_name = serializer.validated_data['student_name']
            city = serializer.validated_data['city']
            phone = serializer.validated_data['phone']
            department = serializer.validated_data['department']
            course = serializer.validated_data['course']
            
            
            subject = 'Admission Confirmation'
            message = 'Thank you for your admission submission. We have received your queries.'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [student_email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            
            subject = 'Admission new Student'
            message = 'StudentDetails'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['komaldhote9165@gmail.com']
            
            
            html_message = render_to_string('email_template.html', {'student_name': student_name,'city':city,'phone':phone,'department':department,'course':course,'student_email':student_email })

            send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)