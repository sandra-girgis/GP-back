from rest_framework import serializers
from .models import *

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(ClassSerializer, self).to_representation(instance)
        rep['Category_ID'] = instance.Category_ID.name
        rep['Instructor_ID'] = instance.Instructor_ID.username
        return rep

#how to call attend.paymentstatus in student here
#  
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('username','password','email','phoneNumber')
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'
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
        fields = ('id','title','content','date','picture','Category_ID')
    
    def to_representation(self, instance):
        rep = super(NewsSerializer, self).to_representation(instance)
        rep['Category_ID'] = instance.Category_ID.name
        return rep

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
