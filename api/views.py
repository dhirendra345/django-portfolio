from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from projects.models import Project
from pages.models import Contact
from .serializers import ProjectSerializer, ContactSerializer


# GET all projects
class ProjectListAPI(generics.ListAPIView):
    queryset = Project.objects.order_by('-created_at')
    serializer_class = ProjectSerializer


# GET single project by slug
class ProjectDetailAPI(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'


# POST new project (admin only)
class ProjectCreateAPI(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAdminUser]


# POST contact message
class ContactCreateAPI(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
