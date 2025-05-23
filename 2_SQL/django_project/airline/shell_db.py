
from flights.models import Flight

f = Flight(origin="New York", destination="London", duration=415)

f
# Out[5]: <Flight: Flight object (None)>

f.save()

Flight.objects.all()
# Out[7]: <QuerySet [<Flight: Flight object (1)>]>

flights = Flight.objects.all()
flight = flights.first()

######################################################################

from flights.models import Airport, Flight

jfk = Airport(code="JFK", city="New York")
jfk.save()

lhr = Airport(code="LHR", city="London")
lhr.save()

cdg = Airport(code="CDG", city="Paris")
cdg.save()

nrt = Airport(code="NRT", city="Tokyo")
nrt.save()

f = Flight(origin=jfk, destination=lhr, duration=415)
f.save()

f.origin
# Out[9]: <Airport: New York (JFK)>

f.origin.city
# Out[10]: 'New York'

f.origin.code
# Out[11]: 'JFK'

lhr.arrivals.all()
# Out[15]: <QuerySet [<Flight: 1 New York (JFK) London (LHR)>]>

##########################################
# cd  C:\Tiarles\cs50_python_js\2_SQL\django_project\airline
# ipython
# python.exe .\manage.py shell
from flights.models import Airport, Flight

Airport.objects.filter(city="New York")
# Out[13]: <QuerySet [<Airport: New York (JFK)>]>

Airport.objects.get(city="New York")
# Out[14]: <Airport: New York (JFK)>

jfk = Airport.objects.get(city="New York")
lhr = Airport.objects.get(city="London")
cdg = Airport.objects.get(city="Paris")
nrt = Airport.objects.get(city="Tokyo")

f = Flight(origin=jfk, destination=cdg, duration=435)
f.save()

# Username (leave blank to use 'david'): tiarles
# Email address: tiarlesmoralles@hotmail.com
# Password: 
