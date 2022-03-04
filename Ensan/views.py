from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# from .forms import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


@api_view(['GET'])
def classes(request):
    classes = Class.objects.all()
    cl_ser = ClassSerializer(classes,many=True)
    return Response(cl_ser.data)


@api_view(['GET'])
def students(request):
    students = Student.objects.all()
    st_ser = StudentSerializer(students,many=True)
    return Response(st_ser.data)


############################
@api_view(['GET'])
def instructors(request):
    instructor=Instructor.objects.all()
    inst_ser=InstructorSerializer(instructors,many=True)
    return Response(inst_ser.data)


@api_view(['GET'])
def category(request):
    category =Category.objects.all()
    cat_ser=CategorySerializer(category,many=True)
    return Response(cat_ser.data)



@api_view(['GET'])
def albumPhotos(request):
    albumPhotos=AlbumPhoto.objects.all()
    albumPhotos_ser=AlbumPhotoSerializer(albumPhotos,many=True)
    return Response(albumPhotos_ser.data)

@api_view(['GET'])
def albums(request):
    albums = Album.objects.all()
    album_ser= AlbumSerializer(albums,many=True)
    return Response(album_ser.data)

@api_view(['GET'])
def news(request):
    news= News.objects.all()
    news_ser= NewsSerializer(news,many=True)
    return Response(news_ser.data)






@api_view(['GET'])
def collections(request):
    collections= Collection.objects.all()
    col_ser= CollectionSerializer(collections,many=True)
    return Response(col_ser.data)
