"""
Configuración de la aplicación chess.
"""
from django.apps import AppConfig


class ChessConfig(AppConfig):
    """Configuración de la aplicación chess."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chess'
    verbose_name = 'Sistema de Registro de Partidas de Ajedrez'
