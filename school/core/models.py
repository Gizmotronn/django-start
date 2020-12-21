from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Person(models.Model): # Create a model called "Person" that inherits from models.Model class
    last_name = models.TextField() # Three attributes - first name, last name, and courses (which is a foreign key relating to the Course class/model)
    first_name = models.TextField()
    courses = models.ManyToManyField("Course", blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Course(models.Model): 
    name = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name}, {self.year}"

class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE) # make a grade attribute for each course in each student
    grade = models.PositiveSmallIntegerField( # the student's grade in a course can be a value from 1-100
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.grade}, {self.person}, {self.course}"