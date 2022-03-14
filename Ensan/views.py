from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view , action
from rest_framework import request, status, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .models import *
from .serializers import *

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

#         '''
# #wa5d hagat mn l req. w 3shan arbut de b de b2ol self
# #l pk 3shan wa5dha mn l url w maynf3sh amsk fl pk w a3ml beh pk
# #l stars hya eli gayaly

#             #bru7 bl url 3l class w gaybly pk fa b3ml query 3leh ageb eli haqymu aw azbtu
#             '''






class instructors(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    @action(detail=True, methods=['post'])
#             create or update
    def rate_class(self, request, pk=None):
        if 'stars' in request.data:
            Instructor = Instructor.objects.get(id=pk)
            stars = request.data['stars']
            student = request.Student
            # student= Student.objects.get(username=username)
            # print(student)
            # wa5du mn l instance bta3ty
            # update 3shan lw 3ndi asln da l mantqy lw msh mwgud y3ml except
            # kan lazm arudelu l serializer eli gayly mn l rate

            try:
                rating = Rating.objects.get(stars=stars, Student=student.id, Instructor=Instructor.id)  # specific rate
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Instructor Rate Updated',
                    'result': Rating_serializer.data
                }
                return Response(json, status=status.HTTP_200_OK)

            except:
                # create if the rate not exist
                # create of new rating
                #rating = Rating.objects.create(stars=stars, Instructor=Instructor.id, user=user)

                rating = Rating.objects.get(student=Student.id, Instructor=Instructor.id)  # specific rate
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Instructor Rate Created',
                    'result': Rating_serializer.data
                }
                return Response(json, status=status.HTTP_200_OK)

        else:
            json = {
                'message': 'stars not provided'
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)









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
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)












""""
    Rating
"""


class rating(viewsets.ModelViewSet):
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


@api_view(['GET'])
def get_user(request,id):
    user=Person.objects.filter(username=id).first()
    user_ser=UserSerializer(user,many=False)
    return Response(user_ser.data)


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
