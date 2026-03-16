from django.http import HttpResponse #sends response to the server
from django.shortcuts import render # this can display the HTML template and send the data to the template and then return the response to the server


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