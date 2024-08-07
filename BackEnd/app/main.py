from starlette.responses import RedirectResponse
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import crud
from .conexion import SessionLocal, engine
from .schemas import Datos_Usuarios, Buscar_Usuario
from .models import Base

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

    # Verificar si el correo ya está en uso
    check_email = crud.get_user_by_email(db=db, email=user.correo)
    if check_email:
        raise HTTPException(status_code=400, detail=f'El correo {user.correo} ya se encuentra en uso')
    
    # Crear el nuevo usuario
    return crud.create_usuario(db=db, usuario=user)
