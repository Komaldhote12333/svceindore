from rest_framework import serializers
from .models import Department, College, CustomUser, Faculty, Event, Gallery, Achievements, Canteen, Buses, SportImages, Subcollege,  Course, YearStudent, StudentPlacement,CourseImage,EventImages,UserQuery,StudentAdmission

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'email', 'role', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}  
        }

    def create(self, validated_data):
        # Create and return a new CustomUser instance
        user = CustomUser(
            name=validated_data['name'],
            email=validated_data['email'],
            role=validated_data['role'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])  # Set the hashed password
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)   

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class EventImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImages
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    images = EventImgSerializer(many=True, read_only=True)
    
    class Meta:
        model = Event
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = '__all__'

class CanteenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canteen
        fields = '__all__'
8
class BusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buses
        fields = '__all__'

class SportImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportImages
        fields = '__all__'


class CourseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseImage
        fields = '__all__'         


class CourseSerializer(serializers.ModelSerializer):
    images = CourseImageSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = '__all__'
        
      

class SubcollegeSerializer(serializers.ModelSerializer):
    courses_offered = CourseSerializer(many = True , read_only = True)
    
    class Meta:
        model = Subcollege
        fields = '__all__'

        

class StudentPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPlacement
        fields = '__all__'



class YearStudentSerializer(serializers.ModelSerializer):
    placements = StudentPlacementSerializer(many = True , read_only = True)

    class Meta:
        model = YearStudent
        fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):

    subcollege = SubcollegeSerializer(many = True , read_only = True)
    faculty_college = FacultySerializer(many = True , read_only = True)
    placedstudentclg= YearStudentSerializer(many = True , read_only = True)
    college_sport_images= SportImagesSerializer(many = True , read_only = True)
    college_buses  =BusesSerializer (many = True , read_only = True)
    college_achievements = AchievementsSerializer(many = True , read_only = True)
    college_canteen= CanteenSerializer(many = True , read_only = True)
    college_gallery = GallerySerializer(many = True , read_only = True)
    college_events =EventSerializer (many = True , read_only = True)
 
    
    
    class Meta:
        model = College
        fields = '__all__'




class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    
class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)    
    
    
    
class UserQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuery
        fields = '__all__'    
    
    
class StudentAdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAdmission
        fields = '__all__'    