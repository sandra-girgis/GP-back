from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# from .forms import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


@api_view(['GET'])
def all_classes(request):
    all_classes = Class.objects.all()
    cl_ser = ClassSerializer(all_classes,many=True)
    return Response(cl_ser.data)  