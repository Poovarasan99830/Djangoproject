from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("welcome django......!")

def fan(request):
    return render(request,"one.html")


def Television(request):
    return render(request,"bootstrap.html")

def Television2(request):
    return render(request,"bootstrap2.html")




print("welcome...!")  