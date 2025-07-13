
# Import all models
from auctions.models import User, Listing

# Adding users
pope = User(
    first_name = "Pope",
    username="Pope Francis",
    last_name = "Francis",
    email = "pope@vatican.vc",
    password = "iLoveJesus123"
)
pope.save()

david = User(
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
    user = User(
        first_name=entry[0],
        username=entry[0],
        last_name=entry[1],
        email=entry[2],
        password=entry[3]
    )
    user.save()


# Listing = Listing()



# jfk = Listing()
# User, 

# # Create some new airports
# jfk = Airport(code="JFK", city="New York")
# lhr = Airport(code="LHR", city="London")
# cdg = Airport(code="CDG", city="Paris")
# nrt = Airport(code="NRT", city="Tokyo")

# # Save the airports to the database
# jfk.save()
# lhr.save()
# cdg.save()
# nrt.save()

# # Add a flight and save it to the database
# f = Flight(origin=jfk, destination=lhr, duration=414)
# f.save()

# # Display some info about the flight
# In [14]: f
# Out[14]: <Flight: 1: New York (JFK) to London (LHR)>
# In [15]: f.origin
# Out[15]: <Airport: New York (JFK)>

# # Using the related name to query by airport of arrival:
# In [17]: lhr.arrivals.all()
# Out[17]: <QuerySet [<Flight: 1: New York (JFK) to London (LHR)>]>



# # Using the filter command to find all airports based in New York
# In [3]: Airport.objects.filter(city="New York")
# Out[3]: <QuerySet [<Airport: New York (JFK)>]>

# # Using the get command to get only one airport in New York
# In [5]: Airport.objects.get(city="New York")
# Out[5]: <Airport: New York (JFK)>

# # Assigning some airports to variable names:
# In [6]: jfk = Airport.objects.get(city="New York")
# In [7]: cdg = Airport.objects.get(city="Paris")

# # Creating and saving a new flight:
# In [8]: f = Flight(origin=jfk, destination=cdg, duration=435)
# In [9]: f.save()