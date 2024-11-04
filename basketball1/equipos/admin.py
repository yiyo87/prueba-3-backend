from django.contrib import admin
from equipos.models import Equipo, Jugador, Partido

# Register your models here.
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombreEquipo', 'ciudad', 'conferencia', 'estadio', 'anioFundacion')

admin.site.register(Equipo, EquipoAdmin)



class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'posicion', 'altura', 'peso', 'edad')

admin.site.register(Jugador, JugadorAdmin)


class PartidoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora','estadio')

admin.site.register(Partido, PartidoAdmin)

