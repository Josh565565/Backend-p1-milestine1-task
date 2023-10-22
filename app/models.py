# models.py
from django.db import models

class Continent(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class MainObject(models.Model):
    name = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} - {self.postcode}'
