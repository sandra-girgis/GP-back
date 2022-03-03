from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# from .forms import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


@api_view(['GET'])
def all_classes(request):
    all_classes = Class.objects.all()
    cl_ser = ClassSerializer(all_classes,many=True)
    return Response(cl_ser.data)


@api_view(['GET'])
def all_students(request):
    all_students = Student.objects.all()
    st_ser = StudentSerializer(all_students,many=True)
    return Response(st_ser.data)


############################
@api_view(['GET'])
def all_instructors(request):
    all_instructor=Instructor.objects.all()
    inst_ser=InstructorSerializer(all_instructors,many=True)
    return Response(inst_ser.data)


@api_view(['GET'])
def all_category(request):
    all_category =Category.objects.all()
    cat_ser=CategorySerializer(all_category,many=True)
    return Response(cat_ser.data)



@api_view(['GET'])
def all_albumPhotos(request):
    all_albumPhotos=AlbumPhoto.objects.all()
    albumPhotos_ser=AlbumPhotoSerializer(all_albumPhotos,many=True)
    return Response(albumPhotos_ser.data)

@api_view(['GET'])
def all_albums(request):
    all_albums = Album.objects.all()
    album_ser= AlbumSerializer(all_albums,many=True)
    return Response(album_ser.data)

@api_view(['GET'])
def all_news(request):
    all_news= News.objects.all()
    news_ser= NewsSerializer(all_news,many=True)
    return Response(news_ser.data)

def all_newsPhoto(request):
    all_newsPhoto= NewsPhoto.objects.all()
    newsPhoto_ser= NewsPhotoSerializer(all_newsPhoto,many=True)
    return Response(newsPhoto_ser.data)




@api_view(['GET'])
def all_collections(request):
    all_collections= Collection.objects.all()
    col_ser= Collectionerializer(all_collections,many=True)
    return Response(col_ser.data)
