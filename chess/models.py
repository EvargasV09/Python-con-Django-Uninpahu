"""
Modelos para la aplicación chess.

Define los modelos Player y Game para registrar partidas de ajedrez.
"""
from django.db import models
from django.urls import reverse


class Player(models.Model):
    """
    Modelo para representar un jugador de ajedrez.
    
    Atributos:
        first_name: Nombre del jugador
        last_name: Apellido del jugador
        ranking: Ranking ELO del jugador
        registered_at: Fecha de registro del jugador
    """
    first_name = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Apellido'
    )
    ranking = models.IntegerField(
        default=1000,
        verbose_name='Ranking ELO'
    )
    registered_at = models.DateField(
        auto_now_add=True,
        verbose_name='Fecha de Registro'
    )

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        ordering = ['-ranking', 'last_name', 'first_name']

    def __str__(self):
        """Retorna la representación en string del jugador."""
        return f'{self.first_name} {self.last_name} ({self.ranking})'

    def get_absolute_url(self):
        """Retorna la URL del detalle del jugador."""
        return reverse('chess:player_detail', kwargs={'pk': self.pk})


class Game(models.Model):
    """
    Modelo para representar una partida de ajedrez.
    
    Atributos:
        white_player: Jugador que juega con las piezas blancas
        black_player: Jugador que juega con las piezas negras
        result: Resultado de la partida
        played_at: Fecha de la partida
        opening: Apertura jugada
        notes: Notas sobre la partida
    """
    
    RESULT_CHOICES = [
        ('white_wins', 'Las Blancas Ganan'),
        ('black_wins', 'Las Negras Ganan'),
        ('draw', 'Empate'),
    ]

    white_player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='games_as_white',
        verbose_name='Jugador Blancas'
    )
    black_player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='games_as_black',
        verbose_name='Jugador Negras'
    )
    result = models.CharField(
        max_length=20,
        choices=RESULT_CHOICES,
        default='draw',
        verbose_name='Resultado'
    )
    played_at = models.DateField(
        verbose_name='Fecha de la Partida'
    )
    opening = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Apertura'
    )
    notes = models.TextField(
        blank=True,
        verbose_name='Notas'
    )

    class Meta:
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'
        ordering = ['-played_at']

    def __str__(self):
        """Retorna la representación en string de la partida."""
        result_display = self.get_result_display()
        return f'{self.white_player} vs {self.black_player} - {result_display}'

    def get_absolute_url(self):
        """Retorna la URL del detalle de la partida."""
        return reverse('chess:game_detail', kwargs={'pk': self.pk})
