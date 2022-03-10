from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework import request, status, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, renderer_classes,action
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import *
from .serializers import *
############
from rest_framework.authentication import BasicAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated

""""
    persons
"""
class persons(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
""""
    students
"""
class students(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
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
class Class(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['post'])
    def rate_class(self, request, pk=None):

        '''
#wa5d hagat mn l req. w 3shan arbut de b de b2ol self 
#l pk 3shan wa5dha mn l url w maynf3sh amsk fl pk w a3ml beh pk 
#l stars hya eli gayaly 
        '''

        if 'stars' in request.data:
            '''
            create or update 
            #bru7 bl url 3l class w gaybly pk fa b3ml query 3leh ageb eli haqymu aw azbtu 
            '''
            Class = Class.objects.get(id=pk)
            stars = request.data['stars']
            student= request.Student
            student= Student.objects.get(username=username)     
            #print(student) 
            # username = request.data['username']
            #wa5du mn l instance bta3ty 

            try:
                # update 3shan lw 3ndi asln da l mantqy lw msh mwgud y3ml except
                rating = Rating.objects.get(student=Student.id, Class=Class.id) # specific rate 
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Class Rate Updated',
                    'result': Rating_serializer .data      #kan lazm arudelu l serializer eli gayly mn l rate 
                }
                return Response(json , status=status.HTTP_200_OK)

            except:
                # create if the rate not exist 
                
                #create of new rating 
                # rating = Rating.objects.create(stars=stars, Class=Class, user=user)
                rating = Rating.objects.get(student=Student.id, Class=Class.id) # specific rate 
                
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Class Rate Created',
                    'result': Rating_serializer .data
                }
                return Response(json , status=status.HTTP_200_OK)

        else:
            json = {
                'message': 'stars not provided'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)

""""
    Rating
"""
class Rating(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    
    authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = {
            'message': 'Invalid way to create or update '
            }

        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        response = {
            'message': 'Invalid way to create or update '
            }

        return Response(response, status=status.HTTP_400_BAD_REQUEST)


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