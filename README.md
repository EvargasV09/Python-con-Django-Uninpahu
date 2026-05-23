# ChessCake - Sistema de Registro de Partidas de Ajedrez

ChessCake es una aplicación web Django para registrar y gestionar partidas de ajedrez entre jugadores. Permite mantener un registro de jugadores con su ranking ELO y todas las partidas que han jugado.

## Características

- **Gestión de Jugadores**: Crear, editar, ver y eliminar jugadores con su ranking ELO
- **Registro de Partidas**: Registrar partidas indicando jugadores, resultado, apertura y notas
- **Listados**: Visualizar listados de jugadores y partidas con paginación
- **Detalle de Jugadores**: Ver todas las partidas de un jugador específico
- **Admin Django**: Interfaz administrativa completa para ambos modelos
- **Interfaz Responsive**: Diseñado con Bootstrap 5 y CDN

## Requisitos

- Python 3.8+
- Django 5.0
- SQLite (incluido con Python)

## Instalación

### 1. Clonar o descargar el proyecto

```bash
cd ChessCake
```

### 2. Crear un entorno virtual (recomendado)

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear un superusuario (para acceder al admin)

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000/`

## Estructura del Proyecto

```
ChessCake/
├── ChessCake/           # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── chess/               # Aplicación principal
│   ├── models.py        # Modelos (Player, Game)
│   ├── views.py         # Vistas genéricas
│   ├── urls.py          # URLs de la app
│   ├── forms.py         # Formularios
│   ├── admin.py         # Configuración de admin
│   ├── tests.py         # Tests
│   ├── migrations/      # Migraciones de base de datos
│   └── templates/chess/ # Templates de la app
├── templates/           # Plantillas base
├── manage.py            # Utilidad de gestión de Django
├── requirements.txt     # Dependencias del proyecto
├── .gitignore           # Archivo para git
└── README.md           # Este archivo
```

## Modelos

### Player (Jugador)

- `first_name`: Nombre del jugador (CharField)
- `last_name`: Apellido del jugador (CharField)
- `ranking`: Ranking ELO del jugador (IntegerField, default: 1000)
- `registered_at`: Fecha de registro (DateField, auto)

### Game (Partida)

- `white_player`: Jugador con piezas blancas (ForeignKey a Player)
- `black_player`: Jugador con piezas negras (ForeignKey a Player)
- `result`: Resultado (choices: blancas ganan, negras ganan, empate)
- `played_at`: Fecha de la partida (DateField)
- `opening`: Apertura jugada (CharField, opcional)
- `notes`: Notas sobre la partida (TextField, opcional)

## Vistas Disponibles

### Jugadores
- `GET /players/` - Lista de todos los jugadores
- `GET /players/<id>/` - Detalle del jugador
- `GET /players/create/` - Formulario para crear jugador
- `POST /players/create/` - Procesar nuevo jugador
- `GET /players/<id>/edit/` - Formulario para editar jugador
- `POST /players/<id>/edit/` - Procesar edición de jugador
- `GET /players/<id>/delete/` - Confirmar eliminación
- `POST /players/<id>/delete/` - Procesar eliminación

### Partidas
- `GET /games/` - Lista de todas las partidas
- `GET /games/<id>/` - Detalle de la partida
- `GET /games/create/` - Formulario para registrar partida
- `POST /games/create/` - Procesar nueva partida
- `GET /games/<id>/edit/` - Formulario para editar partida
- `POST /games/<id>/edit/` - Procesar edición de partida
- `GET /games/<id>/delete/` - Confirmar eliminación
- `POST /games/<id>/delete/` - Procesar eliminación

## Tests

Para ejecutar los tests:

```bash
python manage.py test chess
```

Los tests incluyen:
- Tests de creación de modelos
- Tests de campos por defecto
- Tests de relaciones entre modelos
- Tests de vistas (status code 200)
- Tests de templates
- Tests de creación mediante POST

## Admin Django

Accede al panel de administración en:
```
http://127.0.0.1:8000/admin/
```

Con las credenciales del superusuario que creaste.

Características del admin:
- Búsqueda por nombre de jugador
- Filtrado por fecha y ranking
- Búsqueda de partidas por jugador
- Jerarquía de fechas para partidas

## Configuración de Idioma

La aplicación está configurada para usar español:
- Interfaz en español
- Formatos de fecha en español
- Zona horaria: America/Mexico_City

Para cambiar, edita `ChessCake/settings.py`:

```python
LANGUAGE_CODE = 'es'  # Cambiar idioma
TIME_ZONE = 'UTC'     # Cambiar zona horaria
```

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Notas de Desarrollo

- La aplicación utiliza SQLite como base de datos por defecto
- Las contraseñas se hashean automáticamente (aunque no se usan en esta versión simple)
- Los timestamps se crean automáticamente al registrar jugadores
- Las relaciones entre modelos usan CASCADE para eliminación

## Contacto

Para preguntas o sugerencias, contacta al equipo de desarrollo.

---

**Versión:** 1.0  
**Última actualización:** Marzo 2024

# Python-con-Django-Uninpahu