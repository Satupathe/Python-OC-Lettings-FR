from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'profiles'
urlpatterns = [
    path('', views.index, name='profiles_index'),
    path('profile/<str:username>/', views.profile, name='profile'),
]