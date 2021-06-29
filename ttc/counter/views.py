from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Counter
import datetime
# Create your views here.

def get(request):
    data = []
    for i in Counter.objects.all():
        dict = {}
        dict["iid"] = i.iid
        dict["title"] = i.title
        dict["basetime"] = str(i.basetime)
        dict["stopwatch"] = i.stopwatch
        data.append(dict)
    return HttpResponse("{}".format(data), 200)
