from django.contrib import admin
from .models import City, Continent, Country, State, MainObject

# Register your models here.

admin.site.register(City)
admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(MainObject)