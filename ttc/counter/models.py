from django.db import models
from django.utils import timezone

# Create your models here.
class Counter(models.Model):
    iid = models.IntegerField(unique=True, null=True)
    title = models.CharField(max_length=50)
    basetime = models.DateTimeField(default=timezone.now)
    stopwatch = models.CharField(max_length=20, default="00:00:00")

    def __str__(self):
        return self.title

    def show_values(self):
        print(self.iid)
        print(self.title)
        print(self.basetime)
        print(self.stopwatch)
