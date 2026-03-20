from django.shortcuts import render


def basefunc(request):
    return render(request, 'base.html')