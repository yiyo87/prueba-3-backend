from django.db import models
from django.utils import timezone

# Create your models here.
class Equipo(models.Model):
    CONFERENCIAS =[
        ('E','ESTE'),
        ('W','OESTE'),
        ]

    nombreEquipo = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    conferencia = models.CharField(max_length=2,choices=CONFERENCIAS,default='E')
    estadio = models.CharField(max_length=50)
    anioFundacion = models.IntegerField()

    def __str__(self):
        return self.nombreEquipo


class Jugador(models.Model):
    POSICIONES = [
        ('PG', 'Base (Point Guard)'),
        ('SG', 'Escolta (Shooting Guard)'),
        ('SF', 'Alero (Small Forward)'),
        ('PF', 'Ala-Pivot (Power Forward)'),
        ('C', 'Pivot (Center)'),
    ]
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    posicion = models.CharField(max_length=2,choices=POSICIONES, default='PG')
    altura = models.CharField(max_length=50)
    peso = models.CharField(max_length=50)
    edad = models.IntegerField()
    equipo = models.ForeignKey(
        Equipo, 
        on_delete=models.CASCADE,  # Si se elimina el equipo, se eliminan sus jugadores
        related_name='jugadores',  # Permite acceder a los jugadores desde un equipo como equipo.jugadores.all()
        null=True,  # Permite que un jugador no tenga equipo
        blank=True  # Permite dejar el campo vacío en formularios
    )
    


    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Partido(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)
    estadio = models.CharField(max_length=255, default='Estadio desconocido')
    equipo  = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos',null=True, blank=True)

    def __str__(self):
        return f"Partido en {self.estadio} - {self.fecha.strftime('%Y-%m-%d')} {self.hora.strftime('%H:%M')}"