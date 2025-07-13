from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing


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


# Mockup data:
# - Title: Vintage Nintendo GameBoy
# - Description: Original GameBoy from 1989 in excellent condition. Includes Tetris game cartridge and original carrying case. Battery cover intact, screen has no dead pixels.
# - Starting bid value: 49.99
# - URL Image: "https://images.example.com/gameboy.jpg"
#

# mock_listings = [
#     {
#         "title": "Vintage Rolex Watch",
#         "description": "Classic 1970s Rolex Oyster Perpetual, stainless steel, excellent condition.",
#         "starting_bid": 2500,
#         "url_image": "https://images.example.com/rolex.jpg"
#     },
#     {
#         "title": "Apple MacBook Pro 2021",
#         "description": "M1 Pro chip, 16GB RAM, 512GB SSD, lightly used, includes charger.",
#         "starting_bid": 1200,
#         "url_image": "https://images.example.com/macbook.jpg"
#     },
#     {
#         "title": "Signed Michael Jordan Jersey",
#         "description": "Authentic Chicago Bulls jersey signed by Michael Jordan, with certificate.",
#         "starting_bid": 5000,
#         "url_image": "https://images.example.com/jordan_jersey.jpg"
#     },
#     {
#         "title": "LEGO Star Wars Millennium Falcon",
#         "description": "Ultimate Collector Series, unopened box, rare and collectible.",
#         "starting_bid": 350,
#         "url_image": "https://images.example.com/lego_falcon.jpg"
#     }
# ]



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

        # listings_db = Listing.objects.all()

        # print("listings_db:\n", listings_db)

        # new_listing = Listing()
        # new_listing.title = title
        # new_listing.description = description
        # new_listing.starting_bid = starting_bid
        # new_listing.url_image = url_image

        # listings_db = Listing.objects.all()

        # print(new_listing)

        # # listings_db.

        return render(request, "auctions/new_listing.html", {
            "message": "",
        })
    return render(request, "auctions/new_listing.html", {
        "message": "",
    })
