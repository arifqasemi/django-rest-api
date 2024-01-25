from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from users.userserializer import LoginSerializer,RegisterSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class Authentication(APIView):
    def get(self,request):
        return Response('this is')
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            print(user)
            
            if user:
                token = Token.objects.get(user=user).key
                return Response({'token':token})
            else:
                return Response('Wrong username or password')
        return Response(serializer.errors, status=400)

        
        
class RegisterView(APIView):
    def get(self,request):
        return Response('this is')
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            token = Token.objects.get(user=account).key
            data['email'] = account.email
            data['username'] = account.username
            data['token'] = token
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
    
    
    



class LogoutView(APIView):
    # authentication_classes = [TokenAuthentication]
   

    def post(self, request):
        request.auth.delete()  
        return Response({'detail': 'Successfully logged out'}, status=status.HTTP_200_OK)

