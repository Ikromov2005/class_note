from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views

urlpatterns = [
    # localhost:8000/api/notes/
    path('notes/', views.NoteViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    # localhost:8000/api/notes/:pk
    path('notes/<int:pk>/', views.NoteViewSet.as_view({
        'put': 'update',
        'patch': 'partial_update',
        'get': 'retrieve',
        'delete': 'destroy',
    })),
     # localhost:8000/api/users/
    path('users/', views.UserViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    # localhost:8000/api/users/:pk
    path('users/<int:pk>/', views.UserViewSet.as_view({
        'put': 'update',
        'patch': 'partial_update',
        'get': 'retrieve',
        'delete': 'destroy',
    })),
]