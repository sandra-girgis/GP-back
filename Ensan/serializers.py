from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token

""""
    persons
"""
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('username','password','email','phoneNumber','is_staff')
        extra_kwargs = {'password':{'write_only':True,'required':True}}
    def create(self,validated_data):
        person = Person.objects.create_user(**validated_data)
        Token.objects.create(user=person)
        return person
""""
    students
"""
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('username','password','email','phoneNumber','is_staff','attend')
        extra_kwargs = {'password':{'write_only':True,'required':True}}
    def create(self,validated_data):
        student = Student.objects.create_user(**validated_data)
        Token.objects.create(user=student)
        return student
    
    def to_representation(self, instance):
        rep = super(StudentSerializer, self).to_representation(instance)
        att = Attend.objects.filter(Student_ID=instance.id).all()
        rep['attend']=[]
        for i in att:
            rep['attend'].append({"PaymentStatus":i.paymentStatus,"ClassName":i.Class_ID.title})
        return rep
""""
    instructors
"""
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('username','password','email','phoneNumber','is_staff','classinfo')
        extra_kwargs = {'password':{'write_only':True,'required':True}}
    def create(self,validated_data):
        instructor = Instructor.objects.create_user(**validated_data)
        Token.objects.create(user=instructor)
        return instructor
    def to_representation(self, instance):
        rep = super(InstructorSerializer, self).to_representation(instance)
        att = Class.objects.filter(Instructor_ID=instance.id).all()
        rep['classinfo']=[]
        for i in att:
            rep['classinfo'].append({"ClassName":i.title,"CategoryName":i.Category_ID.name})
        return rep
""""
    Category
"""
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
""""
    classes
"""
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(ClassSerializer, self).to_representation(instance)
        rep['Category_ID'] = instance.Category_ID.name
        rep['Instructor_ID'] = instance.Instructor_ID.username
        return rep
""""
    news
"""
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model =News 
        fields = ('id','title','content','date','picture','Category_ID')
    
    def to_representation(self, instance):
        rep = super(NewsSerializer, self).to_representation(instance)
        rep['Category_ID'] = instance.Category_ID.name
        return rep
""""
    collections
"""
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
""""
    albums all albums (select one album)
"""
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
    def to_representation(self, instance):
        rep = super(AlbumSerializer, self).to_representation(instance)
        rep['Collection_ID'] = instance.Collection_ID.name
        return rep
""""
    albumPhotos may be delete all photos (select one photo)
"""
class AlbumPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumPhoto
        fields = '__all__'
    def to_representation(self, instance):
        rep = super(AlbumPhotoSerializer, self).to_representation(instance)
        rep['Album_ID'] = instance.Album_ID.name
        return rep
""""
    albumPhotosnew all photos related to specific album 
    important
"""
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumPhoto
        fields = '__all__'
    def to_representation(self, instance):
            rep = super(PhotoSerializer, self).to_representation(instance)
            rep['Album_ID'] = instance.Album_ID.name
            return rep