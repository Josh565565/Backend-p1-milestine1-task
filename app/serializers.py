from rest_framework import serializers
from .models import MainObject  

class MainObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainObject
        fields = ('id', 'name', 'description')

