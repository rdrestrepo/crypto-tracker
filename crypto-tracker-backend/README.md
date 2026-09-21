# Crypto Tracker API (Backend)

Backend en FastAPI que consume la API pública de CoinGecko, con autenticación JWT
y watchlist persistida en base de datos por usuario.

## Instalación

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edita .env con tus valores (SECRET_KEY, DATABASE_URL)
```

## Migraciones (Alembic)

```bash
alembic init alembic
# Configura alembic.ini y alembic/env.py apuntando a app.db.base.Base y settings.DATABASE_URL
alembic revision --autogenerate -m "init"
alembic upgrade head
```

## Correr el servidor

```bash
uvicorn app.main:app --reload
```

Docs interactivas: http://localhost:8000/docs

## Endpoints principales

- `POST /api/v1/auth/register` — crear usuario
- `POST /api/v1/auth/login` — obtener token JWT (form-urlencoded: username, password)
- `GET  /api/v1/crypto/prices?ids=bitcoin,ethereum` — precios en vivo (público)
- `GET  /api/v1/crypto/search?q=doge` — buscar monedas (público)
- `GET  /api/v1/watchlist/` — listar watchlist del usuario (requiere token)
- `POST /api/v1/watchlist/` — agregar moneda a watchlist (requiere token)
- `DELETE /api/v1/watchlist/{item_id}` — quitar de watchlist (requiere token)
