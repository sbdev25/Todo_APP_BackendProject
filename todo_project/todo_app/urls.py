from django.contrib import admin 
from django.urls import path 
from .views import MyTokenObtainPairView
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', MyTokenObtainPairView),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('todos/' , views.getTodos),
    path('todos/add/' , views.addTodos),
    path('todos/edit/<int:pk>' , views.updateTodo),
    path('todos/delete/<int:pk>',views.deleteTodo),
]