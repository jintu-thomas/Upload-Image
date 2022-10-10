from dataclasses import field
from distutils.command.upload import upload
from urllib import request
from rest_framework import serializers
from .models import Images,User


class RegSeializer(serializers.ModelSerializer):
    password = serializers.CharField(style = {'input_type':'password'},write_only = True)
    password2 = serializers.CharField(style = {'input_type':'password'},write_only = True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile_no', 'username', 'password','password2']
    
     
    def save(self,validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            mobile_no=validated_data['mobile_no'],
        )

        password = validated_data['password']
        password2 = validated_data['password2']

        if password and password2 and password != password2:
            raise serializers.ValidationError("Passwords doesn't match")

        user.set_password(password)
        user.save()
        return user

class uploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['upload']

    def upload(self,users,validated_data):
        img = Images(
            upload = validated_data['upload'],
            users=users
        )
        print(img)
        return img