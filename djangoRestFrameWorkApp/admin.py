from django.contrib import admin
from .models import Student,Teacher

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade','roll_no', 'age', 'email', 'address', 'phone',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'subject_teaches', 'phone',)


    