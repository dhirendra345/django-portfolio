from django.urls import path
from . import views
from .views import ProjectCreateView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('', views.project_list, name='projects'),
    path('add/', ProjectCreateView.as_view(), name='project_add'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
    path('<slug:slug>/edit/', ProjectUpdateView.as_view(), name='project_edit'),
    path('<slug:slug>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
]
