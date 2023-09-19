from django.contrib import admin
from .models import Department, College, CustomUser, Faculty, Event, Gallery, Achievements, Canteen, Buses, SportImages, Subcollege, Course, YearStudent, StudentPlacement,CourseImage,EventImages

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'name']

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'department', 'college']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['eventname', 'college']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name', 'college']

@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ['college']

@admin.register(Canteen)
class CanteenAdmin(admin.ModelAdmin):
    list_display = ['name', 'college']

@admin.register(Buses)
class BusesAdmin(admin.ModelAdmin):
    list_display = ['name', 'college']

@admin.register(SportImages)
class SportImagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'college']

@admin.register(Subcollege)
class SubcollegeAdmin(admin.ModelAdmin):
    list_display = ['name', 'college']




@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'subcollege']

@admin.register(YearStudent)
class YearStudentAdmin(admin.ModelAdmin):
    list_display = ['year']

@admin.register(StudentPlacement)
class StudentPlacementAdmin(admin.ModelAdmin):
    list_display = ['year', 'company_name', 'job_role', 'package']


admin.site.register(CourseImage)
admin.site.register(EventImages)