"""
Configuración de URLs para la aplicación chess.

Define las rutas de URL para todas las vistas de la aplicación.
"""
from django.urls import path
from . import views

app_name = 'chess'

urlpatterns = [
    # URL de inicio
    path('', views.index, name='index'),
    
    # URLs de Jugadores
    path('players/', views.PlayerListView.as_view(), name='player_list'),
    path('players/<int:pk>/', views.PlayerDetailView.as_view(), name='player_detail'),
    path('players/create/', views.PlayerCreateView.as_view(), name='player_create'),
    path('players/<int:pk>/edit/', views.PlayerUpdateView.as_view(), name='player_edit'),
    path('players/<int:pk>/delete/', views.PlayerDeleteView.as_view(), name='player_delete'),
    
    # URLs de Partidas
    path('games/', views.GameListView.as_view(), name='game_list'),
    path('games/<int:pk>/', views.GameDetailView.as_view(), name='game_detail'),
    path('games/create/', views.GameCreateView.as_view(), name='game_create'),
    path('games/<int:pk>/edit/', views.GameUpdateView.as_view(), name='game_edit'),
    path('games/<int:pk>/delete/', views.GameDeleteView.as_view(), name='game_delete'),
]
