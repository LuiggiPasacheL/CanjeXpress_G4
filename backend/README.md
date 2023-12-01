
# Enviroments

## Production
```sh
sudo docker compose -f docker-compose.production.yaml up -d --build
```

## Local
```sh
sudo docker compose up -d --build
```

# Endpoints

## **1. Login**
- A las rutas descritas en el microservicio [login](https://github.com/LuiggiPasacheL/CanjeXpress_G4/tree/master/backend/login) agregar el prefijo `/login`

## **2. Canje**
- A las rutas descritas en el microservicio [canje](https://github.com/LuiggiPasacheL/CanjeXpress_G4/tree/master/backend/canje) agregar el prefijo `/canje`
