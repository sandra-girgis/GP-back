from rest_framework import serializers, status
from .models import *
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','username', 'password', 'email', 'phoneNumber', 'is_staff')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        student = Student.objects.create_user(**validated_data)
        Token.objects.create(user=student)
        return student

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('username', 'password', 'email', 'phoneNumber', 'is_staff')
        # extra_kwargs = {'password':{'write_only':True,'required':True}}

    def create(self, validated_data):
        person = Person.objects.create_user(**validated_data)
        Token.objects.create(user=person)
        return person

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('username','password','email','phoneNumber','is_staff')
        extra_kwargs = {'password':{'write_only':True,'required':True}}
    def create(self,validated_data):
        instructor = Instructor.objects.create_user(**validated_data)
        Token.objects.create(user=instructor)
        return instructor

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
