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
from django.urls import path
from equipos import views

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
    
]
