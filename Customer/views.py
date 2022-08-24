from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import Product, User
from .serializers import UserSerializer

class CreateView(APIView):
    pass

class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()