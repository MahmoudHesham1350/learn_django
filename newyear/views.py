from django.shortcuts import render
import datetime

# Create your views here.
def is_newyear(date : datetime.datetime.now) -> bool:
    return date.month == 1 and date.day == 1


def index(request):
    datetime_now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": is_newyear(datetime_now)
    })

