from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db

router = APIRouter()

@router.get("/")
async def listar_tecnicos(db: Session = Depends(get_db)):
    """Listar todos los técnicos"""
    # TODO: Implementar lógica
    return {"tecnicos": []}

@router.get("/{tecnico_id}")
async def obtener_tecnico(tecnico_id: int, db: Session = Depends(get_db)):
    """Obtener técnico por ID"""
    # TODO: Implementar lógica
    return {"tecnico_id": tecnico_id}

@router.post("/")
async def crear_tecnico(db: Session = Depends(get_db)):
    """Registrar nuevo técnico"""
    # TODO: Implementar lógica
    return {"message": "Técnico registrado"}

@router.put("/{tecnico_id}/disponibilidad")
async def actualizar_disponibilidad(tecnico_id: int, db: Session = Depends(get_db)):
    """Actualizar disponibilidad del técnico"""
    # TODO: Implementar lógica
    return {"message": "Disponibilidad actualizada"}

@router.get("/{tecnico_id}/servicios")
async def servicios_tecnico(tecnico_id: int, db: Session = Depends(get_db)):
    """Obtener servicios de un técnico"""
    # TODO: Implementar lógica
    return {"servicios": []}