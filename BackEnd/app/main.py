from typing import Annotated

from starlette.responses import RedirectResponse
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import crud
from .conexion import SessionLocal, engine
from .schemas import Datos_Usuarios, Buscar_Usuario, Login, LoginResponse
from .models import Base
from passlib.context import CryptContext

from jose import JWTError, jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
SECRET_KEY = "663020057e3698f9f5152633db69f3e5284ca38ef799372ab0a73dea90ce160f"
TOKEN_SECONDS_EXPIRE = 3600

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:5173",  # El origen de tu aplicación React
    "http://localhost",       # Puedes agregar más orígenes si es necesario
    "http://127.0.0.1"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir orígenes especificados
    allow_credentials=True,
    allow_methods=["*"],    # Permitir todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],    # Permitir todos los encabezados
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def create_token(data: list): 
    data_token = data.copy()
    data_token["exp"] = datetime.utcnow() + timedelta(seconds=TOKEN_SECONDS_EXPIRE)
    token_jwt = jwt.encode(data_token, key = SECRET_KEY, algorithm="HS256")
    return token_jwt

# Función para hacer hash de la contraseña
def hash_contrasena(password: str) -> str:
    return pwd_context.hash(password)

# Función para verificar la contraseña contra su hash
def verificar_contrasena(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def validate_user(username: str, password: str, db: Session = Depends(get_db)):
    user = crud.get_usur_by_name(db=db, nombre=username)
    if user and verificar_contrasena(password, user.contrasena):
        return True
    return False
        
@app.get('/')
def inicio():
    return RedirectResponse(url='/docs/')
        
@app.get('/')
def root():
    return {'mensaje': 'Bienvenido a la API de usuarios'}

@app.get('/api/usuarios/', response_model=list[Buscar_Usuario])
def get_user(db: Session = Depends(get_db)):
    return crud.get_usuarios(db=db)

@app.get('/api/user/{id:int}', response_model=Buscar_Usuario)
def get_user(id, db: Session = Depends(get_db)):
    user_by_id = crud.get_usuario_by_id(db=db, id_usuario=id)
    if user_by_id: 
        return user_by_id
    raise HTTPException(status_code=404, detail=f'El usuario con el id {id} no se encuentra en la base de datos')

@app.post('/api/usuarios/', response_model=Buscar_Usuario)
def create_user(user: Datos_Usuarios, db: Session = Depends(get_db)):
    # Verificar si el nombre ya está en uso
    check_name = crud.get_usur_by_name(db=db, nombre=user.nombre)
    if check_name:
        raise HTTPException(status_code=400, detail=f'El usuario {user.nombre} ya se encuentra en la base de datos')

    # Hash de la contraseña
    user.contrasena = hash_contrasena(user.contrasena)

    # Crear el nuevo usuario
    return crud.create_usuario(db=db, usuario=user)


@app.post('/api/login/', response_model=LoginResponse)
def login(user: Login, db: Session = Depends(get_db)):
    if user.nombre and user.contrasena:
        if validate_user(user.nombre, user.contrasena, db):
            # Crear el token
            token = create_token(data={"sub": user.nombre})
            
            # Imprimir el token en la consola
            print(f'Token generado para {user.nombre}: {token}')
            
            return LoginResponse(nombre=user.nombre, token=token)
        raise HTTPException(status_code=404, detail='Usuario o contraseña incorrectos')
    else:
        return "No Authorization"
