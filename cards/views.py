from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Card
from .serializers import CardSerializer
from rest_framework.permissions import IsAuthenticated
from .filters import CardFilter
from rest_framework.filters import  OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter, DjangoFilterBackend,CardFilter]
    filterset_fields = ['title']
    ordering_fields = ['date_created']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

