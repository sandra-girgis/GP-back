from .models import *
from .serializers import *
from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def classes(request):
    classes = Class.objects.all()
    cl_ser = ClassSerializer(classes,many=True)
    return Response(cl_ser.data)





@api_view(['GET','POST'])
def students(request):
    if(request.method =='POST'):
        st_ser = StudentSerializer(data=request.data)
        if st_ser.is_valid():
            st_ser.save()
        return redirect('students')
    students= Student.objects.all()
    st_ser= StudentSerializer(students,many=True)
    return Response(st_ser.data)


api_view(['GET','POST'])
def instructors(request):
    if(request.method =='POST'):
        inst_ser = InstructorSerializer(data=request.data)
        if inst_ser.is_valid():
            inst_ser.save()
        return redirect('instructors')
    instructors= Instructor.objects.all()
    inst_ser= InstructorSerializer(instructors,many=True)
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

#colid= collection id ,, Aid=album id  
@api_view(['GET'])
def albumPhotosnew(request,colid,Aid):
    albumPhotos=AlbumPhoto.objects.filter(Album_ID=Aid)
    newAlbum = albumPhotos.filter(Album_ID__Collection_ID=colid)
    newalbumPhotos_ser=PhotoSerializer(newAlbum,many=True)
    return Response(newalbumPhotos_ser.data)

