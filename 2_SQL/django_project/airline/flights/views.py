from django.shortcuts import render, HttpResponse

from .models import Flight, Airport


def index(request):
    return render (request, "flights/index.html", {
        "flights": Flight.objects.all(),
    })


def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)

    return render(request, "flights/flights.html", {
        "flight": flight, 
    })
