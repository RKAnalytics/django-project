from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello Welcome to my first project Home page.")
    return render(request, 'website/index.html') 
#render takes the HTML tempalte and adds the data for the view and then returns back as a HTTp response

def about(request):
    # return HttpResponse("Hello Welcome to my first project About page.")
    return render(request, "website/about.html")

def projects(request):
    # return HttpResponse("Hello Welcome to my first project project page.")
    return render(request, "website/projects.html")

def contact(request):
    # return HttpResponse("This is my conatct page")
    return render(request, "website/contact.html")