from django.urls import path, include
from .views import CardViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cards', CardViewSet, basename='cardsviewset')

urlpatterns = [
    path('', include(router.urls)),
]

