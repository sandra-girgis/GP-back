from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

import os

""""
    persons
"""
class Person(AbstractUser):
    phoneNumber = models.CharField(max_length=11,null=True)
""""
    students
"""
class Student(Person):
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        
""""
    instructors
"""
def no_of_ratings(self):
        Instructor = apps.get_model(app_label='Ensan', model_name='Instructor')
        ratings = Rating.objects.filter(Instructor=self)
        return len(ratings)
        # return Instructor.objects.filter(status='A').count() * Instructor.DEFAULT_VALUE

def avg_rating(self):
        Instructor = apps.get_model(app_label='Ensan', model_name='Instructor')
        # sum of ratings stars  / len of rating how many ratings 
        sum = 0
        ratings = Rating.objects.filter(Instructor=self) # no of ratings happened to the class

        for x in ratings:
            sum += x.stars

        if len(ratings) > 0:
            avrage_rating=sum / len(ratings)

            return avrage_rating
        else:
            return 0

class Instructor(Person):
    Stars =  models.ForeignKey('Rating',related_name="ratinginfo", on_delete=models.CASCADE)
    Review=models.OneToOneField('Rating',related_name="ratinginfo", on_delete=models.CASCADE)
    no_of_ratings = models.IntegerField(default=0)
    avg_rating = models.IntegerField(default=0)
    salary =  models.IntegerField(default=0)
    picture = models.ImageField(upload_to='images/instructors/')
    bio = models.TextField(max_length = 2000, null = False)
    # Rating=models.FloatField(default=0)
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'

        # if len(ratings) > 0:
        #     self.Rating =sum / len(ratings)
        #     self.save()
        #     return self.Rating
        # else:
        #     return 0
# ,'no_of_ratings','avg_rating'
""""
    Category
"""
class Category(models.Model):
    name = models.CharField(max_length = 50, null = False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
""""
    classes
"""
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
    Category_ID= models.ForeignKey(Category,related_name="classinfo", on_delete=models.CASCADE)
    Instructor_ID= models.ForeignKey(Instructor,related_name="classinfo", on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'
    
""""
    Rating
"""
class Rating(models.Model):
    Student= models.ForeignKey(Student, on_delete=models.CASCADE)
    Stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    Review=models.TextField(max_length = 4000, null = True)
    Instructor= models.ForeignKey(Instructor, on_delete=models.CASCADE)
    avrage_rating =models.FloatField(default=0)
    no_of_ratings=models.FloatField(default=0)

    def __str__(self):
        return str(self.Instructor)

            #USER CAN'T rate the same class 2 times 
    class Meta:
        unique_together = (('Student', 'Instructor'),)
        index_together =  (('Student', 'Instructor'),)


""""
    news
"""
def get_upload_path(instance, filename):
    """ creates unique-Path & filename for upload """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance, ext)
    return os.path.join(
        'images','News', filename
    )

class News(models.Model):
    title = models.CharField(max_length = 100, null = False)
    content = models.TextField(max_length = 4000, null = False)
    date = models.DateTimeField()
    picture = models.ImageField(upload_to=get_upload_path)
    Category_ID= models.ForeignKey(Category,related_name="newscategory", on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
""""
    collections
"""
class Collection(models.Model):
    name = models.CharField(max_length = 50, null = False)
    def __str__(self):
        return self.name
""""
    albums
"""
class Album(models.Model):
    name = models.CharField(max_length = 50, null = False)
    Collection_ID= models.ForeignKey(Collection,related_name="collection", on_delete=models.CASCADE)
    def __str__(self):
        return self.name
""""
    albumPhotos
"""
def get_upload_path2(instance,filename):
    """ creates unique-Path & filename for upload """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.Album_ID.id, ext)
    return os.path.join(
        'images','Albums',instance.Album_ID.Collection_ID.name, instance.Album_ID.name, filename
    )

class AlbumPhoto(models.Model):
    Album_ID= models.ForeignKey(Album,related_name="album", on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=get_upload_path2)
""""
    Attend no view
"""
class Attend(models.Model):
    paymentStatus =  models.BooleanField(default=False)
    Student_ID= models.ForeignKey(Student,related_name="attend", on_delete=models.CASCADE)
    Class_ID= models.ForeignKey(Class,related_name="attend", on_delete=models.CASCADE)
    paymentStatus.boolean = True
    def __str__(self):
        return self.Class_ID.title
