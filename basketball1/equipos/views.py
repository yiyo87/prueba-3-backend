from django.shortcuts import render,redirect
from . import forms
from .serializers import JugadorSerializer, EquipoSerializer, PartidoSerializer
from equipos.forms import FormularioEquipo, FormularioJugador, FormularioPartido
from equipos.models import Equipo, Jugador, Partido
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

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

def listadoJugadores1(resquest):
    jugadores = Jugador.objects.all()
    data = {'jugadores': list(jugadores.values('nombre','apellido','posicion','altura','peso','edad','equipo'))}
    return JsonResponse(data)

@api_view(['GET','POST'])
def lista_jugadores(request):
    if request.method == 'GET':
        jugadores = Jugador.objects.all()
        serializer = JugadorSerializer(jugadores, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = JugadorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET','PUT','DELETE'])
def jugadores_detalle(request, pk):
    try:
        jugador = Jugador.objects.get(pk=pk)
    except Jugador.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = JugadorSerializer(jugador)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = JugadorSerializer(jugador, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    if request.method == 'DELETE':
        jugador.delete()
        return Response(status=204)
    

    

#---------------------------------------------------------------#

class jugadoresViewSets(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

class equiposViewSets(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class partidosViewSets(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer