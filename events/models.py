from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    organizer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
