from starlette.responses import RedirectResponse
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import crud
from .conexion import SessionLocal, engine
from .schemas import Datos_Usuarios, Buscar_Usuario
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

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
    check_name = crud.get_usur_by_name(db=db, nombre=user.nombre)
    if check_name:
        raise HTTPException(status_code=400, detail=f'El usuario {user.nombre} ya se encuentra en la base de datos')
    return crud.create_usuario(db=db, usuario=user)