from django.shortcuts import render,redirect
from . import forms

from equipos.forms import FormularioEquipo, FormularioJugador, FormularioPartido
from equipos.models import Equipo, Jugador, Partido

# Create your views here.

def index(request):
    return render (request,'equipos/index.html')


#------------------------------------------------------------------#

#LEER

def listadoEquipos(request):
    equipos = Equipo.objects.all()
    data = {'equipos':equipos}
    return render (request,'equipos/equipos.html', data)

def listadoJugadores(resquest):
    jugadores = Jugador.objects.all()
    data = {'jugadores': jugadores}
    return render (resquest, 'equipos/jugadores.html',data)

def listadoPartidos(resquest):
    partidos = Partido.objects.all()
    data = {'partidos': partidos}
    return render (resquest, 'equipos/partidos.html', data)


#------------------------------------------------------------------#

#CREAR
def agregarEquipos(request):
    form = FormularioEquipo()
    if request.method == 'POST':
        form = forms.FormularioEquipo(request.POST)
        if form.is_valid():
            form.save()
            return listadoEquipos(request)
    data= {'form':form}
    return render(request, 'equipos/agregarEquipo.html', data)

def agregarJugador(request):
    form = FormularioJugador()
    if request.method == 'POST':
        form = forms.FormularioJugador(request.POST)
        if form.is_valid():
            form.save()
            return listadoJugadores(request)
    data = {'form': form}
    return render(request, 'equipos/agregarJugador.html', data)

def agregarPartido(request):
    form = FormularioPartido()
    if request.method == 'POST':
        form = forms.FormularioPartido(request.POST)
        if form.is_valid():
            form.save()
            return listadoPartidos(request)
    data = {'form': form}
    return render(request, 'equipos/agregarPartido.html', data)


#---------------------------------------------------------------------#

#ELIMINAR

def eliminarEquipo(request,id):
    equipo = Equipo.objects.get(id=id)
    equipo.delete()
    return redirect('/equipos')

def eliminarJugador(request,id):
    jugador = Jugador.objects.get(id=id)
    jugador.delete()
    return redirect('/jugadores')

def eliminarPartido(request,id):
    partido = Partido.objects.get(id=id)
    partido.delete()
    return redirect('/partidos')


#-----------------------------------------------------------------------#


#ACTUALIZAR
def actualizarEquipos(request,id):
    equipo = Equipo.objects.get(id=id)
    form = FormularioEquipo(instance=equipo)
    if request.method == 'POST':
        form = FormularioEquipo(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return listadoEquipos(request)
    
    data = {'form': form}
    return render(request, 'equipos/agregarEquipo.html', data)

def actualizarJugador(request,id):
    jugador = Jugador.objects.get(id=id)
    form = FormularioJugador(instance=jugador)
    if request.method == 'POST':
        form = FormularioJugador(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            return listadoJugadores(request)
    
    data = {'form': form}
    return render(request, 'equipos/agregarJugador.html', data)

def actualizarPartido(request,id):
    partido = Partido.objects.get(id=id)
    form = FormularioPartido(instance=partido)
    if request.method == 'POST':
        form = FormularioPartido(request.POST, instance=partido)
        if form.is_valid():
            form.save()
            return listadoPartidos(request)
    
    data = {'form': form}
    return render(request, 'equipos/agregarPartido.html', data)



#----------------------------------------------------------------#