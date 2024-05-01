from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world!")
    # return HttpResponse("<h1 style=\"color:blue\">Hello, world!</h1>")
    return render(request, "hello/index.html")

def tiarles(request):
    return HttpResponse("Hello, Tiarles!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name: str):
    # return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize(),
    })
