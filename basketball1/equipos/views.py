from django.shortcuts import render,redirect
from . import forms
from .serializers import JugadorSerializer, EquipoSerializer, PartidoSerializer
from equipos.forms import FormularioEquipo, FormularioJugador, FormularioPartido
from equipos.models import Equipo, Jugador, Partido
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
import json
from django.views.decorators.csrf import csrf_exempt
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
@csrf_exempt
def listadoJugadores1(request):
    if request.method == "GET":
        jugadores = Jugador.objects.all()
        data = {
            'jugadores': list(jugadores.values('nombre', 'apellido', 'posicion', 'altura', 'peso', 'edad', 'equipo'))
        }
        return JsonResponse(data)

    elif request.method == "POST":
        try:
            body = json.loads(request.body)
            print (body)
            equipo = Equipo.objects.get(nombreEquipo=body.get('equipo'))
            jugador = Jugador.objects.create(
                nombre=body.get('nombre'),
                apellido=body.get('apellido'),
                posicion=body.get('posicion'),
                altura=body.get('altura'),
                peso=body.get('peso'),
                edad=body.get('edad'),
                equipo=equipo,
            )

            return JsonResponse({'message': 'Jugador creado con éxito', 'id': jugador.id}, status=201)

        except Exception as e:
            # Respuesta en caso de error
            return JsonResponse({'error': str(e)}, status=400)


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

#--------------------------------------------------------#

@csrf_exempt
def listadoEquipos1(request):
    if request.method == "GET":
        equipos = Equipo.objects.all()
        data = {
            'equipos': list(equipos.values('nombreEquipo', 'ciudad', 'conferencia', 'estadio', 'anioFundacion'))
        }
        return JsonResponse(data)

    elif request.method == "POST":
        try:
            body = json.loads(request.body)
            print (body)
            equipo = Equipo.objects.create(
                nombreEquipo=body.get('nombre'),
                ciudad=body.get('apellido'),
                conferencia=body.get('posicion'),
                estadio=body.get('altura'),
                anioFundacion=body.get('peso'),
            )

            return JsonResponse({'message': 'Equipo creado con éxito', 'id': equipo.id}, status=201)

        except Exception as e:
            # Respuesta en caso de error
            return JsonResponse({'error': str(e)}, status=400)

    
@api_view(['GET','POST'])
def lista_equipos(request):
    if request.method == 'GET':
        equipos = Equipo.objects.all()
        serializer = EquipoSerializer(equipos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = EquipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET','PUT','DELETE'])
def equipo_detalle(request, pk):
    try:
        equipo = Equipo.objects.get(pk=pk)
    except Equipo.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = EquipoSerializer(equipo)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = EquipoSerializer(equipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    if request.method == 'DELETE':
        equipo.delete()
        return Response(status=204)



#---------------------------------------------------------------#

@csrf_exempt
def listadoPartidos1(request):
    if request.method == "GET":
        partidos = Partido.objects.all()
        data = {
            'Partidos': list(partidos.values('fecha', 'hora','estadio', 'equipo'))
        }
        return JsonResponse(data)

    elif request.method == "POST":
        try:
            body = json.loads(request.body)
            print (body)
            equipo = Equipo.objects.get(nombreEquipo=body.get('equipo'))
            partido = Partido.objects.create(
                fecha=body.get('fecha'),
                hora=body.get('hora'),
                estadio=body.get('estadio'),
                equipo=equipo,
            )

            return JsonResponse({'message': 'Partido creado con éxito', 'id': partido.id}, status=201)

        except Exception as e:
            # Respuesta en caso de error
            return JsonResponse({'error': str(e)}, status=400)

    
@api_view(['GET','POST'])
def lista_partidos(request):
    if request.method == 'GET':
        partidos = Partido.objects.all()
        serializer = PartidoSerializer(partidos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PartidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET','PUT','DELETE'])
def partido_detalle(request, pk):
    try:
        equipo = Equipo.objects.get(pk=pk)
    except Equipo.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = PartidoSerializer(equipo)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = PartidoSerializer(equipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    if request.method == 'DELETE':
        equipo.delete()
        return Response(status=204)
    
#-------------------------------------------------------------#

class jugadoresViewSets(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

class equiposViewSets(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class partidosViewSets(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer