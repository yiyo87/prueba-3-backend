from django import forms
from equipos.models import Equipo,Jugador,Partido
from django.forms.widgets import TimeInput

class FormularioEquipo(forms.ModelForm):
    class Meta:
        model= Equipo
        fields = '__all__'

class FormularioJugador(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'

class FormularioPartido(forms.ModelForm):
    class Meta:
        model = Partido
        fields = '__all__'
        widgets = {
            "fecha":forms.DateInput(attrs={'type':'date'}),
            "hora": forms.TimeInput(attrs={'type':'time'}),
            }


