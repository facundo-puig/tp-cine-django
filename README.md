# 🎬 CineApp

Sistema de gestión de cine desarrollado con Django. Permite ver la cartelera, seleccionar funciones, elegir asientos, agregar candy y confirmar reservas.

## Capturas

### Home — Cartelera
![Home](screenshots/sc_home.png)

### Detalle de película
![Detalle](screenshots/sc_detalle_pelicula.png)

### Selección de asientos
![Asientos](screenshots/sc_asientos.png)

### Selección de candy
![Candy](screenshots/sc_candy.png)

### Confirmación de reserva
![Confirmacion](screenshots/sc_confirmacion_reserva.png)

### Mis Reservas
![Reservas](screenshots/sc_mis_reservas.png)

### Promociones
![Promociones](screenshots/sc_promociones.png)

## Tecnologías
- Python 3.12
- Django 5.x
- Tailwind CSS (CDN)
- JavaScript
- SQLite

## Apps
- `peliculas` — cartelera y detalle de películas
- `funciones` — funciones por película (fecha, hora, formato, precio)
- `salas` — salas y asientos
- `reservas` — flujo de compra de entradas
- `promociones` — promociones con descuentos
- `candy` — productos del candy bar
- `usuarios` — registro, login y logout

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/facundo-puig/tp-cine-django.git
cd tp_cine

# Crear entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Migrar base de datos
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Correr el servidor
python manage.py runserver
```

## Credenciales de prueba
- **Admin:** usuario: `admin` / contraseña: `admin`
- **Empleado:** usuario: `empleado` / contraseña: `clave123`

## Integrantes
- Facundo Puig
- Gonzalo Riva