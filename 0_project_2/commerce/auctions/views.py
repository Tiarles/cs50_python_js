from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User


def index(request):
    return render(request, "auctions/index.html")


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


# From Specification:
#
# - Create Listing: Users should be able to visit a page to create a
# new listing. They should be able to specify:
#   - A title for the listing,
#   - A text-based description, and
#   - What the starting bid should be. 
# Users should also optionally be able to:
#   -  Provide a URL for an image for the listing and/or a category
#      (e.g. Fashion, Toys, Electronics, Home, etc.).
#
# Mockup data:
# - Title: Vintage Nintendo GameBoy
# - Description: Original GameBoy from 1989 in excellent condition. Includes Tetris game cartridge and original carrying case. Battery cover intact, screen has no dead pixels.
# - Starting bid value: 49.99
# - URL Image: "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Game-Boy-FL.png/800px-Game-Boy-FL.png"
# 



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
        url_image = request.POST["url_image"]

        print("title:", title)
        print("description:", description)
        print("starting_bid:", starting_bid)
        print("url_image:", url_image)

        return render(request, "auctions/new_listing.html", {
            "message": "Invalid URL",
        })
    return render(request, "auctions/new_listing.html", {
        "message": "Invalid URLInvalid URL",
    })
