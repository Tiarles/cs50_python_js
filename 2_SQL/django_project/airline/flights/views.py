from django.shortcuts import render

from .models import Flight

def index(request):
    return render (request, "flights/index.html", {
        "flights": Flight.objects.all(),
    })


def flights(request, flight_id):
    flight = Flight.objects.all(id=flight_id)
    return render(request, "flights/flights.html", {})
