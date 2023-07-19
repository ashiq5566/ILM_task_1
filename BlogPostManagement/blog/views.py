from django.shortcuts import render
from .models import *
from rest_framework import viewsets, generics
from .serializers import *
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# def index(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         category = request.POST.get('blogs')
#         tag = request.POST.get('tag')
        
#         Blog(title=title,content=content,category=category,tag=tag).save()
        
#     return render(request, 'index.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = (TokenAuthentication,)