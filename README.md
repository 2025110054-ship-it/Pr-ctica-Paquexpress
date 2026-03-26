# Paquexpress - Aplicación de Entregas

## Descripción

Aplicación móvil desarrollada en Flutter para la gestión de entregas de paquetes, conectada a un backend en FastAPI. Permite a los agentes autenticarse, visualizar paquetes asignados y registrar entregas mediante evidencia fotográfica y geolocalización.

## Tecnologías utilizadas

### Frontend
- Flutter
- http
- image_picker
- geolocator
- shared_preferences

### Backend
- FastAPI
- Uvicorn
- SQLAlchemy
- Passlib (bcrypt)
- JWT

### Base de datos
- MySQL (gestionado con phpMyAdmin)

## Instalación del Backend

1. Clonar el repositorio o ubicar el proyecto backend.

2. Instalar dependencias:

    pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose
    pip install bcrypt==3.2.2

3. Configurar la base de datos en el archivo de conexión.

4. Ejecutar el servidor:

    uvicorn main:app --reload

5. Acceder a la documentación:

    http://127.0.0.1:8000/docs

## Instalación del Frontend (Flutter)

1. Ubicar el proyecto Flutter.

2. Instalar dependencias:

    flutter pub get

3. Configurar la URL del backend en constants.dart:

    http://127.0.0.1:8000 o http://localhost:8000

4. Ejecutar la aplicación:

    flutter run

## Uso de la aplicación

1. Iniciar sesión con un usuario previamente registrado en la base de datos.
2. Visualizar la lista de paquetes asignados.
3. Seleccionar un paquete.
4. Capturar evidencia (imagen) y obtener ubicación.
5. Confirmar entrega.
6. El sistema registra la entrega y actualiza el estado del paquete.

## Endpoints principales

- POST /login  
- GET /paquetes  
- POST /entrega  

## Notas importantes

- Las contraseñas deben almacenarse con hash bcrypt.
- No se permite registrar una entrega más de una vez por paquete.
- La aplicación requiere permisos de cámara y ubicación.
- El backend valida autenticación mediante JWT.
- El backend permite registrar un usuario para poder realizar la práctica.