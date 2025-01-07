from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('blogpost/<id>/', views.blogpost, name="blogpost"),
    path('about/', views.about, name="about"),
    path('addpost/', views.addPost, name="addpost"),
    path('editpost/<id>/', views.editPost, name="editpost"),
]