"""
Tests para la aplicación chess.

Sigue el estilo del tutorial oficial de Django.
Incluye tests para modelos y vistas.
"""
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Player, Game


class PlayerModelTests(TestCase):
    """Tests para el modelo Player."""

    def test_player_creation(self):
        """Test que se puede crear un jugador."""
        player = Player.objects.create(
            first_name='Garry',
            last_name='Kasparov',
            ranking=2800
        )
        self.assertEqual(str(player), 'Garry Kasparov (2800)')
        self.assertEqual(player.first_name, 'Garry')
        self.assertEqual(player.last_name, 'Kasparov')
        self.assertEqual(player.ranking, 2800)

    def test_player_default_ranking(self):
        """Test que el ranking por defecto es 1000."""
        player = Player.objects.create(
            first_name='Juan',
            last_name='Pérez'
        )
        self.assertEqual(player.ranking, 1000)

    def test_player_ordering(self):
        """Test que los jugadores se ordenan por ranking."""
        player1 = Player.objects.create(
            first_name='Jugador',
            last_name='Fuerte',
            ranking=2000
        )
        player2 = Player.objects.create(
            first_name='Jugador',
            last_name='Débil',
            ranking=1000
        )
        players = Player.objects.all()
        self.assertEqual(players[0].ranking, 2000)
        self.assertEqual(players[1].ranking, 1000)


class GameModelTests(TestCase):
    """Tests para el modelo Game."""

    def setUp(self):
        """Crea jugadores para los tests."""
        self.player1 = Player.objects.create(
            first_name='Fischer',
            last_name='Bobby',
            ranking=2700
        )
        self.player2 = Player.objects.create(
            first_name='Spassky',
            last_name='Boris',
            ranking=2680
        )

    def test_game_creation(self):
        """Test que se puede crear una partida."""
        today = timezone.now().date()
        game = Game.objects.create(
            white_player=self.player1,
            black_player=self.player2,
            result='white_wins',
            played_at=today,
            opening='Ruy López'
        )
        self.assertEqual(game.white_player, self.player1)
        self.assertEqual(game.black_player, self.player2)
        self.assertEqual(game.result, 'white_wins')
        self.assertEqual(game.opening, 'Ruy López')

    def test_game_default_result(self):
        """Test que el resultado por defecto es empate."""
        today = timezone.now().date()
        game = Game.objects.create(
            white_player=self.player1,
            black_player=self.player2,
            played_at=today
        )
        self.assertEqual(game.result, 'draw')

    def test_game_string_representation(self):
        """Test la representación en string de la partida."""
        today = timezone.now().date()
        game = Game.objects.create(
            white_player=self.player1,
            black_player=self.player2,
            result='white_wins',
            played_at=today
        )
        expected = 'Fischer Bobby (2700) vs Spassky Boris (2680) - Las Blancas Ganan'
        self.assertEqual(str(game), expected)

    def test_game_related_names(self):
        """Test que los nombres relacionados funcionan correctamente."""
        today = timezone.now().date()
        game1 = Game.objects.create(
            white_player=self.player1,
            black_player=self.player2,
            result='white_wins',
            played_at=today
        )
        game2 = Game.objects.create(
            white_player=self.player2,
            black_player=self.player1,
            result='black_wins',
            played_at=today
        )
        
        # Player1 jugó 2 partidas como blancas
        self.assertEqual(self.player1.games_as_white.count(), 1)
        # Player1 jugó 1 partida como negras
        self.assertEqual(self.player1.games_as_black.count(), 1)


class PlayerViewTests(TestCase):
    """Tests para las vistas de jugador."""

    def setUp(self):
        """Crea datos de prueba."""
        self.player = Player.objects.create(
            first_name='Anatoly',
            last_name='Karpov',
            ranking=2750
        )

    def test_player_list_view_status(self):
        """Test que la vista de lista de jugadores retorna 200."""
        response = self.client.get(reverse('chess:player_list'))
        self.assertEqual(response.status_code, 200)

    def test_player_list_view_template(self):
        """Test que se usa el template correcto."""
        response = self.client.get(reverse('chess:player_list'))
        self.assertTemplateUsed(response, 'chess/player_list.html')

    def test_player_detail_view_status(self):
        """Test que la vista de detalle de jugador retorna 200."""
        response = self.client.get(
            reverse('chess:player_detail', kwargs={'pk': self.player.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_player_detail_view_template(self):
        """Test que se usa el template correcto."""
        response = self.client.get(
            reverse('chess:player_detail', kwargs={'pk': self.player.pk})
        )
        self.assertTemplateUsed(response, 'chess/player_detail.html')

    def test_player_create_view_status(self):
        """Test que la vista de crear jugador retorna 200."""
        response = self.client.get(reverse('chess:player_create'))
        self.assertEqual(response.status_code, 200)

    def test_player_create_view_post(self):
        """Test que se puede crear un jugador mediante POST."""
        response = self.client.post(reverse('chess:player_create'), {
            'first_name': 'Miguel',
            'last_name': 'Najdorf',
            'ranking': 2650
        })
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertTrue(
            Player.objects.filter(first_name='Miguel').exists()
        )


class GameViewTests(TestCase):
    """Tests para las vistas de partida."""

    def setUp(self):
        """Crea datos de prueba."""
        self.player1 = Player.objects.create(
            first_name='José Raúl',
            last_name='Capablanca',
            ranking=2800
        )
        self.player2 = Player.objects.create(
            first_name='Alexander',
            last_name='Alekhine',
            ranking=2750
        )
        today = timezone.now().date()
        self.game = Game.objects.create(
            white_player=self.player1,
            black_player=self.player2,
            result='white_wins',
            played_at=today,
            opening='Gambito de Dama'
        )

    def test_game_list_view_status(self):
        """Test que la vista de lista de partidas retorna 200."""
        response = self.client.get(reverse('chess:game_list'))
        self.assertEqual(response.status_code, 200)

    def test_game_list_view_template(self):
        """Test que se usa el template correcto."""
        response = self.client.get(reverse('chess:game_list'))
        self.assertTemplateUsed(response, 'chess/game_list.html')

    def test_game_detail_view_status(self):
        """Test que la vista de detalle de partida retorna 200."""
        response = self.client.get(
            reverse('chess:game_detail', kwargs={'pk': self.game.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_game_detail_view_template(self):
        """Test que se usa el template correcto."""
        response = self.client.get(
            reverse('chess:game_detail', kwargs={'pk': self.game.pk})
        )
        self.assertTemplateUsed(response, 'chess/game_detail.html')

    def test_game_create_view_status(self):
        """Test que la vista de crear partida retorna 200."""
        response = self.client.get(reverse('chess:game_create'))
        self.assertEqual(response.status_code, 200)

    def test_game_create_view_post(self):
        """Test que se puede crear una partida mediante POST."""
        today = timezone.now().date()
        response = self.client.post(reverse('chess:game_create'), {
            'white_player': self.player1.pk,
            'black_player': self.player2.pk,
            'result': 'draw',
            'played_at': today,
            'opening': 'Apertura Abierta',
            'notes': 'Partida bien jugada'
        })
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertEqual(Game.objects.filter(opening='Apertura Abierta').count(), 1)


class IndexViewTests(TestCase):
    """Tests para la vista de inicio."""

    def test_index_view_status(self):
        """Test que la vista de inicio retorna 200."""
        response = self.client.get(reverse('chess:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template(self):
        """Test que se usa el template correcto."""
        response = self.client.get(reverse('chess:index'))
        self.assertTemplateUsed(response, 'chess/index.html')

    def test_index_view_context(self):
        """Test que el contexto tiene los datos correctos."""
        Player.objects.create(first_name='Test', last_name='Player')
        response = self.client.get(reverse('chess:index'))
        self.assertEqual(response.context['total_players'], 1)
        self.assertEqual(response.context['total_games'], 0)
