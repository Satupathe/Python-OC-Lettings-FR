from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include(("lettings.urls", 'lettings'), namespace='lettings')),
    path('profiles/', include(("profiles.urls", 'profiles'), namespace='profiles')),
    path('admin/', admin.site.urls),
]
