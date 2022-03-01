from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Student
class Student(User):
    username= models.TextField(max_length = 100, null = False)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,null=False)
    def __str__(self):
        return self.username
#StudentPhone
class StudentPhone(models.Model): 
    Student_ID = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='author')
    phoneNumber = models.CharField(max_length=11)
    def __str__(self):
        return self.phoneNumber
# Instructor
class Instructor(User):
    username= models.TextField(max_length = 100, null = False)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,null=False)
    salary =  models.IntegerField(default=0)
    numberLectures =  models.IntegerField(default=0)
    picture = models.ImageField(upload_to='img/instructors/')
    bio = models.TextField(max_length = 2000, null = False)
    def __str__(self):
        return self.username
# InstructorPhone
class InstructorPhone(models.Model): 
    Instructor_ID = models.ForeignKey(Instructor, on_delete=models.CASCADE,related_name='author')
    phoneNumber = models.CharField(max_length=11)
    def __str__(self):
        return self.phoneNumber
# Category
class Category(models.Model):
    name = models.CharField(max_length = 50, null = False)
    def __str__(self):
        return self.name

