"""
URL configuration for basketball project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from equipos import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('jugadoresviewsets', views.jugadoresViewSets)
router.register('equiposviewsets', views.equiposViewSets)
router.register('partidoviewsets', views.partidosViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.index),

    path('equipos/',views.listadoEquipos),
    path('jugadores/',views.listadoJugadores),
    path('partidos/',views.listadoPartidos),

    path('agregarequipos/',views.agregarEquipos),
    path('agregarjugador/',views.agregarJugador),
    path('agregarpartido/',views.agregarPartido),

    path('eliminarjugador/<int:id>',views.eliminarJugador),
    path('actualizarjugador/<int:id>',views.actualizarJugador),

    path('eliminarEquipos/<int:id>',views.eliminarEquipo),
    path('actualizarEquipos/<int:id>',views.actualizarEquipos),

    path('eliminarpartido/<int:id>',views.eliminarPartido),
    path('actualizarpartido/<int:id>',views.actualizarPartido),

    path('jugadoresapi/',views.listadoJugadores1),
    path('jugadoresfunction/',views.lista_jugadores),
    path('jugadoresapi2/<int:pk>',views.jugadores_detalle),

    path('equiposapi/',views.listadoEquipos1),
    path('equiposfunction/',views.lista_equipos),
    path('equipoapi2/<int:pk>',views.equipo_detalle),

    path ('partidoapi/',views.listadoPartidos1),

    path('', include(router.urls)),
    
]
