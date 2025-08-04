from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routes import exercicios, auth
from .config import settings
import logging

# Configurar logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TrainSmart API",
    description="API para exercícios físicos com autenticação e autorização",
    version="1.0.0",
    docs_url="/docs",  # Habilita docs sempre
    redoc_url="/redoc"  # Habilita redoc sempre
)

# Configuração CORS para produção
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Middleware de segurança
@app.middleware("http")
async def security_headers(request, call_next):
    response = await call_next(request)
    
    # Headers de segurança
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    
    # HSTS apenas em produção com HTTPS
    if settings.is_production:
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    
    return response

# Rotas de autenticação
app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])

# Rotas de exercícios
app.include_router(exercicios.router, prefix="/exercicios", tags=["Exercícios"])

@app.get("/")
def root():
    return {
        "message": "TrainSmart API - API para exercícios físicos",
        "version": "1.0.0",
        "environment": settings.ENVIRONMENT,
        "docs": "/docs" if not settings.is_production else "Disabled in production",
        "endpoints": {
            "exercicios": "/exercicios",
            "autenticacao": "/auth",
            "grupos_musculares": "/exercicios/grupos-musculares",
            "equipamentos": "/exercicios/equipamentos"
        }
    }

@app.get("/health")
def health_check():
    """Health check endpoint para monitoramento"""
    return {"status": "healthy", "environment": settings.ENVIRONMENT}
