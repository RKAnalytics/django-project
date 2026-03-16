from django.shortcuts import render #this is used to import the render function from the django.shortcuts module which is used to render the templates and return an HttpResponse object with the rendered content


def appsfunc(request):
    return render(request, 'app/app_index.html')

# Create your views here.
