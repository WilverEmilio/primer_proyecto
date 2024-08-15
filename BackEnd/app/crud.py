from sqlalchemy.orm import Session

from .models import Usuario, Categoria, Presentacion,  Cliente, Proveedor, Empleado
from .schemas import Datos_Usuarios, CategoriaBase, PresentacionBase,  ClienteBase, ProveedorBase, EmpleadoBase

# CRUD para Usuario
def get_usuarios(db: Session):
    return db.query(Usuario).all()

def get_usuario_by_id(db: Session, id_usuario: int):
    return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()

def get_usur_by_name(db: Session, usuario: str):
    return db.query(Usuario).filter(Usuario.usuario == usuario).first()

def create_usuario(db: Session, usuario: Datos_Usuarios):
    new_user = Usuario(usuario=usuario.usuario, contrasena=usuario.contrasena, rol=usuario.rol, email=usuario.email,  idempleado=usuario.idempleado)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login(db: Session, nombre: str, contrasena: str):
    return db.query(Usuario).filter(Usuario.usuario == nombre, Usuario.contrasena == contrasena).first()

# CRUD para Categoria
def get_categorias(db: Session):
    return db.query(Categoria).all()

def get_categoria_by_id(db: Session, idcategoria: int):
    return db.query(Categoria).filter(Categoria.idcategoria == idcategoria).first()

def create_categoria(db: Session, categoria: CategoriaBase):
    new_categoria = Categoria(nombre=categoria.nombre, descripcion=categoria.descripcion)
    db.add(new_categoria)
    db.commit()
    db.refresh(new_categoria)
    return new_categoria

def update_categoria(db: Session, idcategoria: int, categoria: CategoriaBase):
    db_categoria = db.query(Categoria).filter(Categoria.idcategoria == idcategoria).first()
    if db_categoria:
        db_categoria.nombre = categoria.nombre
        db_categoria.descripcion = categoria.descripcion
        db.commit()
        db.refresh(db_categoria)
    return db_categoria

def delete_categoria(db: Session, idcategoria: int):
    db_categoria = db.query(Categoria).filter(Categoria.idcategoria == idcategoria).first()
    if db_categoria:
        db.delete(db_categoria)
        db.commit()
    return db_categoria

# CRUD para Presentacion
def get_presentaciones(db: Session):
    return db.query(Presentacion).all()

def get_presentacion_by_id(db: Session, idpresentacion: int):
    return db.query(Presentacion).filter(Presentacion.idpresentacion == idpresentacion).first()

def create_presentacion(db: Session, presentacion: PresentacionBase):
    new_presentacion = Presentacion(nombre=presentacion.nombre, descripcion=presentacion.descripcion)
    db.add(new_presentacion)
    db.commit()
    db.refresh(new_presentacion)
    return new_presentacion

def update_presentacion(db: Session, idpresentacion: int, presentacion: PresentacionBase):
    db_presentacion = db.query(Presentacion).filter(Presentacion.idpresentacion == idpresentacion).first()
    if db_presentacion:
        db_presentacion.nombre = presentacion.nombre
        db_presentacion.descripcion = presentacion.descripcion
        db.commit()
        db.refresh(db_presentacion)
        return db_presentacion
    return None


def delete_presentacion(db: Session, idpresentacion: int):
    db_presentacion = db.query(Presentacion).filter(Presentacion.idpresentacion == idpresentacion).first()
    if db_presentacion:
        db.delete(db_presentacion)
        db.commit()
    return db_presentacion

# # CRUD para Lote
# def get_lotes(db: Session):
#     return db.query(Lote).all()

# def get_lote_by_id(db: Session, idlote: int):
#     return db.query(Lote).filter(Lote.idlote == idlote).first()

# def create_lote(db: Session, lote: LoteBase):
#     new_lote = Lote(idarticulo=lote.idarticulo, numero_lote=lote.numero_lote, cantidad=lote.cantidad, fecha_vencimiento=lote.fecha_vencimiento)
#     db.add(new_lote)
#     db.commit()
#     db.refresh(new_lote)
#     return new_lote

# def update_lote(db: Session, idlote: int, lote: LoteBase):
#     db_lote = db.query(Lote).filter(Lote.idlote == idlote).first()
#     if db_lote:
#         db_lote.idarticulo = lote.idarticulo
#         db_lote.numero_lote = lote.numero_lote
#         db_lote.cantidad = lote.cantidad
#         db_lote.fecha_vencimiento = lote.fecha_vencimiento
#         db.commit()
#         db.refresh(db_lote)
#     return db_lote

# def delete_lote(db: Session, idlote: int):
#     db_lote = db.query(Lote).filter(Lote.idlote == idlote).first()
#     if db_lote:
#         db.delete(db_lote)
#         db.commit()
#     return db_lote

# CRUD para Cliente
def get_clientes(db: Session):
    return db.query(Cliente).all()

def get_cliente_by_id(db: Session, idcliente: int):
    return db.query(Cliente).filter(Cliente.idcliente == idcliente).first()

def create_cliente(db: Session, cliente: ClienteBase):
    new_cliente = Cliente(nombre=cliente.nombre, apellido=cliente.apellido, run_documento=cliente.run_documento, direccion=cliente.direccion, telefono=cliente.telefono, email=cliente.email)
    db.add(new_cliente)
    db.commit()
    db.refresh(new_cliente)
    return new_cliente

def update_cliente(db: Session, idcliente: int, cliente: ClienteBase):
    db_cliente = db.query(Cliente).filter(Cliente.idcliente == idcliente).first()
    if db_cliente:
        db_cliente.nombre = cliente.nombre
        db_cliente.apellido = cliente.apellido
        db_cliente.run_documento = cliente.run_documento
        db_cliente.direccion = cliente.direccion
        db_cliente.telefono = cliente.telefono
        db_cliente.email = cliente.email
        db.commit()
        db.refresh(db_cliente)
    return db_cliente

def delete_cliente(db: Session, idcliente: int):
    db_cliente = db.query(Cliente).filter(Cliente.idcliente == idcliente).first()
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
    return db_cliente

# CRUD para Proveedor
def get_proveedores(db: Session):
    return db.query(Proveedor).all()

def get_proveedor_by_id(db: Session, idproveedor: int):
    return db.query(Proveedor).filter(Proveedor.idproveedor == idproveedor).first()

def create_proveedor(db: Session, proveedor: ProveedorBase):
    new_proveedor = Proveedor(razon_social=proveedor.razon_social, tipo_documento=proveedor.tipo_documento, num_documento=proveedor.num_documento, direccion=proveedor.direccion, telefono=proveedor.telefono, email=proveedor.email, url=proveedor.url)
    db.add(new_proveedor)
    db.commit()
    db.refresh(new_proveedor)
    return new_proveedor

def update_proveedor(db: Session, idproveedor: int, proveedor: ProveedorBase):
    db_proveedor = db.query(Proveedor).filter(Proveedor.idproveedor == idproveedor).first()
    if db_proveedor:
        db_proveedor.razon_social = proveedor.razon_social
        db_proveedor.tipo_documento = proveedor.tipo_documento
        db_proveedor.num_documento = proveedor.num_documento
        db_proveedor.direccion = proveedor.direccion
        db_proveedor.telefono = proveedor.telefono
        db_proveedor.email = proveedor.email
        db_proveedor.url = proveedor.url
        db.commit()
        db.refresh(db_proveedor)
    return db_proveedor

def delete_proveedor(db: Session, idproveedor: int):
    db_proveedor = db.query(Proveedor).filter(Proveedor.idproveedor == idproveedor).first()
    if db_proveedor:
        db.delete(db_proveedor)
        db.commit()
    return db_proveedor


#Crud para empleado
def get_empleado(db: Session): 
    return db.query(Empleado).all()

def get_empleado_by_id(db: Session, idempleado: int):
    return db.query(Empleado).filter(Empleado.idempleado == idempleado).first()

def create_empleado(db: Session, empleado: EmpleadoBase):
    new_empleado = Empleado(
        nombre=empleado.nombre,
        apellidos=empleado.apellidos,
        telefono=empleado.telefono,
        direccion=empleado.direccion,
        disponible=True  # Agregar `disponible` con valor predeterminado
    )
    db.add(new_empleado)
    db.commit()
    db.refresh(new_empleado)
    return new_empleado

def update_empleado(db: Session, idempleado: int, empleado: EmpleadoBase):
    db_empleado = db.query(Empleado).filter(Empleado.idempleado == idempleado).first()
    if db_empleado:
        db_empleado.nombre = empleado.nombre
        db_empleado.apellidos = empleado.apellidos
        db_empleado.telefono = empleado.telefono
        db_empleado.direccion = empleado.direccion
        db.commit()
        db.refresh(db_empleado)
    return db_empleado
