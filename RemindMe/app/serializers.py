from rest_framework import serializers
from app.models import *
from django.contrib.auth.models import User


class RemidermeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
        
        