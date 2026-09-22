# 📊 Crypto Tracker

Aplicación full-stack de seguimiento de criptomonedas en tiempo real, con autenticación de usuarios y watchlist personalizada. La construí como proyecto de portfolio para mostrar mi stack completo: Python con FastAPI en el backend y Angular con TypeScript en el frontend.

![Status](https://img.shields.io/badge/status-en%20desarrollo-yellow)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)
![Angular](https://img.shields.io/badge/Angular-18-DD0031?logo=angular&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 🚀 Demo en vivo

👉 **[crypto-tracker-omega-wine.vercel.app](https://crypto-tracker-omega-wine.vercel.app)**

El backend corre en el plan gratuito de Render, así que si nadie lo ha usado en un rato se "duerme" — la primera carga puede tardar unos 30-40 segundos mientras el servidor despierta. Después de eso todo funciona con normalidad.

---

## ✨ Funcionalidades

- 🔐 **Autenticación JWT** — registro e inicio de sesión seguros, con contraseñas hasheadas (bcrypt)
- 📈 **Precios en tiempo real** — consumo de la API pública de [CoinGecko](https://www.coingecko.com/en/api), con actualización automática cada 30s
- ⭐ **Watchlist personalizada** — cada usuario guarda y gestiona su propia lista de monedas favoritas, persistida en base de datos
- 🛡️ **Rutas protegidas** — guards e interceptors HTTP en Angular que inyectan el token automáticamente y bloquean el acceso sin sesión
- 🎨 **UI standalone en Angular 18** — componentes standalone, signals, control flow moderno (`@if`, `@for`)

---

## 🛠️ Stack técnico

| Capa            | Tecnología                                                        |
|-----------------|---------------------------------------------------------------------|
| **Backend**     | Python · FastAPI · SQLAlchemy · Alembic · Pydantic v2 · JWT (python-jose) · bcrypt |
| **Base de datos**| PostgreSQL en producción (Render) — SQLite para desarrollo local   |
| **Frontend**    | Angular 18 (standalone components) · TypeScript · RxJS · SCSS       |
| **Despliegue**  | Vercel (frontend) · Render (backend + PostgreSQL)                   |
| **API externa** | [CoinGecko API](https://www.coingecko.com/en/api) (pública, sin API key) |

---

## 📁 Estructura del repositorio

```
crypto-tracker/
├── crypto-tracker-backend/     # API REST en FastAPI
│   ├── app/
│   │   ├── api/                # Rutas y endpoints (auth, crypto, watchlist)
│   │   ├── core/                # Configuración y seguridad (JWT, hashing)
│   │   ├── crud/                # Operaciones de base de datos
│   │   ├── db/                  # Conexión y modelos base de SQLAlchemy
│   │   ├── models/              # Modelos ORM
│   │   ├── schemas/             # Esquemas Pydantic (validación/serialización)
│   │   └── services/            # Cliente de la API de CoinGecko
│   └── requirements.txt
│
└── crypto-tracker-frontend/    # SPA en Angular
    └── src/app/
        ├── core/                 # Servicios, guards e interceptors
        ├── features/             # Componentes por funcionalidad (auth, dashboard, watchlist)
        └── shared/                # Modelos TypeScript compartidos
```

---

## ⚙️ Instalación y ejecución local

### Requisitos previos
- Python 3.11 o 3.12
- Node.js 18+ y npm
- Git

### Backend

```bash
cd crypto-tracker-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -c "from app.db.base_all import Base; from app.db.session import engine; Base.metadata.create_all(bind=engine)"
uvicorn app.main:app --reload
```

API disponible en `http://localhost:8000` — documentación interactiva (Swagger) en `http://localhost:8000/docs`.

### Frontend

```bash
cd crypto-tracker-frontend
npm install
ng serve
```

App disponible en `http://localhost:4200`.

---

## 📡 Endpoints principales de la API

| Método | Endpoint                          | Descripción                          | Auth |
|--------|------------------------------------|---------------------------------------|------|
| POST   | `/api/v1/auth/register`            | Crear un nuevo usuario                | No   |
| POST   | `/api/v1/auth/login`               | Iniciar sesión (devuelve JWT)         | No   |
| GET    | `/api/v1/crypto/prices?ids=...`    | Precios en vivo de monedas            | No   |
| GET    | `/api/v1/crypto/search?q=...`      | Buscar monedas por nombre             | No   |
| GET    | `/api/v1/watchlist/`               | Listar watchlist del usuario          | Sí   |
| POST   | `/api/v1/watchlist/`               | Agregar moneda a la watchlist         | Sí   |
| DELETE | `/api/v1/watchlist/{item_id}`      | Quitar moneda de la watchlist         | Sí   |

---

## 🗺️ Roadmap

- [ ] Migraciones versionadas con Alembic
- [ ] Alertas de precio por email/push
- [ ] Tests automatizados (pytest + Jasmine/Karma)

---

## 👤 Autor

**Robinson Restrepo**
[GitHub](https://github.com/rdrestrepo)

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT — libre para usar como referencia o base de aprendizaje.
