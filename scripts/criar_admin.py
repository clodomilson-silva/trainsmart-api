import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import SessionLocal
from app.models import Usuario
from app.utils import get_password_hash
from app.database import Base, engine
from app.config import settings

# Cria as tabelas se não existirem
Base.metadata.create_all(bind=engine)

def criar_admin():
    db = SessionLocal()
    
    # Verifica se já existe um admin
    admin_existente = db.query(Usuario).filter(Usuario.is_admin == True).first()
    if admin_existente:
        print(f"✅ Administrador já existe: {admin_existente.username}")
        db.close()
        return
    
    # Dados do admin das configurações
    admin_data = {
        "username": settings.ADMIN_USERNAME,
        "email": settings.ADMIN_EMAIL,
        "password": settings.ADMIN_PASSWORD,
        "is_admin": True
    }
    
    # Cria o usuário admin
    hashed_password = get_password_hash(admin_data["password"])
    admin_user = Usuario(
        username=admin_data["username"],
        email=admin_data["email"],
        hashed_password=hashed_password,
        is_admin=admin_data["is_admin"]
    )
    
    db.add(admin_user)
    db.commit()
    db.refresh(admin_user)
    db.close()
    
    print("✅ Usuário administrador criado com sucesso!")
    print(f"Username: {admin_data['username']}")
    print(f"Email: {admin_data['email']}")
    print(f"Environment: {settings.ENVIRONMENT}")
    
    if settings.is_production:
        print("\n🔐 PRODUÇÃO: Certifique-se de que as variáveis de ambiente estão configuradas!")
    else:
        print(f"Password: {admin_data['password']}")
        print("\n🔐 IMPORTANTE: Altere a senha padrão em produção!")

if __name__ == "__main__":
    criar_admin()
