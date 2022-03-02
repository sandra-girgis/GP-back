from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

#Student
class Student(User):
    phoneNumber = models.CharField(max_length=11)
    def __str__(self):
        return self.username
# Instructor
class Instructor(User):
    salary =  models.IntegerField(default=0)
    picture = models.ImageField(upload_to='images/instructors/')
    bio = models.TextField(max_length = 2000, null = False)
    phoneNumber = models.CharField(max_length=11)
    def __str__(self):
        return self.username
# Category
class Category(models.Model):
    name = models.CharField(max_length = 50, null = False)
    def __str__(self):
        return self.name

# Class
DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)
class Class(models.Model):
    title = models.CharField(max_length = 100, null = False)
    content = models.TextField(max_length = 4000, null = False)
    fromTime = models.TimeField()
    toTime = models.TimeField()
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    Category_ID= models.ForeignKey(Category, on_delete=models.CASCADE)
    Instructor_ID= models.ForeignKey(Instructor, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
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

def get_upload_path(instance, filename):
    """ creates unique-Path & filename for upload """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.News_ID.id, ext)
    return os.path.join(
        'images','News', instance.News_ID.title, filename
    )

# NewsPhotos
class NewsPhoto(models.Model):
    News_ID= models.ForeignKey(News, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=get_upload_path)

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

def get_upload_path2(instance, filename):
    """ creates unique-Path & filename for upload """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.Album_ID.id, ext)
    return os.path.join(
        'images','Albums',instance.Album_ID.Collection_ID.name, instance.Album_ID.name, filename
    )

# AlbumPhotos
class AlbumPhoto(models.Model):
    Album_ID= models.ForeignKey(Album, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=get_upload_path2)
