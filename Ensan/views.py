from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework import request, status, viewsets

""""
    persons
"""
class persons(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
""""
    students
"""
class students(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
""""
    instructors
"""
class instructors(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
""""
    category
"""
class category(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
""""
    classes
"""
class classes(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
""""
    news
"""
class news(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
""""
    collections
"""
class collections(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
""""
    albums all albums (select one album)
"""
class albums(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
""""
    albumPhotos may be delete all photos (select one photo)
"""
class albumPhotos(viewsets.ModelViewSet):
    queryset = AlbumPhoto.objects.all()
    serializer_class = AlbumPhotoSerializer
""""
    albumPhotosnew all photos related to specific album 
    important
"""
@api_view(['GET'])
def albumPhotosnew(request,Aid):
    albumPhotos=AlbumPhoto.objects.filter(Album_ID=Aid).all()
    newalbumPhotos_ser=PhotoSerializer(albumPhotos,many=True)
    return Response(newalbumPhotos_ser.data)