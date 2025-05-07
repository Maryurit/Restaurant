from django.db import models

class Restaurante(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre

class Menu(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} - {self.restaurante.nombre}"

class MenuPlato(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="platos")
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('menu', 'plato')

class Reserva(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=255)
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.PositiveIntegerField()

    def __str__(self):
        return f"Reserva de {self.nombre_cliente} en {self.restaurante.nombre}"

class Reseña(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='resenas')
    cliente = models.CharField(max_length=255)
    comentario = models.TextField()
    calificacion = models.PositiveIntegerField()  # 1 a 5

    def __str__(self):
        return f"Reseña de {self.cliente} para {self.restaurante.nombre}"
