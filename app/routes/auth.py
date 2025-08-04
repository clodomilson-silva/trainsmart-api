from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..auth import authenticate_user, create_access_token, get_db
from ..config import settings

router = APIRouter()

@router.post("/register", response_model=schemas.Usuario)
def register(user: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    """Registrar novo usuário (usuário comum)"""
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Username já registrado"
        )
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email já registrado"
        )
    return crud.create_user(db=db, user=user)

@router.post("/register-admin", response_model=schemas.Usuario)
def register_admin(user: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    """Registrar novo administrador - Desabilitado em produção"""
    if settings.is_production:
        raise HTTPException(
            status_code=403,
            detail="Registro de admin desabilitado em produção"
        )
    
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Username já registrado"
        )
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email já registrado"
        )
    return crud.create_user(db=db, user=user, is_admin=True)

@router.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Login e obtenção de token de acesso"""
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
