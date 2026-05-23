"""
Formularios para la aplicación chess.

Define formularios para crear y editar jugadores y partidas.
"""
from django import forms
from .models import Player, Game


class PlayerForm(forms.ModelForm):
    """
    Formulario para crear y editar jugadores.
    """
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'ranking']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa el nombre'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa el apellido'
            }),
            'ranking': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ranking ELO (por defecto 1000)'
            }),
        }


class GameForm(forms.ModelForm):
    """
    Formulario para crear y editar partidas.
    """
    class Meta:
        model = Game
        fields = ['white_player', 'black_player', 'result', 'played_at', 'opening', 'notes']
        widgets = {
            'white_player': forms.Select(attrs={
                'class': 'form-control'
            }),
            'black_player': forms.Select(attrs={
                'class': 'form-control'
            }),
            'result': forms.Select(attrs={
                'class': 'form-control'
            }),
            'played_at': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'opening': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Ruy López, Gambito de Dama, etc.'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Notas sobre la partida (opcional)'
            }),
        }
