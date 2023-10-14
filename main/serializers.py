from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name', 'email')
        extra_kwargs = {
            'password':{'write_only': True},
            'email':{'required': True}
        }
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'email')
        
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = ('user','weight','height')

class UserMoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserMood
        fields = ('id','user','mood','date')
        
class MemoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Memories
        fields = '__all__'