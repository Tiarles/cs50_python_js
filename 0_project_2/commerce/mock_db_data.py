
# Import all models
from auctions.models import User, Listing

# Adding users
pope = User.objects.create_user(
    first_name = "Pope",
    username="Pope Francis",
    last_name = "Francis",
    email = "pope@vatican.vc",
    password = "iLoveJesus123"
)
pope.save()

david = User.objects.create_user(
    first_name = "David",
    username="David Pop",
    last_name = "Pop",
    email = "dadid@pop.hr",
    password = "vet4Life"
)
david.save()

# Random users entries

random_entries = [
    ("Julia"   , "Hartman" , "julia.hartman@fakemail.com"  , "R3dSky!92"   ),
    ("Leo"     , "Marquez" , "leo.marquez82@demo.net"      , "Giraffe#204" ),
    ("Sabrina" , "Koenig"  , "sabrina.k@mockmail.org"      , "Moon^Dash77" ),
    ("Diego"   , "Morales" , "diego.m@nowhere.email"       , "Tiger!Run23" ),
    ("Tyler"   , "Bennett" , "ty.bennett@placeholder.co"   , "JetStream88*"),
    ("Amira"   , "Nassar"  , "amira.nassar@nomail.test"    , "EchoWave_19" ),
    ("Marcus"  , "Doyle"   , "marcus.doyle33@samplebox.io" , "RocketPass54"),
    ("Linnea"  , "Stokes"  , "linnea.s@fakeservice.com"    , "Cloud9Wind!" ),
    ("Hana"    , "Tanaka"  , "hana.t@tempmail.net"         , "Snowfall#31" ),
]

for entry in random_entries:   
    user = User.objects.create_user(
        first_name=entry[0],
        username=entry[0],
        last_name=entry[1],
        email=entry[2],
        password=entry[3]
    )
    user.save()


# Listing items

mock_listings = [
    {
        "title": "Vintage Nintendo GameBoy",
        "description": "Original GameBoy from 1989 in excellent condition. Includes Tetris game cartridge and original carrying case. Battery cover intact, screen has no dead pixels.",
        "starting_bid": 49.99,
        "category": "electronics",
        "url_image": "https://images.example.com/gameboy.jpg"
    },
    {
        "title": "Vintage Rolex Watch",
        "description": "Classic 1970s Rolex Oyster Perpetual, stainless steel, excellent condition.",
        "starting_bid": 2500,
        "category": "fashion",
        "url_image": "https://images.example.com/rolex.jpg"
    },
    {
        "title": "Apple MacBook Pro 2021",
        "description": "M1 Pro chip, 16GB RAM, 512GB SSD, lightly used, includes charger.",
        "starting_bid": 1200,
        "category": "electronics",
        "url_image": "https://images.example.com/macbook.jpg"
    },
    {
        "title": "Signed Michael Jordan Jersey",
        "description": "Authentic Chicago Bulls jersey signed by Michael Jordan, with certificate.",
        "starting_bid": 5000,
        "category": "collectibles",
        "url_image": "https://images.example.com/jordan_jersey.jpg"
    },
    {
        "title": "LEGO Star Wars Millennium Falcon",
        "description": "Ultimate Collector Series, unopened box, rare and collectible.",
        "starting_bid": 350,
        "category": "toys",
        "url_image": "https://images.example.com/lego_falcon.jpg"
    }
]

for item in mock_listings:
    listing = Listing(
        title=item["title"],
        description=item["description"],
        starting_bid=item["starting_bid"],
        category=item["category"],
        url_image=item["url_image"],
    )
    listing.save()
