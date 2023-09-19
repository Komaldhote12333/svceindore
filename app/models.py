from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class College(models.Model):
    name = models.CharField(max_length=100, unique=True)
    hprincipaldimg = models.ImageField(upload_to='principalimg/',null=True)
    principalname = models.CharField(max_length=100, null=True)
    Aboutprincipal = models.CharField(max_length=100,null=True )
    
    
    

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    # Choices for the 'role' field
    TPO = 'tpo'
    ADMIN = 'admin'
    SUPERADMIN = 'Superadmin'
    ROLE_CHOICES = [
        (TPO, 'Training and Placement Officer'),        
        (ADMIN, 'Admin'),
        (SUPERADMIN, 'Superadmin'),
    ]

    name = models.CharField(max_length=100, default="")
    email = models.EmailField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ADMIN)
    username = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.username

class Faculty(models.Model):
    image = models.ImageField(upload_to='Faculty/',default="")
    name = models.CharField(max_length=244) 
    subject = models.CharField(max_length=600)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True, related_name='faculty_members')
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, related_name='faculty_college')
    role = models.CharField(max_length=100 ,null=True)

class Event(models.Model):
    eventname = models.CharField(max_length=244) 
    image = models.ImageField(upload_to='Events/',default="")
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, related_name='college_events') 
    event_date = models.DateField( null=True)



    

    
    
     
class EventImages(models.Model):
    Events = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Events_images2/', null=True)


    

class Gallery(models.Model):
    name = models.CharField(max_length=244) 
    image = models.ImageField(upload_to='Gallery/',default="")
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, related_name='college_gallery')

class Achievements(models.Model):
    image = models.ImageField(upload_to='Achiements/',default="")
    
    name = models.CharField(max_length=244, default="koo") 
    
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, related_name='college_achievements')

class Canteen(models.Model):
    image = models.ImageField(upload_to='Cantten/',default="")
    
    name = models.CharField(max_length=244) 
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, related_name='college_canteen')

class Buses(models.Model):
    image = models.ImageField(upload_to='Bus/',default="")
    
    name = models.CharField(max_length=244) 
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, related_name='college_buses')

class SportImages(models.Model):
    image = models.ImageField(upload_to='Sport/',default="")
    
    name = models.CharField(max_length=244) 
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, related_name='college_sport_images')


class Subcollege(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, related_name='subcollege', on_delete=models.CASCADE)
    duration = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    subcollege = models.ForeignKey(Subcollege, related_name='courses_offered', on_delete=models.CASCADE)
    fees = models.CharField(max_length=100,null=True)
    hodname = models.CharField(max_length=100,null=True)
    hodimg = models.ImageField(upload_to='hodimg/',null=True)
    hoddetais = models.CharField(max_length=100,null=True)
    aboutdepartment = models.TextField(null=True)
       
    
    def __str__(self):
        return self.name
    
    
class CourseImage(models.Model):
    course = models.ForeignKey(Course, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='course_images/')  # Specify the image field

    def __str__(self):
        return f"Image for {self.course.name}"
    
        

class YearStudent(models.Model):
    year = models.IntegerField(default=2024)
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, related_name='placedstudentclg')  
    def __str__(self):
        return str(self.year)

class StudentPlacement(models.Model):
    year = models.ForeignKey(YearStudent, on_delete=models.CASCADE, null=True ,related_name='placements')
    company_name = models.CharField(max_length=100,null=True , default="") 
    job_role = models.CharField(max_length=100, null=True ,default="") 
    pakageLpa = models.CharField(max_length=100,null=True , default="") 
    studentname = models.CharField(max_length=100,null=True , default="") 
    
    package = models.IntegerField(default=0,null=True ,)
    college = models.CharField(max_length=100,null=True , default="") 
    image = models.ImageField(upload_to='Placedstudent/',default="")
    
    
    def __str__(self):
        return f"{self.company_name} ({self.year})"
    

class UserQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
    
    
class StudentAdmission(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    admission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name    