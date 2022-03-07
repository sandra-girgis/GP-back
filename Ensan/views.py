from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


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
######################################


# @api_view(['GET'])
# def api_student_details(request,st_id):
#     all_st = Student.objects.get(id=st_id)
#     sr_serializer = StudentSerializer(all_st, many=False)
#     return Response(sr_serializer.data)



#colid= collection id ,, Aid=album id  
@api_view(['GET'])
def albumPhotosnew(request,colid,Aid):
    albumPhotos=AlbumPhoto.objects.filter(Album_ID=Aid)
    newAlbum = albumPhotos.filter(Album_ID__Collection_ID=colid)
    newalbumPhotos_ser=PhotoSerializer(newAlbum,many=True)
    return Response(newalbumPhotos_ser.data)




###########################
# @api_view(['POST'])
# def api_student_create(request):
#     sr_serializer = StudentSerializer(data=request.data)
#     if sr_serializer.is_valid():
#         sr_serializer.save()
#     return redirect('api-list')





##############omar
# @api_view(['POST','GET'])
# def register(request):
#     # create register form
#     signup_form = registerSerializer()
#     # if the method post
#     if(request.method =='POST'):
#         signup_form = registerSerializer(request.POST)  #input from user
#         if(signup_form.is_valid()):
#             # the user is active (not block)
#             signup_form.save()
#             # msg = 'User account created for username: ' + signup_form.cleaned_data.get('username')
#             # messages.info(request, msg)
#             return redirect('persons')
#     # if the method not post
#     return Response(signup_form.data)



# # Log in page
# def loginPg(request):
#     # if the user already logedin
#     if request.user.is_authenticated:
#         # return to home
#         return redirect('home')
#     else:
#         # if the method is post (contain data)
#         if request.method == 'POST':
#             name = request.POST.get('username')
#             passwd = request.POST.get('password')
#             user = authenticate(username= name, password =passwd)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 # show error massage if user name or password was incorrect
#                 messages.info(request, 'User name or password is incorrect')
#         # go to login if :
#         # user not authenticated or the name or password not correct
#         return render(request, 'djapp/login.html')





# Sign out function
# def signoutPg(request):
#     logout(request)
#     return redirect('home')