"""
Configuración de Django Admin para la aplicación chess.

Registra los modelos en el admin y personaliza su visualización.
"""
from django.contrib import admin
from .models import Player, Game


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    """
    Administrador personalizado para el modelo Player.
    
    Personaliza la lista de visualización y la búsqueda.
    """
    list_display = ['get_full_name', 'ranking', 'registered_at']
    list_filter = ['registered_at', 'ranking']
    search_fields = ['first_name', 'last_name']
    ordering = ['-ranking']
    
    def get_full_name(self, obj):
        """Retorna el nombre completo del jugador."""
        return f'{obj.first_name} {obj.last_name}'
    
    get_full_name.short_description = 'Jugador'


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """
    Administrador personalizado para el modelo Game.
    
    Personaliza la lista de visualización y la búsqueda.
    """
    list_display = ['get_game_display', 'result', 'played_at', 'opening']
    list_filter = ['result', 'played_at', 'opening']
    search_fields = [
        'white_player__first_name', 'white_player__last_name',
        'black_player__first_name', 'black_player__last_name',
        'opening'
    ]
    date_hierarchy = 'played_at'
    ordering = ['-played_at']
    
    def get_game_display(self, obj):
        """Retorna una representación legible de la partida."""
        return f'{obj.white_player} vs {obj.black_player}'
    
    get_game_display.short_description = 'Partida'
