from sqlalchemy.orm import Session
from .models import Usuario, Categoria, Presentacion,  Cliente, Proveedor, Empleado, Horario, Venta
from .schemas import Datos_Usuarios, CategoriaBase, PresentacionBase,  ClienteBase, ProveedorBase, EmpleadoBase, DetalleVentaBase, VentaBase
from .models import Usuario, Categoria, Presentacion,  Cliente, Proveedor, Empleado, Articulo, Lote, DetalleVenta, Ingreso, DetalleIngreso
from .schemas import Datos_Usuarios, CategoriaBase, PresentacionBase,  ClienteBase, ProveedorBase, EmpleadoBase, IngresoBase, DetalleIngresoBase
from .schemas import ArticuloBase, LoteBase
from .models import Usuario, Categoria, Presentacion,  Cliente, Proveedor, Empleado, Horario
from .schemas import Datos_Usuarios, CategoriaBase, PresentacionBase,  ClienteBase, ProveedorBase, EmpleadoBase, HorarioBase

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

# CRUD para Lote
def get_lotes(db: Session):
     return db.query(Lote).all()

def get_lote_by_id(db: Session, idlote: int):
     return db.query(Lote).filter(Lote.idlote == idlote).first()

def create_lote(db: Session, lote: LoteBase):
     new_lote = Lote(idarticulo=lote.idarticulo, numero_lote=lote.numero_lote, cantidad=lote.cantidad, fecha_vencimiento=lote.fecha_vencimiento)
     db.add(new_lote)
     db.commit()
     db.refresh(new_lote)
     return new_lote

def update_lote(db: Session, idlote: int, lote: LoteBase):
     db_lote = db.query(Lote).filter(Lote.idlote == idlote).first()
     if db_lote:
         db_lote.idarticulo = lote.idarticulo
         db_lote.numero_lote = lote.numero_lote
         db_lote.cantidad = lote.cantidad
         db_lote.fecha_vencimiento = lote.fecha_vencimiento
         db.commit()
         db.refresh(db_lote)
     return db_lote

def delete_lote(db: Session, idlote: int):
     db_lote = db.query(Lote).filter(Lote.idlote == idlote).first()
     if db_lote:
         db.delete(db_lote)
         db.commit()
     return db_lote

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
        disponible = True  # Agregar `disponible` con valor predeterminado
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

def update_empleado_disponible(db: Session, idempleado: int, disponible: bool):
    empleado = db.query(Empleado).filter(Empleado.idempleado == idempleado).first()
    if empleado:
        empleado.disponible = disponible
        db.commit()
        db.refresh(empleado)
        return empleado
    return None

#Crud de Articulo
def get_articulo(db: Session):
    return db.query(Articulo).all()

def get_articulo_by_id(db: Session, idarticulo: int):
    return db.query(Articulo).filter(Articulo.idarticulo == idarticulo).first()

def create_articulo(db: Session, articulo: ArticuloBase):
    new_articulo = Articulo(
        idcategoria=articulo.idcategoria,
        idpresentacion=articulo.idpresentacion,
        codigo=articulo.codigo,
        nombre=articulo.nombre,
        descripcion=articulo.descripcion,
        perecedero=articulo.perecedero
    )
    db.add(new_articulo)
    db.commit()
    db.refresh(new_articulo)
    return new_articulo

def update_articulo(db: Session, idarticulo: int, articulo: ArticuloBase):
    db_articulo = db.query(Articulo).filter(Articulo.idarticulo == idarticulo).first()
    if db_articulo:
        db_articulo.idcategoria = articulo.idcategoria
        db_articulo.idpresentacion = articulo.idpresentacion
        db_articulo.codigo = articulo.codigo
        db_articulo.nombre = articulo.nombre
        db_articulo.descripcion = articulo.descripcion
        db_articulo.perecedero = articulo.perecedero
        db.commit()
        db.refresh(db_articulo)
    return db_articulo

def delete_articulo(db: Session, idarticulo: int):
    db_articulo = db.query(Articulo).filter(Articulo.idarticulo == idarticulo).first()
    if db_articulo:
        db.delete(db_articulo)
        db.commit()
    return db_articulo

#Crud para Horarios
def create_horario(db: Session, horario: HorarioBase):
    db_horario = Horario(**horario.dict())
    db.add(db_horario)
    db.commit()
    db.refresh(db_horario)
    return db_horario

def get_horarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Horario).offset(skip).limit(limit).all()

def get_horario(db: Session, horario_id: int):
    return db.query(Horario).filter(Horario.idhorario == horario_id).first()

def update_horario(db: Session, horario_id: int, horario_update: HorarioBase):
    db_horario = db.query(Horario).filter(Horario.idhorario == horario_id).first()
    if db_horario:
        for key, value in horario_update.dict().items():
            setattr(db_horario, key, value)
        db.commit()
        db.refresh(db_horario)
    return db_horario

def delete_horario(db: Session, horario_id: int):
    db_horario = db.query(Horario).filter(Horario.idhorario == horario_id).first()
    if db_horario:
        db.delete(db_horario)
        db.commit()
    return db_horario

#Crud venta
def create_venta(db: Session, venta: VentaBase):
    db_venta = Venta(**venta.dict())
    db.add(db_venta)
    db.commit()
    db.refresh(db_venta)
    return db_venta

def get_ventas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Venta).offset(skip).limit(limit).all()

def get_venta(db: Session, venta_id: int):
    return db.query(Venta).filter(Venta.idventa == venta_id).first()

def update_venta(db: Session, venta_id: int, venta_update: VentaBase):
    db_venta = db.query(Venta).filter(Venta.idventa == venta_id).first()
    if db_venta:
        for key, value in venta_update.dict().items():
            setattr(db_venta, key, value)
        db.commit()
        db.refresh(db_venta)
    return db_venta

def delete_venta(db: Session, venta_id: int):
    db_venta = db.query(Venta).filter(Venta.idventa == venta_id).first()
    if db_venta:
        db.delete(db_venta)
        db.commit()
    return db_venta

#Crud Detalle_venta
def create_detalle_venta(db: Session, detalle_venta: DetalleVentaBase):
    db_detalle_venta = DetalleVenta(**detalle_venta.dict())
    db.add(db_detalle_venta)
    db.commit()
    db.refresh(db_detalle_venta)
    return db_detalle_venta

def get_detalles_venta(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DetalleVenta).offset(skip).limit(limit).all()

def get_detalle_venta(db: Session, detalle_venta_id: int):
    return db.query(DetalleVenta).filter(DetalleVenta.iddetalle_venta == detalle_venta_id).first()

def update_detalle_venta(db: Session, detalle_venta_id: int, detalle_venta_update: DetalleVentaBase):
    db_detalle_venta = db.query(DetalleVenta).filter(DetalleVenta.iddetalle_venta == detalle_venta_id).first()
    if db_detalle_venta:
        for key, value in detalle_venta_update.dict().items():
            setattr(db_detalle_venta, key, value)
        db.commit()
        db.refresh(db_detalle_venta)
    return db_detalle_venta

def delete_detalle_venta(db: Session, detalle_venta_id: int):
    db_detalle_venta = db.query(DetalleVenta).filter(DetalleVenta.iddetalle_venta == detalle_venta_id).first()
    if db_detalle_venta:
        db.delete(db_detalle_venta)
        db.commit()
    return db_detalle_venta

#Crud Ingreso
def get_ingresos(db: Session):
    return db.query(Ingreso).all()

def get_ingreso_by_id(db: Session, idingreso: int):
    return db.query(Ingreso).filter(Ingreso.idingreso == idingreso).first()

def create_ingreso(db: Session, ingreso: IngresoBase):
    new_ingreso = Ingreso(
        idproveedor=ingreso.idproveedor,
        idusuario=ingreso.idusuario,
        tipo_comprobante=ingreso.tipo_comprobante,
        serie_comprobante=ingreso.serie_comprobante,
        num_comprobante=ingreso.num_comprobante,
        fecha=ingreso.fecha,
        impuesto=ingreso.impuesto
    )
    db.add(new_ingreso)
    db.commit()
    db.refresh(new_ingreso)
    return new_ingreso

def update_ingreso(db: Session, idingreso: int, ingreso: IngresoBase):
    db_ingreso = db.query(Ingreso).filter(Ingreso.idingreso == idingreso).first()
    if db_ingreso:
        db_ingreso.idproveedor = ingreso.idproveedor
        db_ingreso.idusuario = ingreso.idusuario
        db_ingreso.tipo_comprobante = ingreso.tipo_comprobante
        db_ingreso.serie_comprobante = ingreso.serie_comprobante
        db_ingreso.num_comprobante = ingreso.num_comprobante
        db_ingreso.fecha = ingreso.fecha
        db_ingreso.impuesto = ingreso.impuesto
        db.commit()
        db.refresh(db_ingreso)
    return db_ingreso

def delete_ingreso(db: Session, idingreso: int):
    db_ingreso = db.query(Ingreso).filter(Ingreso.idingreso == idingreso).first()
    if db_ingreso:
        db.delete(db_ingreso)
        db.commit()
    return db_ingreso

#Crud Detalle_ingreso
def get_detalles_ingreso(db: Session):
    return db.query(DetalleIngreso).all()

def get_detalle_ingreso_by_id(db: Session, iddetalle_ingreso: int):
    return db.query(DetalleIngreso).filter(DetalleIngreso.iddetalle_ingreso == iddetalle_ingreso).first()

def create_detalle_ingreso(db: Session, detalle_ingreso: DetalleIngresoBase):
    new_detalle_ingreso = DetalleIngreso(
        idingreso=detalle_ingreso.idingreso,
        idproducto=detalle_ingreso.idproducto,
        precio_compra=detalle_ingreso.precio_compra,
        precio_venta=detalle_ingreso.precio_venta,
        stock_inicial=detalle_ingreso.stock_inicial,
        stock_actual=detalle_ingreso.stock_actual,
        fecha_produccion=detalle_ingreso.fecha_produccion,
        fecha_vencimiento=detalle_ingreso.fecha_vencimiento
    )
    db.add(new_detalle_ingreso)
    db.commit()
    db.refresh(new_detalle_ingreso)
    return new_detalle_ingreso

def update_detalle_ingreso(db: Session, iddetalle_ingreso: int, detalle_ingreso: DetalleIngresoBase):
    db_detalle_ingreso = db.query(DetalleIngreso).filter(DetalleIngreso.iddetalle_ingreso == iddetalle_ingreso).first()
    if db_detalle_ingreso:
        db_detalle_ingreso.idingreso = detalle_ingreso.idingreso
        db_detalle_ingreso.idproducto = detalle_ingreso.idproducto
        db_detalle_ingreso.precio_compra = detalle_ingreso.precio_compra
        db_detalle_ingreso.precio_venta = detalle_ingreso.precio_venta
        db_detalle_ingreso.stock_inicial = detalle_ingreso.stock_inicial
        db_detalle_ingreso.stock_actual = detalle_ingreso.stock_actual
        db_detalle_ingreso.fecha_produccion = detalle_ingreso.fecha_produccion
        db_detalle_ingreso.fecha_vencimiento = detalle_ingreso.fecha_vencimiento
        db.commit()
        db.refresh(db_detalle_ingreso)
    return db_detalle_ingreso

def delete_detalle_ingreso(db: Session, iddetalle_ingreso: int):
    db_detalle_ingreso = db.query(DetalleIngreso).filter(DetalleIngreso.iddetalle_ingreso == iddetalle_ingreso).first()
    if db_detalle_ingreso:
        db.delete(db_detalle_ingreso)
        db.commit()
    return db_detalle_ingreso
