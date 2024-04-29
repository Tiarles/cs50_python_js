from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def tiarles(request):
    return HttpResponse("Hello, Tiarles!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name: str):
    return HttpResponse(f"Hello, {name.capitalize()}!")
