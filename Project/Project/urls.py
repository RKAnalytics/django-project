"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



#while making a sub urls.py we have to control transfer the main urls.py to the sub urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= "Home"),
    path('about/', views.about, name= "About"),
    path('projects/', views.projects, name= "Projects"),
    path('contact/', views.contact, name= "Contact"),
    path('app/', include ("app.urls")), # this is the line that tells django to look for the urls.py file in the app folder and then look for the urls in that file and then return the response to the server
    
]
