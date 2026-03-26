from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Usuario
from auth import verify_password, create_token, hash_password
from schemas import LoginRequest, RegisterRequest, TokenResponse

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):

    user = db.query(Usuario).filter(Usuario.email == data.email).first()

    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = create_token({"user_id": user.id})

    return {"access_token": token}

@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):

    existing = db.query(Usuario).filter(Usuario.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    print("Password recibido:", data.password)
    print("Longitud:", len(data.password))
    
    if len(data.password) < 6:
        raise HTTPException(status_code=400, detail="Contraseña muy corta")

    hashed_password = hash_password(data.password)

    nuevo_usuario = Usuario(
        nombre=data.nombre,
        email=data.email,
        password_hash=hashed_password
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return {"mensaje": "Usuario creado correctamente"}