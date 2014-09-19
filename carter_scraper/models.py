from django.db import models


class Car(models.Model):
    vin = models.CharField(max_length=17, blank=True, null=True)
    stock_number = models.CharField(max_length=5, blank=True, null=True)
    first_seen = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)
    year = models.IntegerField(max_length=4, blank=True, null=True)
    mileage = models.IntegerField(max_length=6, blank=True, null=True)
    transmission = models.CharField(max_length=30, blank=True, null=True)
    ex_color = models.CharField(max_length=80, blank=True, null=True)
    in_color = models.CharField(max_length=80, blank=True, null=True)
    engine = models.CharField(max_length=80, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=10, blank=True, null=True)
    trim = models.CharField(max_length=10, blank=True, null=True)
    number = models.CharField(max_length=5, blank=True, null=True)


class Price(models.Model):
    car = models.ForeignKey('Car')
    time = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(max_length=5, blank=True, null=True)


class Feature(models.Model):
    car = models.ForeignKey('Car')
    feature = models.CharField(max_length=80)