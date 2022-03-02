from rest_framework import serializers
from .models import *

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
        #('id','fname','lname','age','student_track')
