from typing import Annotated, List
from starlette.responses import RedirectResponse
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from . import crud
from .conexion import SessionLocal, engine
from .schemas import Datos_Usuarios, Buscar_Usuario, Login, LoginResponse
from .schemas import Datos_Categoria, Buscar_Categoria, Datos_Presentacion, Buscar_Presentacion, Datos_Lote, Buscar_Lote, Datos_Cliente, Buscar_Cliente, Datos_Proveedor, Buscar_Proveedor
from .models import Base
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse

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

def create_token(data: dict): 
    data_token = data.copy()
    data_token["exp"] = datetime.utcnow() + timedelta(seconds=TOKEN_SECONDS_EXPIRE)
    token_jwt = jwt.encode(data_token, key=SECRET_KEY, algorithm="HS256")
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

@app.get('/api/usuarios/', response_model=List[Buscar_Usuario])
def get_users(db: Session = Depends(get_db)):
    return crud.get_usuarios(db=db)

@app.get('/api/usuario/{id_usuario}', response_model=Buscar_Usuario)
def get_user(id_usuario: int, db: Session = Depends(get_db)):
    user_by_id = crud.get_usuario_by_id(db=db, id_usuario=id_usuario)
    if user_by_id:
        return user_by_id
    raise HTTPException(status_code=404, detail=f'El usuario con el id {id_usuario} no se encuentra en la base de datos')

@app.post('/api/usuarios/', response_model=Buscar_Usuario)
def create_user(user: Datos_Usuarios, db: Session = Depends(get_db)):
    check_name = crud.get_usur_by_name(db=db, nombre=user.nombre)
    if check_name:
        raise HTTPException(status_code=400, detail=f'El usuario {user.nombre} ya se encuentra en la base de datos')
    
    user.contrasena = hash_contrasena(user.contrasena)
    return crud.create_usuario(db=db, usuario=user)

@app.post('/api/login/', response_model=LoginResponse)
def login(user: Login, db: Session = Depends(get_db)):
    if user.nombre and user.contrasena:
        if validate_user(user.nombre, user.contrasena, db):
            token = create_token(data={"sub": user.nombre})
            expired = datetime.utcnow() + timedelta(seconds=TOKEN_SECONDS_EXPIRE)
            
            response = JSONResponse(content={
                "message": "Login successful",
                "token": token,
                "expires_at": expired.strftime('%Y-%m-%d %H:%M:%S UTC')
            })
            response.set_cookie(key="access_token", value=token, httponly=True, samesite="Strict", expires=TOKEN_SECONDS_EXPIRE)
            
            return response
    raise HTTPException(status_code=400, detail="Invalid username or password")

# Rutas para Categoria
@app.get('/api/categorias/', response_model=List[Buscar_Categoria])
def get_categorias(db: Session = Depends(get_db)):
    return crud.get_categorias(db=db)

@app.get('/api/categoria/{idcategoria}', response_model=Buscar_Categoria)
def get_categoria(idcategoria: int, db: Session = Depends(get_db)):
    categoria_by_id = crud.get_categoria_by_id(db=db, idcategoria=idcategoria)
    if categoria_by_id:
        return categoria_by_id
    raise HTTPException(status_code=404, detail=f'La categoría con el id {idcategoria} no se encuentra en la base de datos')

@app.post('/api/categorias/', response_model=Buscar_Categoria)
def create_categoria(categoria: Datos_Categoria, db: Session = Depends(get_db)):
    return crud.create_categoria(db=db, categoria=categoria)

@app.put('/api/categoria/{idcategoria}', response_model=Buscar_Categoria)
def update_categoria(idcategoria: int, categoria: Datos_Categoria, db: Session = Depends(get_db)):
    updated_categoria = crud.update_categoria(db=db, idcategoria=idcategoria, categoria=categoria)
    if updated_categoria:
        return updated_categoria
    raise HTTPException(status_code=404, detail=f'La categoría con el id {idcategoria} no se encuentra en la base de datos')

@app.delete('/api/categoria/{idcategoria}', response_model=Buscar_Categoria)
def delete_categoria(idcategoria: int, db: Session = Depends(get_db)):
    deleted_categoria = crud.delete_categoria(db=db, idcategoria=idcategoria)
    if deleted_categoria:
        return deleted_categoria
    raise HTTPException(status_code=404, detail=f'La categoría con el id {idcategoria} no se encuentra en la base de datos')

# Rutas para Presentacion
@app.get('/api/presentaciones/', response_model=List[Buscar_Presentacion])
def get_presentaciones(db: Session = Depends(get_db)):
    return crud.get_presentaciones(db=db)

@app.get('/api/presentacion/{idpresentacion}', response_model=Buscar_Presentacion)
def get_presentacion(idpresentacion: int, db: Session = Depends(get_db)):
    presentacion_by_id = crud.get_presentacion_by_id(db=db, idpresentacion=idpresentacion)
    if presentacion_by_id:
        return presentacion_by_id
    raise HTTPException(status_code=404, detail=f'La presentación con el id {idpresentacion} no se encuentra en la base de datos')

@app.post('/api/presentaciones/', response_model=Buscar_Presentacion)
def create_presentacion(presentacion: Datos_Presentacion, db: Session = Depends(get_db)):
    return crud.create_presentacion(db=db, presentacion=presentacion)

@app.put('/api/presentacion/{idpresentacion}', response_model=Buscar_Presentacion)
def update_presentacion(idpresentacion: int, presentacion: Datos_Presentacion, db: Session = Depends(get_db)):
    updated_presentacion = crud.update_presentacion(db=db, idpresentacion=idpresentacion, presentacion=presentacion)
    if updated_presentacion:
        return updated_presentacion
    raise HTTPException(status_code=404, detail=f'La presentación con el id {idpresentacion} no se encuentra en la base de datos')

@app.delete('/api/presentacion/{idpresentacion}', response_model=Buscar_Presentacion)
def delete_presentacion(idpresentacion: int, db: Session = Depends(get_db)):
    deleted_presentacion = crud.delete_presentacion(db=db, idpresentacion=idpresentacion)
    if deleted_presentacion:
        return deleted_presentacion
    raise HTTPException(status_code=404, detail=f'La presentación con el id {idpresentacion} no se encuentra en la base de datos')

# Rutas para Lote
@app.get('/api/lotes/', response_model=List[Buscar_Lote])
def get_lotes(db: Session = Depends(get_db)):
    return crud.get_lotes(db=db)

@app.get('/api/lote/{idlote}', response_model=Buscar_Lote)
def get_lote(idlote: int, db: Session = Depends(get_db)):
    lote_by_id = crud.get_lote_by_id(db=db, idlote=idlote)
    if lote_by_id:
        return lote_by_id
    raise HTTPException(status_code=404, detail=f'El lote con el id {idlote} no se encuentra en la base de datos')

@app.post('/api/lotes/', response_model=Buscar_Lote)
def create_lote(lote: Datos_Lote, db: Session = Depends(get_db)):
    return crud.create_lote(db=db, lote=lote)

@app.put('/api/lote/{idlote}', response_model=Buscar_Lote)
def update_lote(idlote: int, lote: Datos_Lote, db: Session = Depends(get_db)):
    updated_lote = crud.update_lote(db=db, idlote=idlote, lote=lote)
    if updated_lote:
        return updated_lote
    raise HTTPException(status_code=404, detail=f'El lote con el id {idlote} no se encuentra en la base de datos')

@app.delete('/api/lote/{idlote}', response_model=Buscar_Lote)
def delete_lote(idlote: int, db: Session = Depends(get_db)):
    deleted_lote = crud.delete_lote(db=db, idlote=idlote)
    if deleted_lote:
        return deleted_lote
    raise HTTPException(status_code=404, detail=f'El lote con el id {idlote} no se encuentra en la base de datos')

# Rutas para Cliente
@app.get('/api/clientes/', response_model=List[Buscar_Cliente])
def get_clientes(db: Session = Depends(get_db)):
    return crud.get_clientes(db=db)

@app.get('/api/cliente/{idcliente}', response_model=Buscar_Cliente)
def get_cliente(idcliente: int, db: Session = Depends(get_db)):
    cliente_by_id = crud.get_cliente_by_id(db=db, idcliente=idcliente)
    if cliente_by_id:
        return cliente_by_id
    raise HTTPException(status_code=404, detail=f'El cliente con el id {idcliente} no se encuentra en la base de datos')

@app.post('/api/clientes/', response_model=Buscar_Cliente)
def create_cliente(cliente: Datos_Cliente, db: Session = Depends(get_db)):
    return crud.create_cliente(db=db, cliente=cliente)

@app.put('/api/cliente/{idcliente}', response_model=Buscar_Cliente)
def update_cliente(idcliente: int, cliente: Datos_Cliente, db: Session = Depends(get_db)):
    updated_cliente = crud.update_cliente(db=db, idcliente=idcliente, cliente=cliente)
    if updated_cliente:
        return updated_cliente
    raise HTTPException(status_code=404, detail=f'El cliente con el id {idcliente} no se encuentra en la base de datos')

@app.delete('/api/cliente/{idcliente}', response_model=Buscar_Cliente)
def delete_cliente(idcliente: int, db: Session = Depends(get_db)):
    deleted_cliente = crud.delete_cliente(db=db, idcliente=idcliente)
    if deleted_cliente:
        return deleted_cliente
    raise HTTPException(status_code=404, detail=f'El cliente con el id {idcliente} no se encuentra en la base de datos')

# Rutas para Proveedor
@app.get('/api/proveedores/', response_model=List[Buscar_Proveedor])
def get_proveedores(db: Session = Depends(get_db)):
    return crud.get_proveedores(db=db)

@app.get('/api/proveedor/{idproveedor}', response_model=Buscar_Proveedor)
def get_proveedor(idproveedor: int, db: Session = Depends(get_db)):
    proveedor_by_id = crud.get_proveedor_by_id(db=db, idproveedor=idproveedor)
    if proveedor_by_id:
        return proveedor_by_id
    raise HTTPException(status_code=404, detail=f'El proveedor con el id {idproveedor} no se encuentra en la base de datos')

@app.post('/api/proveedores/', response_model=Buscar_Proveedor)
def create_proveedor(proveedor: Datos_Proveedor, db: Session = Depends(get_db)):
    return crud.create_proveedor(db=db, proveedor=proveedor)

@app.put('/api/proveedor/{idproveedor}', response_model=Buscar_Proveedor)
def update_proveedor(idproveedor: int, proveedor: Datos_Proveedor, db: Session = Depends(get_db)):
    updated_proveedor = crud.update_proveedor(db=db, idproveedor=idproveedor, proveedor=proveedor)
    if updated_proveedor:
        return updated_proveedor
    raise HTTPException(status_code=404, detail=f'El proveedor con el id {idproveedor} no se encuentra en la base de datos')

@app.delete('/api/proveedor/{idproveedor}', response_model=Buscar_Proveedor)
def delete_proveedor(idproveedor: int, db: Session = Depends(get_db)):
    deleted_proveedor = crud.delete_proveedor(db=db, idproveedor=idproveedor)
    if deleted_proveedor:
        return deleted_proveedor
    raise HTTPException(status_code=404, detail=f'El proveedor con el id {idproveedor} no se encuentra en la base de datos')
