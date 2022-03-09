from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework import request, status, viewsets

from .models import *
from .serializers import *

class students(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class persons(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class instructors(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer    


