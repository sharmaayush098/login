from django.contrib.auth.models import User
from django.db import models


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)


class Standard(models.Model):
    std_name = models.CharField(max_length=10)
    std_integer = models.IntegerField(unique=True)


class Notifications(models.Model):
    notify_date = models.DateField()
    message = models.CharField(max_length=1000)


class NationalHolidays(models.Model):
    month = models.CharField(max_length=20)
    holiday_date = models.DateField()
    holiday_event = models.CharField(max_length=100)
