from django.db import models
from django.contrib.auth.models import AbstractUser
import os

# Create your models here.

#Student
class Person(AbstractUser):
    phoneNumber = models.CharField(max_length=11)

class Student(Person):
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

# Instructor
class Instructor(Person):
    salary =  models.IntegerField(default=0)
    picture = models.ImageField(upload_to='images/instructors/')
    bio = models.TextField(max_length = 2000, null = False)
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'

# Category
class Category(models.Model):
    name = models.CharField(max_length = 50, null = False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

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
    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

# Attend
class Attend(models.Model):
    paymentStatus =  models.BooleanField(default=False)
    Student_ID= models.ForeignKey(Student, on_delete=models.CASCADE)
    Class_ID= models.ForeignKey(Class, on_delete=models.CASCADE)
    paymentStatus.boolean = True


def get_upload_path(instance, filename):
    """ creates unique-Path & filename for upload """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance, ext)
    return os.path.join(
        'images','News', filename
    )

# News
class News(models.Model):
    title = models.CharField(max_length = 100, null = False)
    content = models.TextField(max_length = 4000, null = False)
    date = models.DateTimeField()
    picture = models.ImageField(upload_to=get_upload_path)
    Category_ID= models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

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


