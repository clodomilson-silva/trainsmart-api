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

# Popular banco de dados no startup (apenas em produção)
if settings.is_production:
    try:
        from .database import SessionLocal
        from .models import Exercicio, Usuario
        
        db = SessionLocal()
        
        # Verificar se precisa popular exercícios
        exercicios_count = db.query(Exercicio).count()
        logger.info(f"Exercícios no banco: {exercicios_count}")
        
        if exercicios_count == 0:
            logger.info("Banco vazio, populando exercícios...")
            import subprocess
            import sys
            result = subprocess.run([sys.executable, "scripts/popular_exercicios.py"], 
                                  capture_output=True, text=True)
            logger.info(f"População resultado: {result.stdout}")
            if result.stderr:
                logger.error(f"Erro na população: {result.stderr}")
        else:
            # Atualizar URLs dos GIFs se necessário
            logger.info("Atualizando URLs dos GIFs...")
            import subprocess
            import sys
            result = subprocess.run([sys.executable, "scripts/atualizar_gifs.py"], 
                                  capture_output=True, text=True)
            logger.info(f"Atualização GIFs resultado: {result.stdout}")
            if result.stderr:
                logger.error(f"Erro na atualização GIFs: {result.stderr}")
        
        # Verificar se precisa criar admin
        admin_count = db.query(Usuario).filter(Usuario.is_admin == True).count()
        logger.info(f"Admins no banco: {admin_count}")
        
        if admin_count == 0:
            logger.info("Nenhum admin encontrado, criando...")
            import subprocess
            import sys
            result = subprocess.run([sys.executable, "scripts/criar_admin.py"], 
                                  capture_output=True, text=True)
            logger.info(f"Admin criação resultado: {result.stdout}")
            if result.stderr:
                logger.error(f"Erro na criação admin: {result.stderr}")
        
        db.close()
        
    except Exception as e:
        logger.error(f"Erro no startup: {e}")

app = FastAPI(
    title="TrainSmart API",
    description="API para exercícios físicos com autenticação e autorização",
    version="1.0.0",
    docs_url=None,  # Desabilitado por segurança em produção
    redoc_url=None  # Desabilitado por segurança em produção
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
        "docs": "Disponível no GitHub README",
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
