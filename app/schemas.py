from pydantic import BaseModel, ConfigDict
from typing import Optional

class ExercicioBase(BaseModel):
    nome: str
    grupo_muscular: str
    descricao: str
    equipamento: str
    gif_url: str

class ExercicioCreate(ExercicioBase):
    pass

class Exercicio(ExercicioBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)

# Schemas para autenticação
class UsuarioBase(BaseModel):
    username: str
    email: str

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int
    is_admin: bool
    
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
