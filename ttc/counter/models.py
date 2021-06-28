from django.db import models
from django.utils import timezone

# Create your models here.
class Counter(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    basetime = models.DateTimeField(default=timezone.now)
    stopwatch = models.CharField(max_length=20)

    def __str__(self):
        return self.title
