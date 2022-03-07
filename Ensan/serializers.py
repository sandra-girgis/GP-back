from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
        #('id','fname','lname','age','student_track')

#how to call attend.paymentstatus in student here
#  
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AlbumPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumPhoto
        fields = '__all__'
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model =News 
        fields = '__all__'
# ('title','content','date','Category_ID')




class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumPhoto
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
   

   ########################omar 
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('username','password','email','phoneNumber','is_staff')
        extra_kwargs = {'password':{'write_only':True,'required':True}}
    def create(self,validated_data):
        student = Student.objects.create_user(**validated_data)
        Token.objects.create(user=student)
        return student
   
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('username','password','email','phoneNumber','is_staff')
        extra_kwargs = {'password':{'write_only':True,'required':True}}
    def create(self,validated_data):
        instructor = Instructor.objects.create_user(**validated_data)
        Token.objects.create(user=instructor)
        return instructor
  


# class registerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Person
#         fields = ('username','password','email','phoneNumber','is_staff')
