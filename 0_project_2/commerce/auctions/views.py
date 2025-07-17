from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing


def index(request):
    # listings = Listing.objects.all()
    # for listing in listings:
    #     print(f"title: {listing.title}")
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all(),
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def new_listing(request):
    # 1) Check if the user is authenticated
    if not request.user.is_authenticated:
        # return HttpResponseRedirect(reverse("login"))
        return render(request, "auctions/login.html", {
                "message": "You must be logged in to create a listing!"
            })

    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid = request.POST["starting_bid"]
        category = request.POST["category"]
        url_image = request.POST["url_image"]

        print("title:", title)
        print("description:", description)
        print("starting_bid:", starting_bid)
        print("url_image:", url_image)

        new_listing = Listing(
            title=title,
            description=description,
            starting_bid=starting_bid,
            category=category,
            url_image=url_image,
        )
        new_listing.save()

        return render(request, "auctions/new_listing.html", {
            "message": "",
        })
    return render(request, "auctions/new_listing.html", {
        "message": "",
    })

