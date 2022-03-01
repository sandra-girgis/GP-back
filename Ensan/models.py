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

# Course
DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)
class Course(models.Model):
    title = models.CharField(max_length = 100, null = False)
    content = models.TextField(max_length = 4000, null = False)
    average_rate= models.FloatField(default=0)
    fromTime = models.TimeField()
    toTime = models.TimeField()
    day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    Category_ID= models.ForeignKey(Category, on_delete=models.CASCADE)
    Instructor_ID= models.ForeignKey(Instructor, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
# Review
class Review(models.Model):
    rate =  models.IntegerField(default=0)
    comment = models.CharField(max_length = 200, null = False)
    Student_ID= models.ForeignKey(Student, on_delete=models.CASCADE)
    Category_ID= models.ForeignKey(Category, on_delete=models.CASCADE)
# Attend
class Attend(models.Model):
    paymentStatus =  models.BooleanField(default=False)
    Student_ID= models.ForeignKey(Student, on_delete=models.CASCADE)
    Category_ID= models.ForeignKey(Category, on_delete=models.CASCADE)
    paymentStatus.boolean = True
# News
class News(models.Model):
    title = models.CharField(max_length = 100, null = False)
    content = models.TextField(max_length = 4000, null = False)
    date = models.DateTimeField()
    Category_ID= models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
# NewsPhotos
class NewsPhoto(models.Model):
    picture = models.ImageField(upload_to='img/news/{News_ID}/')
    News_ID= models.ForeignKey(News, on_delete=models.CASCADE)

# Collection
class Collection(models.Model):
    name = models.CharField(max_length = 50, null = False)
    def __str__(self):
        return self.name
# Album
class Album(models.Model):
    name = models.CharField(max_length = 50, null = False)
    Collection_ID= models.ForeignKey(Collection, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
# AlbumPhotos
class AlbumPhoto(models.Model):
    picture = models.ImageField(upload_to='img/{Album_ID}/')
    Album_ID= models.ForeignKey(Album, on_delete=models.CASCADE)