from rest_framework import viewsets
from .models import Restaurante, Plato, Menu, MenuPlato, Reserva, Reseña
from .serializers import (
    RestauranteSerializer, PlatoSerializer, MenuSerializer,
    MenuPlatoSerializer, ReservaSerializer, ReseñaSerializer
)
from django_filters.rest_framework import DjangoFilterBackend


class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoria', 'ubicacion']

class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuPlatoViewSet(viewsets.ModelViewSet):
    queryset = MenuPlato.objects.all()
    serializer_class = MenuPlatoSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReseñaViewSet(viewsets.ModelViewSet):
    queryset = Reseña.objects.all()
    serializer_class = ReseñaSerializer
