from rest_framework import serializers, status
from .models import *
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
""""
    persons
"""
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id','username','password','email','phoneNumber','is_staff')
        extra_kwargs = {#'password':{'write_only':True,'required':True},
                        'is_staff':{'default':False}}
    def create(self,validated_data):
        person = Person.objects.create_user(**validated_data)
        Token.objects.create(user=person)
        return person

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'student', 'instructor')

class AttendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attend
        fields = ('paymentStatus', 'Student_ID', 'Class_ID')

""""
    students
"""
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','username','password','email','phoneNumber','is_staff')
        extra_kwargs = {#'password':{'write_only':False,'required':True},
                        'attend':{'required':False},
                        'is_staff':{'default':False}}
    def create(self,validated_data):
        student = Student.objects.create_user(**validated_data)
        Token.objects.create(user=student)
        return student
   
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
   
    def to_representation(self, instance):
        rep = super(StudentSerializer, self).to_representation(instance)
        att = Attend.objects.filter(Student_ID=instance.id).all()
        rep['attend']=[]
        for i in att:
            if Rating.objects.filter(student=instance.id, instructor=i.Class_ID.Instructor_ID.id).exists():
                rating = Rating.objects.filter(student=instance.id, instructor=i.Class_ID.Instructor_ID.id).first()

                rep['attend'].append({"PaymentStatus":i.paymentStatus,
                                "ClassName":i.Class_ID.title,
                                "content":i.Class_ID.content,
                                "from":i.Class_ID.fromTime,
                                "to":i.Class_ID.toTime,
                                "day":i.Class_ID.day,
                                "CategoryName":i.Class_ID.Category_ID.name,
                                "Instructor_ID":i.Class_ID.Instructor_ID.username,
                                "Rating":rating.stars,
                                "InsID":i.Class_ID.Instructor_ID.id,
                                })
            else:
                rep['attend'].append({"PaymentStatus":i.paymentStatus,
                "ClassName":i.Class_ID.title,
                "content":i.Class_ID.content,
                "from":i.Class_ID.fromTime,
                "to":i.Class_ID.toTime,
                "day":i.Class_ID.day,
                "CategoryName":i.Class_ID.Category_ID.name,
                "Instructor_ID":i.Class_ID.Instructor_ID.username,
                "Rating":0,
                "InsID":i.Class_ID.Instructor_ID.id,
                                })
        return rep
""""
    instructors
"""
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('id','username','password','email','phoneNumber','salary','bio','picture','is_staff','no_of_ratings', 'avg_rating')
        extra_kwargs = {#'password':{'write_only':False,'required':True},
                        'classinfo':{'required':False},
                        'is_staff':{'default':True}}
    def create(self,validated_data):
        instructor = Instructor.objects.create_user(**validated_data)
        Token.objects.create(user=instructor)
        return instructor
   
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    def to_representation(self, instance):
        rep = super(InstructorSerializer, self).to_representation(instance)
        att = Class.objects.filter(Instructor_ID=instance.id).all()
        rep['classinfo']=[]
        for i in att:
            rep['classinfo'].append({"ClassId":i.id,
                                    "ClassName":i.title,
                                    "content":i.content,
                                    "from":i.fromTime,
                                    "to":i.toTime,
                                    "day":i.day,
                                    "CategoryName":i.Category_ID.name})
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
        model = News
        fields = ('id', 'title', 'date','content', 'picture', 'Category_ID')

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

########################
class AlbumnewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields =  ('id', 'name', 'Collection_ID')
    def to_representation(self, instance):
        rep = super(AlbumnewSerializer, self).to_representation(instance)
        rep['Collection_ID'] = instance.Collection_ID.name
        rep['album']=[]
        if AlbumPhoto.objects.filter(Album_ID=instance.id).exists():
            att = AlbumPhoto.objects.filter(Album_ID=instance.id).first()
            rep['album'].append(str(att.picture))
        else:
            rep['album'].append(str(""))
        return rep

#######################
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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'




# class PasswordSerializer(serializers.Serializer):
#     """
#     Serializer for password change endpoint.
#     """
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)