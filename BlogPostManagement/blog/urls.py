from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('blogs', BlogViewSet ,basename='blog')
router.register('users', UserViewSet)


urlpatterns = [
    path('api/', include(router.urls))
]