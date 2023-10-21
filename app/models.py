# models.py
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Continent(Location):
    pass

class Country(Location):
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

class State(Location):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class City(Location):
    state = models.ForeignKey(State, on_delete=models.CASCADE)

class MainObject(models.Model):
    name = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.postcode}'
