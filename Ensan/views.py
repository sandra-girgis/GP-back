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
    
##############
@api_view(['GET'])
def albumsnew(request,cid):
    album=Album.objects.filter(Collection_ID=cid).all()
    newalbum_ser=AlbumnewSerializer(album,many=True)
    return Response(newalbum_ser.data)
    
##############
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


# @action(methods=['put'], detail=True)
# def change_password(self, request, pk):
#     serializer = PasswordSerializer(data=request.data)
#     if serializer.is_valid():
#         user = get_object_or_404(User, pk=pk)
#         if user != request.user:
#             return Response({'error': "Cannot change other user's password"},
#                             status=status.HTTP_403_FORBIDDEN)
#         else:
#             if not user.check_password(serializer.data.get('old_password')):
#                 return Response({'old_password': ['Wrong password.']},
#                                 status=status.HTTP_400_BAD_REQUEST)
#             user.set_password(request.POST.get('new_password'))
#             user.save()
#     else:
#         return Response(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)
#     return Response({'details': 'Success'}, status=status.HTTP_200_OK)