
# Microservicio de Login

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

- Ejecutar
```sh
python main.py
```

## Run with docker

- Create .env file
```sh
cp .env.example .env
```
Modify the generated .env file according your credentials

- Run
```sh
docker compose up -d --build
```

## Routes

#### 1. **/validate/admin [GET]**
   - **Descripción:** Endpoint para validar si el usuario actual es un administrador.
   - **Método:** `GET`
   - **Requisitos:**
       - El usuario debe estar autenticado mediante JWT.
   - **Parámetros:**
       - No requiere parámetros adicionales.
   - **Funcionalidad:**
       - Obtiene los datos del usuario actual a partir del token JWT.
       - Si el usuario es administrador, devuelve un mensaje exitoso junto con los datos del usuario.
       - Si el usuario no es administrador, devuelve un mensaje indicando la falta de permisos.
   - **Respuestas:**
       - `200 OK`: Si el usuario es administrador y se valida correctamente.
       - `401 Unauthorized`: Si el usuario no es administrador o no está autenticado.

#### 2. **/validate [GET]**
   - **Descripción:** Endpoint para validar y obtener los datos del usuario actual.
   - **Método:** `GET`
   - **Requisitos:**
       - El usuario debe estar autenticado mediante JWT.
   - **Parámetros:**
       - No requiere parámetros adicionales.
   - **Funcionalidad:**
       - Obtiene los datos del usuario actual a partir del token JWT.
       - Devuelve un mensaje exitoso junto con los datos del usuario.
   - **Respuesta:**
       - `200 OK`: Si el usuario se valida correctamente.

#### 3. **/user-data [GET]**
   - **Descripción:** Endpoint para obtener los datos de un usuario específico.
   - **Método:** `GET`
   - **Requisitos:**
       - El usuario debe estar autenticado mediante JWT.
   - **Parámetros:**
       - No requiere parámetros adicionales.
   - **Funcionalidad:**
       - Obtiene los datos del usuario actual a partir del token JWT.
       - Utiliza el servicio de usuario para obtener los datos de un usuario específico.
       - Devuelve los datos del usuario si se encuentra en el sistema.
   - **Respuestas:**
       - `200 OK`: Si se encuentran los datos del usuario.
       - `401 Unauthorized`: Si no se encuentran los datos del usuario.

#### 4. **/login [POST]**
   - **Descripción:** Endpoint para iniciar sesión y obtener un token de acceso.
   - **Método:** `POST`
   - **Requisitos:**
       - No requiere autenticación.
   - **Parámetros:**
       - Formato JSON en el cuerpo de la solicitud (`Content-Type: application/json`):
           - `username`: Nombre de usuario (cadena).
           - `password`: Contraseña (cadena).
   - **Funcionalidad:**
       - Recibe las credenciales de inicio de sesión (nombre de usuario y contraseña) como JSON.
       - Utiliza el servicio de inicio de sesión para autenticar al usuario.
       - Si las credenciales son válidas, se genera un token de acceso JWT.
   - **Respuestas:**
       - `200 OK`: Si las credenciales son válidas y se genera el token de acceso.
       - `401 Unauthorized`: Si las credenciales son incorrectas o no se encuentran en el sistema.

#### 5. **/logout [POST]**
   - **Descripción:** Endpoint para cerrar sesión y eliminar el token de acceso.
   - **Método:** `POST`
   - **Requisitos:**
       - El usuario debe estar autenticado mediante JWT.
   - **Parámetros:**
       - No requiere parámetros adicionales.
   - **Funcionalidad:**
       - Elimina el token de acceso almacenado en las cookies.
       - Proporciona una respuesta exitosa indicando que la sesión se ha cerrado correctamente.
   - **Respuesta:**
       - `200 OK`: Si la sesión se cierra correctamente.
