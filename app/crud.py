from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from . import models, schemas
from .utils import get_password_hash
from typing import Optional, List

# Funções para exercícios
def get_exercicios(db: Session, skip: int = 0, limit: int = 100, 
                  grupo_muscular: Optional[str] = None, 
                  equipamento: Optional[str] = None):
    query = db.query(models.Exercicio)
    
    if grupo_muscular:
        query = query.filter(models.Exercicio.grupo_muscular.ilike(f"%{grupo_muscular}%"))
    
    if equipamento:
        query = query.filter(models.Exercicio.equipamento.ilike(f"%{equipamento}%"))
    
    return query.offset(skip).limit(limit).all()

def get_exercicio(db: Session, exercicio_id: int):
    return db.query(models.Exercicio).filter(models.Exercicio.id == exercicio_id).first()

def create_exercicio(db: Session, exercicio: schemas.ExercicioCreate):
    db_exercicio = models.Exercicio(**exercicio.dict())
    db.add(db_exercicio)
    db.commit()
    db.refresh(db_exercicio)
    return db_exercicio

def update_exercicio(db: Session, exercicio_id: int, exercicio: schemas.ExercicioCreate):
    db_exercicio = get_exercicio(db, exercicio_id)
    if db_exercicio:
        for key, value in exercicio.dict().items():
            setattr(db_exercicio, key, value)
        db.commit()
        db.refresh(db_exercicio)
    return db_exercicio

def delete_exercicio(db: Session, exercicio_id: int):
    db_exercicio = get_exercicio(db, exercicio_id)
    if db_exercicio:
        db.delete(db_exercicio)
        db.commit()
    return db_exercicio

# Funções para usuários
def get_user_by_username(db: Session, username: str):
    return db.query(models.Usuario).filter(models.Usuario.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def create_user(db: Session, user: schemas.UsuarioCreate, is_admin: bool = False):
    hashed_password = get_password_hash(user.password)
    db_user = models.Usuario(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_admin=is_admin
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_grupos_musculares(db: Session):
    """Retorna lista de grupos musculares únicos"""
    result = db.query(models.Exercicio.grupo_muscular).distinct().all()
    return [grupo[0] for grupo in result]

def get_equipamentos(db: Session):
    """Retorna lista de equipamentos únicos"""
    result = db.query(models.Exercicio.equipamento).distinct().all()
    return [equip[0] for equip in result]
