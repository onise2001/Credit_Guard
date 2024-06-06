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
from rest_framework.permissions import SAFE_METHODS
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.



class CardViewSet(APIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['title']
    ordering_fields = ['date_created']


    def post(self, request, *args, **kwargs):
        request.data['user_id'] = request.user.id
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data,status=status.HTTP_201_CREATED )
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, reqeust,*args, **kwargs):
        my_queryset = self.get_queryset()
        serializer = self.serializer_class(my_queryset, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        

    def get_queryset(self):
        queryset = Card.objects.filter(user=self.request.user)
        return queryset
    
   





# I think the problem was ambiguous with it's requirements for the CardViewSet so I wrote it two different ways, therefore there are also
# two serializers, one for each viewset, also two different URLs, one with DefaultRouter and other as viewset

# class CardViewSet(ModelViewSet):
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer
#     permission_classes = [IsAuthenticated]
#     filter_backends = [OrderingFilter, DjangoFilterBackend,CardFilter]
#     filterset_fields = ['title']
#     ordering_fields = ['date_created']

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)






