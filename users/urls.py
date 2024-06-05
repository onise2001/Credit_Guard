from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateUserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'signup', CreateUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view())
]
