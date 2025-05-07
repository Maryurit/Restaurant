from rest_framework import serializers
from .models import Restaurante, Plato, Menu, MenuPlato, Reserva, Reseña

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = '__all__'

class MenuPlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPlato
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    platos = MenuPlatoSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class ReseñaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reseña
        fields = '__all__'
