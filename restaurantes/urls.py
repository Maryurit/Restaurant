from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RestauranteViewSet, PlatoViewSet, MenuViewSet,
    MenuPlatoViewSet, ReservaViewSet, ReseñaViewSet
)

router = DefaultRouter()
router.register(r'restaurantes', RestauranteViewSet)
router.register(r'platos', PlatoViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'menuplatos', MenuPlatoViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'resenas', ReseñaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
