from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Counter
import datetime
# Create your views here.

def index(request):
    data = []
    dict = {}
    for i in Counter.objects.all():
        dict["id"] = i.id
        dict["title"] = i.title
        dict["basetime"] = str(i.basetime)
        dict["stopwatch"] = i.stopwatch
        data.append(dict)
    return HttpResponse("{}".format(data), 200)
