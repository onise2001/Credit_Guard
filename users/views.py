from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class CreateUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



