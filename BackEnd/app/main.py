from typing import Annotated, List
from starlette.responses import RedirectResponse
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from . import crud
from .conexion import SessionLocal, engine
from .schemas import Datos_Usuarios, Buscar_Usuario, Login, LoginResponse, HorarioBase, Horario, VentaBase
from .schemas import Datos_Usuarios, Buscar_Usuario, Login, LoginResponse,  Horario,  Venta,  DetalleVenta, DetalleVentaBase, DetalleIngreso, DetalleIngresoBase
from .schemas import Categoria,  Presentacion,   Cliente,  Proveedor, CategoriaBase, PresentacionBase,  ClienteBase, ProveedorBase, EmpleadoBase, Empleado
from .schemas import Articulo, Lote, ArticuloBase, LoteBase, Ingreso, IngresoBase
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
    "http://localhost:3000",  # El origen de tu aplicación React
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
    user = crud.get_usur_by_name(db=db, usuario=username)
    if user and verificar_contrasena(password, user.contrasena):
        return True
    return False

@app.get('/')
def inicio():
    return RedirectResponse(url='/docs/')

@app.get('/api/usuariosObtener/', response_model=List[Buscar_Usuario])
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
    check_name = crud.get_usur_by_name(db=db, usuario=user.usuario)
    if check_name:
        raise HTTPException(status_code=400, detail=f'El usuario {user.usuario} ya se encuentra en la base de datos')
    
    user.contrasena = hash_contrasena(user.contrasena)
    return crud.create_usuario(db=db, usuario=user)

@app.post('/api/login/', response_model=LoginResponse)
def login(user: Login, db: Session = Depends(get_db)):
    if user.usuario and user.contrasena:
        if validate_user(user.usuario, user.contrasena, db):
            token = create_token(data={"sub": user.usuario})
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
@app.get('/api/categoriasObtener/', response_model=List[Categoria])
def get_categorias(db: Session = Depends(get_db)):
    return crud.get_categorias(db=db)

@app.get('/api/categoria/{idcategoria}', response_model=Categoria)
def get_categoria(idcategoria: int, db: Session = Depends(get_db)):
    categoria_by_id = crud.get_categoria_by_id(db=db, idcategoria=idcategoria)
    if categoria_by_id:
        return categoria_by_id
    raise HTTPException(status_code=404, detail=f'La categoría con el id {idcategoria} no se encuentra en la base de datos')

@app.post('/api/categorias/', response_model=Categoria)
def create_categoria(categoria: CategoriaBase, db: Session = Depends(get_db)):
    return crud.create_categoria(db=db, categoria=categoria)

@app.put('/api/categoria/{idcategoria}', response_model=Categoria)
def update_categoria(idcategoria: int, categoria: CategoriaBase, db: Session = Depends(get_db)):
    updated_categoria = crud.update_categoria(db=db, idcategoria=idcategoria, categoria=categoria)
    if updated_categoria:
        return updated_categoria
    raise HTTPException(status_code=404, detail=f'La categoría con el id {idcategoria} no se encuentra en la base de datos')

@app.delete('/api/categoria/{idcategoria}', response_model=Categoria)
def delete_categoria(idcategoria: int, db: Session = Depends(get_db)):
    deleted_categoria = crud.delete_categoria(db=db, idcategoria=idcategoria)
    if deleted_categoria:
        return deleted_categoria
    raise HTTPException(status_code=404, detail=f'La categoría con el id {idcategoria} no se encuentra en la base de datos')

# Rutas para Presentacion
@app.get('/api/presentacionesObtener/', response_model=List[Presentacion])
def get_presentaciones(db: Session = Depends(get_db)):
    return crud.get_presentaciones(db=db)

@app.get('/api/presentacion/{idpresentacion}', response_model=Presentacion)
def get_presentacion(idpresentacion: int, db: Session = Depends(get_db)):
    presentacion_by_id = crud.get_presentacion_by_id(db=db, idpresentacion=idpresentacion)
    if presentacion_by_id:
        return presentacion_by_id
    raise HTTPException(status_code=404, detail=f'La presentación con el id {idpresentacion} no se encuentra en la base de datos')

@app.post('/api/presentaciones/', response_model=Presentacion)
def create_presentacion(presentacion: PresentacionBase, db: Session = Depends(get_db)):
    return crud.create_presentacion(db=db, presentacion=presentacion)

@app.put('/api/presentacion/{idpresentacion}', response_model=Presentacion)
def update_presentacion(idpresentacion: int, presentacion: PresentacionBase, db: Session = Depends(get_db)):
    updated_presentacion = crud.update_presentacion(db=db, idpresentacion=idpresentacion, presentacion=presentacion)
    if updated_presentacion:
        return updated_presentacion
    raise HTTPException(status_code=404, detail=f'La presentación con el id {idpresentacion} no se encuentra en la base de datos')


@app.delete('/api/presentacionDelete/{idpresentacion}', response_model=Presentacion)
def delete_presentacion(idpresentacion: int, db: Session = Depends(get_db)):
    deleted_presentacion = crud.delete_presentacion(db=db, idpresentacion=idpresentacion)
    if deleted_presentacion:
        return deleted_presentacion
    raise HTTPException(status_code=404, detail=f'La presentación con el id {idpresentacion} no se encuentra en la base de datos')

# Rutas para Lote
@app.get('/api/lotes/', response_model=List[Lote])
def get_lotes(db: Session = Depends(get_db)):
     return crud.get_lotes(db=db)

@app.get('/api/lote/{idlote}', response_model=Lote)
def get_lote(idlote: int, db: Session = Depends(get_db)):
     lote_by_id = crud.get_lote_by_id(db=db, idlote=idlote)
     if lote_by_id:
         return lote_by_id
     raise HTTPException(status_code=404, detail=f'El lote con el id {idlote} no se encuentra en la base de datos')

@app.post('/api/lotes/', response_model=Lote)
def create_lote(lote: LoteBase, db: Session = Depends(get_db)):
     return crud.create_lote(db=db, lote=lote)

@app.put('/api/lote/{idlote}', response_model=Lote)
def update_lote(idlote: int, lote: LoteBase, db: Session = Depends(get_db)):
     updated_lote = crud.update_lote(db=db, idlote=idlote, lote=lote)
     if updated_lote:
         return updated_lote
     raise HTTPException(status_code=404, detail=f'El lote con el id {idlote} no se encuentra en la base de datos')

@app.delete('/api/lote/{idlote}', response_model=Lote)
def delete_lote(idlote: int, db: Session = Depends(get_db)):
     deleted_lote = crud.delete_lote(db=db, idlote=idlote)
     if deleted_lote:
         return deleted_lote
     raise HTTPException(status_code=404, detail=f'El lote con el id {idlote} no se encuentra en la base de datos')

# Rutas para Cliente
@app.get('/api/clientesObtener/', response_model=List[Cliente])
def get_clientes(db: Session = Depends(get_db)):
    return crud.get_clientes(db=db)

@app.get('/api/cliente/{idcliente}', response_model=Cliente)
def get_cliente(idcliente: int, db: Session = Depends(get_db)):
    cliente_by_id = crud.get_cliente_by_id(db=db, idcliente=idcliente)
    if cliente_by_id:
        return cliente_by_id
    raise HTTPException(status_code=404, detail=f'El cliente con el id {idcliente} no se encuentra en la base de datos')

@app.post('/api/clientes/', response_model=Cliente)
def create_cliente(cliente: ClienteBase, db: Session = Depends(get_db)):
    return crud.create_cliente(db=db, cliente=cliente)

@app.put('/api/clienteActualizar/{idcliente}', response_model=Cliente)
def update_cliente(idcliente: int, cliente: ClienteBase, db: Session = Depends(get_db)):
    updated_cliente = crud.update_cliente(db=db, idcliente=idcliente, cliente=cliente)
    if updated_cliente:
        return updated_cliente
    raise HTTPException(status_code=404, detail=f'El cliente con el id {idcliente} no se encuentra en la base de datos')

@app.delete('/api/clienteDelete/{idcliente}', response_model=Cliente)
def delete_cliente(idcliente: int, db: Session = Depends(get_db)):
    deleted_cliente = crud.delete_cliente(db=db, idcliente=idcliente)
    if deleted_cliente:
        return deleted_cliente
    raise HTTPException(status_code=404, detail=f'El cliente con el id {idcliente} no se encuentra en la base de datos')

# Rutas para Proveedor
@app.get('/api/proveedoresObtener/', response_model=List[Proveedor])
def get_proveedores(db: Session = Depends(get_db)):
    return crud.get_proveedores(db=db)

@app.get('/api/proveedor/{idproveedor}', response_model=Proveedor)
def get_proveedor(idproveedor: int, db: Session = Depends(get_db)):
    proveedor_by_id = crud.get_proveedor_by_id(db=db, idproveedor=idproveedor)
    if proveedor_by_id:
        return proveedor_by_id
    raise HTTPException(status_code=404, detail=f'El proveedor con el id {idproveedor} no se encuentra en la base de datos')

@app.post('/api/proveedores/', response_model=Proveedor)
def create_proveedor(proveedor: ProveedorBase, db: Session = Depends(get_db)):
    return crud.create_proveedor(db=db, proveedor=proveedor)

@app.put('/api/proveedoresActualizar/{idproveedor}', response_model=Proveedor)
def update_proveedor(idproveedor: int, proveedor: ProveedorBase, db: Session = Depends(get_db)):
    updated_proveedor = crud.update_proveedor(db=db, idproveedor=idproveedor, proveedor=proveedor)
    if updated_proveedor:
        return updated_proveedor
    raise HTTPException(status_code=404, detail=f'El proveedor con el id {idproveedor} no se encuentra en la base de datos')

@app.delete('/api/proveedorDelete/{idproveedor}', response_model=Proveedor)
def delete_proveedor(idproveedor: int, db: Session = Depends(get_db)):
    deleted_proveedor = crud.delete_proveedor(db=db, idproveedor=idproveedor)
    if deleted_proveedor:
        return deleted_proveedor
    raise HTTPException(status_code=404, detail=f'El proveedor con el id {idproveedor} no se encuentra en la base de datos')

# Rutas para Empleado
@app.get('/api/empleadosObtener/', response_model=List[Empleado])
def get_empleados(db: Session = Depends(get_db)):
    return crud.get_empleado(db=db)

@app.get('/api/empleado/{idempleado}', response_model=Empleado)
def get_empleado(idempleado: int, db: Session = Depends(get_db)):
    empleado_by_id = crud.get_empleado_by_id(db=db, idempleado=idempleado)
    if empleado_by_id:
        return empleado_by_id
    raise HTTPException(status_code=404, detail=f'El empleado con el id {idempleado} no se encuentra en la base de datos')

@app.post('/api/empleados/', response_model=Empleado)
async def create_empleado(empleado: EmpleadoBase, db: Session = Depends(get_db)):
    try:
        nuevo_empleado = crud.create_empleado(db=db, empleado=empleado)
        return nuevo_empleado
    except ValueError as e:
        print(e.json())
        raise HTTPException(status_code=422, detail=str(e))

@app.put("/api/empleadoDisponible/{idempleado}")
def update_empleado_disponible(idempleado: int, disponible: bool, db: Session = Depends(get_db)):
    empleado_by_id = crud.get_empleado_by_id(db=db, idempleado=idempleado)
    if not empleado_by_id:
        raise HTTPException(status_code=404, detail=f"El empleado con id {idempleado} no existe.")
    
    # Actualiza el campo 'disponible'
    try:
        empleado_actualizado = crud.update_empleado_disponible(db=db, idempleado=idempleado, disponible=disponible)
        return empleado_actualizado
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al actualizar el estado del empleado.")
    

@app.put('/api/empleadoUpdate/{idempleado}', response_model=Empleado)
def update_empleado(idempleado: int, empleado: EmpleadoBase, db: Session = Depends(get_db)):
    updated_empleado = crud.update_empleado(db=db, idempleado=idempleado, empleado=empleado)
    if updated_empleado:
        return updated_empleado
    raise HTTPException(status_code=404, detail=f'El empleado con el id {idempleado} no se encuentra en la base de datos')

@app.delete('/api/empleado/{idempleado}', response_model=Empleado)
def delete_empleado(idempleado: int, db: Session = Depends(get_db)):
    deleted_empleado = crud.delete_empleado(db=db, idempleado=idempleado)
    if deleted_empleado:
        return deleted_empleado
    raise HTTPException(status_code=404, detail=f'El empleado con el id {idempleado} no se encuentra en la base de datos')

#Rutas de Articulo
@app.get('/api/articulosObtener/', response_model=List[Articulo])
def get_articulos(db: Session = Depends(get_db)):
    return crud.get_articulo(db=db)

@app.get('/api/articulo/{idarticulo}', response_model=Articulo)
def get_articulo(idarticulo: int, db: Session = Depends(get_db)):
    articulo_by_id = crud.get_articulo_by_id(db=db, idarticulo=idarticulo)
    if articulo_by_id:
        return articulo_by_id
    raise HTTPException(status_code=404, detail=f'El artículo con el id {idarticulo} no se encuentra en la base de datos')

@app.post('/api/articulos/', response_model=Articulo)
async def create_articulo(articulo: Articulo, db: Session = Depends(get_db)):
    try:
        nuevo_articulo = crud.create_articulo(db=db, articulo=articulo)
        return nuevo_articulo
    except ValueError as e:
        print(e.json())
        raise HTTPException(status_code=422, detail=str(e))
    
@app.put('/api/articulo/{idarticulo}', response_model=Articulo)
def update_articulo(idarticulo: int, articulo: Articulo, db: Session = Depends(get_db)):
    updated_articulo = crud.update_articulo(db=db, idarticulo=idarticulo, articulo=articulo)
    if updated_articulo:
        return updated_articulo
    raise HTTPException(status_code=404, detail=f'El artículo con el id {idarticulo} no se encuentra en la base de datos')

@app.delete('/api/articulo/{idarticulo}', response_model=Articulo)
def delete_articulo(idarticulo: int, db: Session = Depends(get_db)):
    deleted_articulo = crud.delete_articulo(db=db, idarticulo=idarticulo)
    if deleted_articulo:
        return deleted_articulo
    raise HTTPException(status_code=404, detail=f'El artículo con el id {idarticulo} no se encuentra en la base de datos')

#Rutas Horarios
@app.get('/api/horarios/', response_model=list[Horario])
def get_horarios(db: Session = Depends(get_db)):
    return crud.get_horarios(db=db)

@app.get('/api/horario/{idhorario}', response_model=Horario)
def get_horario(idhorario: int, db: Session = Depends(get_db)):
    horario = crud.get_horario(db=db, horario_id=idhorario)
    if horario:
        return horario
    raise HTTPException(status_code=404, detail=f'El horario con el id {idhorario} no se encuentra en la base de datos')

@app.post('/api/horarios/', response_model=Horario)
def create_horario(horario: HorarioBase, db: Session = Depends(get_db)):
    return crud.create_horario(db=db, horario=horario)

@app.put('/api/horario/{idhorario}', response_model=Horario)
def update_horario(idhorario: int, horario: HorarioBase, db: Session = Depends(get_db)):
    updated_horario = crud.update_horario(db=db, horario_id=idhorario, horario_update=horario)
    if updated_horario:
        return updated_horario
    raise HTTPException(status_code=404, detail=f'El horario con el id {idhorario} no se encuentra en la base de datos')

@app.delete('/api/horario/{idhorario}', response_model=Horario)
def delete_horario(idhorario: int, db: Session = Depends(get_db)):
    deleted_horario = crud.delete_horario(db=db, horario_id=idhorario)
    if deleted_horario:
        return deleted_horario
    raise HTTPException(status_code=404, detail=f'El horario con el id {idhorario} no se encuentra en la base de datos')

#Rutas venta
@app.get('/api/ventas/', response_model=list[Venta])
def get_ventas(db: Session = Depends(get_db)):
    return crud.get_ventas(db=db)

@app.get('/api/venta/{idventa}', response_model=Venta)
def get_venta(idventa: int, db: Session = Depends(get_db)):
    venta = crud.get_venta(db=db, venta_id=idventa)
    if venta:
        return venta
    raise HTTPException(status_code=404, detail=f'La venta con el id {idventa} no se encuentra en la base de datos')

@app.post('/api/ventas/', response_model=Venta)
def create_venta(venta: VentaBase, db: Session = Depends(get_db)):
    return crud.create_venta(db=db, venta=venta)

@app.put('/api/venta/{idventa}', response_model=Venta)
def update_venta(idventa: int, venta: VentaBase, db: Session = Depends(get_db)):
    updated_venta = crud.update_venta(db=db, venta_id=idventa, venta_update=venta)
    if updated_venta:
        return updated_venta
    raise HTTPException(status_code=404, detail=f'La venta con el id {idventa} no se encuentra en la base de datos')

@app.delete('/api/venta/{idventa}', response_model=Venta)
def delete_venta(idventa: int, db: Session = Depends(get_db)):
    deleted_venta = crud.delete_venta(db=db, venta_id=idventa)
    if deleted_venta:
        return deleted_venta
    raise HTTPException(status_code=404, detail=f'La venta con el id {idventa} no se encuentra en la base de datos')

#Rustas Detalle_venta
@app.get('/api/detalles_venta/', response_model=list[DetalleVenta])
def get_detalles_venta(db: Session = Depends(get_db)):
    return crud.get_detalles_venta(db=db)

@app.get('/api/detalle_venta/{iddetalle_venta}', response_model=DetalleVenta)
def get_detalle_venta(iddetalle_venta: int, db: Session = Depends(get_db)):
    detalle_venta = crud.get_detalle_venta(db=db, detalle_venta_id=iddetalle_venta)
    if detalle_venta:
        return detalle_venta
    raise HTTPException(status_code=404, detail=f'El detalle de venta con el id {iddetalle_venta} no se encuentra en la base de datos')

@app.post('/api/detalles_venta/', response_model=DetalleVenta)
def create_detalle_venta(detalle_venta: DetalleVentaBase, db: Session = Depends(get_db)):
    return crud.create_detalle_venta(db=db, detalle_venta=detalle_venta)

@app.put('/api/detalle_venta/{iddetalle_venta}', response_model=DetalleVenta)
def update_detalle_venta(iddetalle_venta: int, detalle_venta: DetalleVentaBase, db: Session = Depends(get_db)):
    updated_detalle_venta = crud.update_detalle_venta(db=db, detalle_venta_id=iddetalle_venta, detalle_venta_update=detalle_venta)
    if updated_detalle_venta:
        return updated_detalle_venta
    raise HTTPException(status_code=404, detail=f'El detalle de venta con el id {iddetalle_venta} no se encuentra en la base de datos')

@app.delete('/api/detalle_venta/{iddetalle_venta}', response_model=DetalleVenta)
def delete_detalle_venta(iddetalle_venta: int, db: Session = Depends(get_db)):
    deleted_detalle_venta = crud.delete_detalle_venta(db=db, detalle_venta_id=iddetalle_venta)
    if deleted_detalle_venta:
        return deleted_detalle_venta
    raise HTTPException(status_code=404, detail=f'El detalle de venta con el id {iddetalle_venta} no se encuentra en la base de datos')


#Ruta ingreso
@app.get('/api/ingresos/', response_model=list[Ingreso])
def get_ingresos(db: Session = Depends(get_db)):
    return crud.get_ingresos(db=db)

@app.get('/api/ingreso/{idingreso}', response_model=Ingreso)
def get_ingreso(idingreso: int, db: Session = Depends(get_db)):
    ingreso = crud.get_ingreso(db=db, ingreso_id=idingreso)
    if ingreso:
        return ingreso
    raise HTTPException(status_code=404, detail=f'El ingreso con el id {idingreso} no se encuentra en la base de datos')

@app.post('/api/ingresos/', response_model=Ingreso)
def create_ingreso(ingreso: IngresoBase, db: Session = Depends(get_db)):
    return crud.create_ingreso(db=db, ingreso=ingreso)

@app.put('/api/ingreso/{idingreso}', response_model=Ingreso)
def update_ingreso(idingreso: int, ingreso: IngresoBase, db: Session = Depends(get_db)):
    updated_ingreso = crud.update_ingreso(db=db, ingreso_id=idingreso, ingreso_update=ingreso)
    if updated_ingreso:
        return updated_ingreso
    raise HTTPException(status_code=404, detail=f'El ingreso con el id {idingreso} no se encuentra en la base de datos')

@app.delete('/api/ingreso/{idingreso}', response_model=Ingreso)
def delete_ingreso(idingreso: int, db: Session = Depends(get_db)):
    deleted_ingreso = crud.delete_ingreso(db=db, ingreso_id=idingreso)
    if deleted_ingreso:
        return deleted_ingreso
    raise HTTPException(status_code=404, detail=f'El ingreso con el id {idingreso} no se encuentra en la base de datos')

#Rutas detalle_ingreso
@app.get('/api/detalles_ingreso/', response_model=list[DetalleIngreso])
def get_detalles_ingreso(db: Session = Depends(get_db)):
    return crud.get_detalles_ingreso(db=db)

@app.get('/api/detalle_ingreso/{iddetalle_ingreso}', response_model=DetalleIngreso)
def get_detalle_ingreso(iddetalle_ingreso: int, db: Session = Depends(get_db)):
    detalle_ingreso = crud.get_detalle_ingreso(db=db, detalle_ingreso_id=iddetalle_ingreso)
    if detalle_ingreso:
        return detalle_ingreso
    raise HTTPException(status_code=404, detail=f'El detalle de ingreso con el id {iddetalle_ingreso} no se encuentra en la base de datos')

@app.post('/api/detalles_ingreso/', response_model=DetalleIngreso)
def create_detalle_ingreso(detalle_ingreso: DetalleIngresoBase, db: Session = Depends(get_db)):
    return crud.create_detalle_ingreso(db=db, detalle_ingreso=detalle_ingreso)

@app.put('/api/detalle_ingreso/{iddetalle_ingreso}', response_model=DetalleIngreso)
def update_detalle_ingreso(iddetalle_ingreso: int, detalle_ingreso: DetalleIngresoBase, db: Session = Depends(get_db)):
    updated_detalle_ingreso = crud.update_detalle_ingreso(db=db, detalle_ingreso_id=iddetalle_ingreso, detalle_ingreso_update=detalle_ingreso)
    if updated_detalle_ingreso:
        return updated_detalle_ingreso
    raise HTTPException(status_code=404, detail=f'El detalle de ingreso con el id {iddetalle_ingreso} no se encuentra en la base de datos')

@app.delete('/api/detalle_ingreso/{iddetalle_ingreso}', response_model=DetalleIngreso)
def delete_detalle_ingreso(iddetalle_ingreso: int, db: Session = Depends(get_db)):
    deleted_detalle_ingreso = crud.delete_detalle_ingreso(db=db, detalle_ingreso_id=iddetalle_ingreso)
    if deleted_detalle_ingreso:
        return deleted_detalle_ingreso
    raise HTTPException(status_code=404, detail=f'El detalle de ingreso con el id {iddetalle_ingreso} no se encuentra en la base de datos')

