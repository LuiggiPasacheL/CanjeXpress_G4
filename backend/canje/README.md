
# Microservicio de Canje

## Prerequisitos
- Postgresql 14.9+
- Python 3.10.12+
- Pip 22.0.2+

## Ejecutar

- Instalar librerías.
```sh
pip install -r requirements.txt
```
- Establecer las variables de entorno como están en el archivo `.env.example`.
```sh
export DATABASE_HOST=localhost #e.g.
```

- Añadir json de credenciales de firebase en la raíz de esta carpeta.

- Ejecutar
```sh
python main.py
```

## Run with docker

- Crear archivo .env
```sh
cp .env.example .env
```
Modifica el archivo `.env` generado de acuerdo a tus credenciales

- Run
```sh
docker compose run -d --build
```

## Routes

#### 1. **/ [GET]**
   - **Descripción:** Punto de entrada del servicio.
   - **Método:** `GET`
   - **Funcionalidad:**
       - Devuelve un mensaje de 'Hello World!' como respuesta.
   - **Respuesta:**
       - Mensaje de 'Hello World!' como texto plano.

#### 2. **/canjear [POST]**
   - **Descripción:** Endpoint para realizar el proceso de canje de productos.
   - **Método:** `POST`
   - **Requisitos:**
       - El usuario debe estar autenticado mediante JWT.
   - **Parámetros:**
       - Formato JSON en el cuerpo de la solicitud (`Content-Type: application/json`):
           - `cart`: Array de objetos de productos (id, cantidad requerida) para comprar.
   - **Funcionalidad:**
       - Verifica si el usuario está autenticado al obtener datos del usuario a través de una solicitud HTTP al servicio de autenticación (`http://login:3000/user-data`).
       - Si la solicitud al servicio de autenticación no devuelve un status code 200, se devuelve un mensaje indicando el problema.
       - Si no existe información de usuario en la respuesta, se devuelve un mensaje indicando que los datos no existen.
       - Si se obtiene información del usuario, se crea un objeto `User` con el ID y puntos del usuario activo.
       - Ejecuta el caso de uso `canjear` con el usuario y el carrito de productos.
   - **Respuestas:**
       - `200 OK`: Si el canje se realiza correctamente.
       - `400 Bad Request`: Si ocurre un error durante el canje.
       - `401 Unauthorized`: Si el token es inválido o no se puede obtener información del usuario.
