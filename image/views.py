from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import *
# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        data={}
        serializer = RegSeializer(data = request.data)
        if serializer.is_valid(raise_exception=ValueError):
            users = serializer.save(validated_data=request.data)

            token = Token.objects.get(user=users).key
            data['token']=token

        else:
            data = serializer.errors
        return Response(data)

class CustomAuthLogin(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
      
        token,created = Token.objects.get_or_create(user = user)
        return Response({
            'token': token.key,
            'user_id':user.id,
            'username':user.username,
            'email':user.email
        })
        
class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        logout(request._request)
        return Response('User Logged out successfully')

@api_view(('POST',))
@permission_classes([IsAuthenticated])
def upload_image(request):
    try:
        user = request.user
        serializer = uploadSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            file = request.data['upload']

            img = Images.objects.create(
                upload = file,
                users=user
            )
            return Response("success")
                
    except Exception as e:
        return Response("error")




