from django.test import TestCase
from .models import Counter
from django.urls import reverse
# Create your tests here.

def create_data(iid, title, stopwatch="00:00:00"):
    return Counter.objects.create(iid=iid, title=title, stopwatch=stopwatch)

class CounterGetValueTest(TestCase):
    def test_vlaues_in_data(self):
        print("-----------------------This is for testing the values in the data---------------------------")
        for i in range(10):
            create_data(iid=i, title=str(i))
        data = []
        for i in Counter.objects.all():
            dict = {}
            dict["iid"] = i.iid
            dict["title"] = i.title
            dict["basetime"] = str(i.basetime)
            dict["stopwatch"] = i.stopwatch
            data.append(dict)
        for d in data:
            print(d)

# class CounterGetViewTest(TestCase):
#     def test_get_views(self):
#         for i in range(10):
#             create_data(title=str(i))
#         response = self.client.get(reverse("counter:get"))
#         data = []
#         for i in Counter.objects.all():
#             dict = {}
#             dict["id"] = i.id
#             dict["title"] = i.title
#             dict["basetime"] = str(i.basetime)
#             dict["stopwatch"] = i.stopwatch
#             data.append(dict)
#         print(response.content)
#         self.assertQuerysetEqual(response.content, data)
