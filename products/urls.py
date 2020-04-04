from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:prod_id>', views.detail, name='detail'),
    path('<int:prod_id>/upvote', views.upvote, name='upvote'),
]
