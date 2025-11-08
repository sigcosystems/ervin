from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.database import get_db

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Login de usuario"""
    # TODO: Implementar lógica de autenticación
    return {"access_token": "token-temporal", "token_type": "bearer"}

@router.post("/register")
async def register(db: Session = Depends(get_db)):
    """Registro de nuevo usuario"""
    # TODO: Implementar lógica de registro
    return {"message": "Usuario registrado exitosamente"}

@router.get("/me")
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Obtener usuario actual"""
    # TODO: Implementar lógica de obtener usuario
    return {"user": "current_user"}