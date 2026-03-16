#app url.py its a sub url.py of the main project 
# In this file we will define the url patterns for the app and map them to the views functions defined in the views.py file of the app
# from django.contrib import admin
from django.urls import path #this is used to import the path function which is used to define the url patterns for the app in simmple words it helps to map the urls to the views functions in the app
from . import views #this is used to import the views module from the current directory (app) which contains the view functions that will be mapped to the urls defined in this file

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.appsfunc, name= "appfunc"),
    # path('about/', views.about, name= "About"),
    # path('projects/', views.projects, name= "Projects"),
    # path('contact/', views.contact, name= "Contact"),
    
]