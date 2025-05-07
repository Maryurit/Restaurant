🍽️ API de Gestión de Restaurantes
Una API RESTful construida con Django y Django REST Framework para gestionar restaurantes, platos, menús, reservas, reseñas y calificaciones.

🚀 Funcionalidades
✅ CRUD completo para Restaurantes, Platos y Menús

📅 Gestión de Reservas

🔍 Filtro de restaurantes por ubicación y categoría

⭐ Gestión de Reseñas y Calificaciones de platos

🔐 Autenticación básica de usuarios

🛠️ Tecnologías
Python 3.13

Django 5.2

Django REST Framework

Django Filter

SQLite (por defecto)

Bootstrap (para admin opcional)

🗂️ Estructura del proyecto
Copiar
Editar
Restaurante/
├── manage.py
├── Restaurante/
│   └── settings.py
├── restaurantes/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py

📦 Instalación
Clona el repositorio:
git clone https://github.com/tuusuario/Restaurant.git && cd Restaurant

Crea y activa un entorno virtual:

Windows: python -m venv venv && venv\Scripts\activate

macOS/Linux: python3 -m venv venv && source venv/bin/activate

Instala las dependencias:
pip install -r requirements.txt

Aplica las migraciones:
python manage.py migrate

Crea un superusuario:
python manage.py createsuperuser

Ejecuta el servidor:
python manage.py runserver

🔗 Endpoints principales
Recurso	Endpoint	Métodos
Restaurantes	/api/restaurantes/	GET, POST
Restaurantes (ID)	/api/restaurantes/<id>/	GET, PUT, DELETE
Platos	/api/platos/	GET, POST
Platos (ID)	/api/platos/<id>/	GET, PUT, DELETE
Menús	/api/menus/	GET, POST
Reservas	/api/reservas/	GET, POST
Reseñas de plato	/api/platos/<id>/resenas/	GET, POS
