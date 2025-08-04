from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from .. import crud, schemas, models
from ..auth import get_current_admin_user, get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.Exercicio])
def listar_exercicios(
    skip: int = Query(0, ge=0, description="Número de exercícios para pular"),
    limit: int = Query(100, ge=1, le=1000, description="Limite de exercícios por página"),
    grupo_muscular: Optional[str] = Query(None, description="Filtrar por grupo muscular"),
    equipamento: Optional[str] = Query(None, description="Filtrar por equipamento"),
    db: Session = Depends(get_db)
):
    """Listar exercícios - Acesso público (GET apenas)"""
    return crud.get_exercicios(
        db, 
        skip=skip, 
        limit=limit, 
        grupo_muscular=grupo_muscular, 
        equipamento=equipamento
    )

@router.get("/grupos-musculares", response_model=List[str])
def listar_grupos_musculares(db: Session = Depends(get_db)):
    """Listar todos os grupos musculares únicos - Acesso público"""
    return crud.get_grupos_musculares(db)

@router.get("/equipamentos", response_model=List[str])
def listar_equipamentos(db: Session = Depends(get_db)):
    """Listar todos os equipamentos únicos - Acesso público"""
    return crud.get_equipamentos(db)

@router.get("/{exercicio_id}", response_model=schemas.Exercicio)
def detalhe_exercicio(exercicio_id: int, db: Session = Depends(get_db)):
    """Obter detalhes de um exercício específico - Acesso público"""
    exercicio = crud.get_exercicio(db, exercicio_id)
    if not exercicio:
        raise HTTPException(status_code=404, detail="Exercício não encontrado")
    return exercicio

# Rotas protegidas - apenas para administradores
@router.post("/", response_model=schemas.Exercicio)
def criar_exercicio(
    exercicio: schemas.ExercicioCreate, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_admin_user)
):
    """Criar novo exercício - Apenas administradores"""
    return crud.create_exercicio(db, exercicio)

@router.put("/{exercicio_id}", response_model=schemas.Exercicio)
def atualizar_exercicio(
    exercicio_id: int,
    exercicio: schemas.ExercicioCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_admin_user)
):
    """Atualizar exercício existente - Apenas administradores"""
    db_exercicio = crud.update_exercicio(db, exercicio_id, exercicio)
    if not db_exercicio:
        raise HTTPException(status_code=404, detail="Exercício não encontrado")
    return db_exercicio

@router.delete("/{exercicio_id}", response_model=schemas.Exercicio)
def deletar_exercicio(
    exercicio_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_admin_user)
):
    """Deletar exercício - Apenas administradores"""
    db_exercicio = crud.delete_exercicio(db, exercicio_id)
    if not db_exercicio:
        raise HTTPException(status_code=404, detail="Exercício não encontrado")
    return db_exercicio
