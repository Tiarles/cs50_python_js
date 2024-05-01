from django.shortcuts import render

# Create your views here.

def index(request):
    from datetime import datetime
    today = datetime.now()
    # if :
    return render(request, "newyear/index.html",{
        "newyear": today.day == 1 and today.month == 1
    })