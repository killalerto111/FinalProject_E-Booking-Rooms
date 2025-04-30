from django.db import models
class Booking(models.Model):
    name = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    attendees = models.IntegerField()
    phone = models.CharField(max_length=20)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    purpose = models.CharField(max_length=255)
    equipments = models.TextField(blank=True)
    other = models.TextField(blank=True)