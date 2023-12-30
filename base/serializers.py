from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):  # Fix typo in class name
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']
