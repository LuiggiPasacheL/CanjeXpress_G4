
# CanjeXpress Login

## Prerequisites
- Postgresql 14.9+
- Python 3.10.12+
- Pip 22.0.2+

## Run

- Install with pip
```sh
pip install -r requirements.txt
```
- Set envoriment variables as .env.example file
```sh
export DATABASE_HOST=localhost #e.g.
```

- Run
```sh
python main.py
```

## Run with docker

- Build
```sh
docker build -t canjexpress_login .
```

- Create .env file
```sh
cp .env.example .env
```
Modify the generated .env file according your credentials

- Run
```sh
docker run --env-file .env --network host canjexpress_login
```