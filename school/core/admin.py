from django.contrib import admin

from core.models import Person, Course, Grade # import 3 classes from the file core/models.py

@admin.register(Person) # register the Person model
class PersonAdmin(admin.ModelAdmin): # we create a class called PersonAdmin that inherits from admin.ModelAdmin
    pass # stub

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass