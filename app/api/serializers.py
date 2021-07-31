from django.db.models.base import Model
from rest_framework import serializers
from app.models import *

class tamañoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tamaño
        fields = '__all__'

class ingredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'
        
class sandwichSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sandwich
        fields = '__all__'

class ingredientesSandwichSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientesSandwich
        fields = '__all__'

class ordenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'

class ordenSandwichSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenSandwich
        fields = '__all__'