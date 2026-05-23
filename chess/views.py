"""
Vistas para la aplicación chess.

Define vistas basadas en clases genéricas para gestionar jugadores y partidas.
"""
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Player, Game
from .forms import PlayerForm, GameForm


# ==================== VISTAS DE JUGADOR ====================

class PlayerListView(ListView):
    """
    Vista para listar todos los jugadores.
    
    Muestra un listado de todos los jugadores ordenados por ranking.
    """
    model = Player
    template_name = 'chess/player_list.html'
    context_object_name = 'players'
    paginate_by = 10


class PlayerDetailView(DetailView):
    """
    Vista para mostrar los detalles de un jugador.
    
    Muestra información del jugador y todas sus partidas.
    """
    model = Player
    template_name = 'chess/player_detail.html'
    context_object_name = 'player'

    def get_context_data(self, **kwargs):
        """Añade información de partidas al contexto."""
        context = super().get_context_data(**kwargs)
        player = self.get_object()
        
        # Obtener todas las partidas del jugador
        games_as_white = player.games_as_white.all()
        games_as_black = player.games_as_black.all()
        
        # Combinar y ordenar
        all_games = sorted(
            list(games_as_white) + list(games_as_black),
            key=lambda x: x.played_at,
            reverse=True
        )
        
        context['games'] = all_games
        return context


class PlayerCreateView(CreateView):
    """
    Vista para crear un nuevo jugador.
    
    Muestra un formulario para ingresar los datos del nuevo jugador.
    """
    model = Player
    form_class = PlayerForm
    template_name = 'chess/player_form.html'
    success_url = reverse_lazy('chess:player_list')


class PlayerUpdateView(UpdateView):
    """
    Vista para editar un jugador existente.
    
    Muestra un formulario para modificar los datos del jugador.
    """
    model = Player
    form_class = PlayerForm
    template_name = 'chess/player_form.html'


class PlayerDeleteView(DeleteView):
    """
    Vista para eliminar un jugador.
    
    Pide confirmación antes de eliminar el jugador.
    """
    model = Player
    template_name = 'chess/player_confirm_delete.html'
    success_url = reverse_lazy('chess:player_list')


# ==================== VISTAS DE PARTIDA ====================

class GameListView(ListView):
    """
    Vista para listar todas las partidas.
    
    Muestra un listado de todas las partidas registradas.
    """
    model = Game
    template_name = 'chess/game_list.html'
    context_object_name = 'games'
    paginate_by = 15


class GameDetailView(DetailView):
    """
    Vista para mostrar los detalles de una partida.
    
    Muestra información completa de una partida.
    """
    model = Game
    template_name = 'chess/game_detail.html'
    context_object_name = 'game'


class GameCreateView(CreateView):
    """
    Vista para registrar una nueva partida.
    
    Muestra un formulario para ingresar los datos de la partida.
    """
    model = Game
    form_class = GameForm
    template_name = 'chess/game_form.html'
    success_url = reverse_lazy('chess:game_list')


class GameUpdateView(UpdateView):
    """
    Vista para editar una partida existente.
    
    Muestra un formulario para modificar los datos de la partida.
    """
    model = Game
    form_class = GameForm
    template_name = 'chess/game_form.html'


class GameDeleteView(DeleteView):
    """
    Vista para eliminar una partida.
    
    Pide confirmación antes de eliminar la partida.
    """
    model = Game
    template_name = 'chess/game_confirm_delete.html'
    success_url = reverse_lazy('chess:game_list')


# ==================== VISTAS GENERALES ====================

def index(request):
    """
    Vista de inicio de la aplicación.
    
    Muestra estadísticas generales.
    """
    total_players = Player.objects.count()
    total_games = Game.objects.count()
    
    context = {
        'total_players': total_players,
        'total_games': total_games,
    }
    
    return render(request, 'chess/index.html', context)
