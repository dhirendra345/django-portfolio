from django.urls import path
from .views import (
    ProjectListAPI,
    ProjectDetailAPI,
    ProjectCreateAPI,
    ContactCreateAPI
)

urlpatterns = [
    path('projects/', ProjectListAPI.as_view(), name='api_projects'),
    path('projects/<slug:slug>/', ProjectDetailAPI.as_view(), name='api_project_detail'),
    path('projects/create/', ProjectCreateAPI.as_view(), name='api_project_create'),
    path('contact/', ContactCreateAPI.as_view(), name='api_contact'),
]
