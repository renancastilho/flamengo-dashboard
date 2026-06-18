# 🔴⚫ Flamengo Dashboard — Plataforma Esportiva Full Stack

Dashboard de notícias e resultados do Flamengo em **todas as modalidades esportivas**, construído com a stack completa exigida pela vaga.

## Stack técnica

| Camada | Tecnologias |
|--------|-------------|
| **Backend** | Python 3.12, FastAPI, SQLAlchemy (async), Alembic, Pydantic v2 |
| **Banco de dados** | PostgreSQL 16, Redis (cache) |
| **Frontend** | React 18, TypeScript, Vite, React Query, Recharts, Tailwind CSS |
| **IA** | Anthropic API (Claude Sonnet) |
| **DevOps** | Docker, Docker Compose, Nginx |
| **CI/CD** | GitHub Actions |

## Esportes cobertos

- ⚽ Futebol (Brasileirão, Libertadores, Copa do Brasil)
- 🏀 Basquete (NBB, Champions League Americas)
- 🏊 Natação
- 🏐 Vôlei (Superliga)
- 🚣 Remo
- 🎮 eSports (CBLOL, Rainbow Six, VALORANT)
- ⚽ Futsal

## Iniciar o projeto

### Pré-requisitos
- Docker e Docker Compose instalados
- Git

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/flamengo-dashboard.git
cd flamengo-dashboard
```

### 2. Configurar variáveis de ambiente

```bash
cp .env.example .env
# Edite o .env com suas chaves de API
```

`.env`:
```env
ANTHROPIC_API_KEY=sk-ant-...
NEWS_API_KEY=sua_chave_newsapi
```

### 3. Subir com Docker Compose

```bash
docker compose up --build
```

| Serviço | URL |
|---------|-----|
| Dashboard | http://localhost |
| API docs (Swagger) | http://localhost/docs |
| API docs (ReDoc) | http://localhost/redoc |
| Backend direto | http://localhost:8000 |
| Frontend dev | http://localhost:5173 |

## Estrutura do projeto

```
flamengo-dashboard/
├── backend/
│   ├── app/
│   │   ├── api/v1/routes/     # Endpoints FastAPI
│   │   │   ├── auth.py        # JWT Authentication
│   │   │   ├── news.py        # CRUD de notícias
│   │   │   ├── matches.py     # Resultados e partidas
│   │   │   ├── sports.py      # Dados por modalidade
│   │   │   └── ai_chat.py     # IA com Anthropic
│   │   ├── models/            # SQLAlchemy models
│   │   ├── schemas/           # Pydantic schemas
│   │   └── core/              # Config, database
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── services/          # API calls
│   │   └── hooks/             # Custom hooks
│   ├── Dockerfile
│   └── package.json
├── nginx/
│   └── nginx.conf             # Reverse proxy
├── .github/workflows/
│   └── ci.yml                 # GitHub Actions CI/CD
└── docker-compose.yml
```

## API REST — Endpoints principais

```
GET    /api/v1/news                  Lista notícias (filtro por esporte)
POST   /api/v1/news                  Cria notícia
GET    /api/v1/matches               Lista resultados
GET    /api/v1/matches/upcoming      Próximos jogos
GET    /api/v1/sports                Dados de todas as modalidades
POST   /api/v1/ai/chat               Chat com IA sobre o Flamengo
GET    /api/v1/ai/summary/{sport}    Resumo IA de modalidade
POST   /api/v1/auth/register         Cadastro de usuário
POST   /api/v1/auth/login            Login (JWT)
GET    /health                       Health check
```

## Desenvolvimento local (sem Docker)

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Banco de dados — Migrations com Alembic

```bash
cd backend
alembic init alembic
alembic revision --autogenerate -m "initial"
alembic upgrade head
```

## Contribuindo

1. Fork o repositório
2. Crie uma branch: `git checkout -b feature/nova-funcionalidade`
3. Commit: `git commit -m 'feat: adiciona nova funcionalidade'`
4. Push: `git push origin feature/nova-funcionalidade`
5. Abra um Pull Request

---

**Mengão até morrer!** 🔴⚫
