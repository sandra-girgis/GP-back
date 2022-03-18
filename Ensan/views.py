from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view , action
from rest_framework import request, status, viewsets
from .models import *
from .serializers import *
############
from rest_framework.authentication import BasicAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated

""""
    students
"""
class students(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

""""
    persons
"""
class persons(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

""""
    instructors
"""
class instructors(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    @action(detail=True, methods=['post'])
    def rate_meal(self, request, pk=None):

        if 'stars' in request.data:
            '''
            create or update 
            '''
            instructor = Instructor.objects.get(id=pk)
            stars = request.data['stars']
            student = request.user

            try:
                # update
                rating = Rating.objects.get(student=student.id, instructor=instructor.id) # specific rate 
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message':  'Instructor Rate has been Updated',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_400_BAD_REQUEST)

            except:
                # create if the rate not exist 
                rating = Rating.objects.create(stars=stars, student=student, instructor=instructor)
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Instructor Rate has been Created',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_200_OK)

        else:
            json = {
                'message': 'stars not provided'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)

'''
    Rating
'''
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

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

@api_view(['GET'])
def albumsnew(request,cid):
    album=Album.objects.filter(Collection_ID=cid).all()
    newalbum_ser=AlbumnewSerializer(album,many=True)
    return Response(newalbum_ser.data)

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


@api_view(['GET'])
def get_user(request,id):
    user=Person.objects.filter(username=id).first()
    user_ser=UserSerializer(user,many=False)
    return Response(user_ser.data)

class attend(viewsets.ModelViewSet):
    queryset = Attend.objects.all()
    serializer_class = AttendSerializer
