from sqlalchemy import Column, Integer, String, Date, Time, Enum, ForeignKey, Boolean, Decimal
from sqlalchemy.orm import relationship
from .conexion import Base

# Modelo de Usuario
class Usuario(Base):
    __tablename__ = 'usuario'
    idusuario = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(50), index=True)
    contrasena = Column(String(512), index=True)
    rol = Column(String(20), index=True)
    email = Column(String(255), index=True)
    disponible = Column(Boolean, nullable=False, default=True)
    idempleado = Column(Integer, ForeignKey('empleado.idempleado'))

# Modelo de Categoria
class Categoria(Base):
    __tablename__ = 'categoria'
    idcategoria = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(256), nullable=False)

# Modelo de Presentacion
class Presentacion(Base):
    __tablename__ = 'presentacion'
    idpresentacion = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(256), nullable=False)

# # Modelo de Lote
# class Lote(Base):
#     __tablename__ = 'lote'
#     idlote = Column(Integer, primary_key=True, index=True)
#     idarticulo = Column(Integer, ForeignKey('articulo.idarticulo'))
#     numero_lote = Column(String(50), nullable=False)
#     cantidad = Column(Integer, nullable=False)
#     fecha_vencimiento = Column(Date, nullable=True)

#     # Relación con el modelo Articulo
#     articulo = relationship("Articulo", back_populates="lotes")

# Modelo de Cliente
class Cliente(Base):
    __tablename__ = 'cliente'
    idcliente = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    run_documento = Column(String(15), nullable=True)
    direccion = Column(String(70), nullable=True)
    telefono = Column(String(10), nullable=True)
    email = Column(String(50), nullable=True)

# Modelo de Proveedor
class Proveedor(Base):
    __tablename__ = 'proveedor'
    idproveedor = Column(Integer, primary_key=True, index=True)
    razon_social = Column(String(100), nullable=False)
    tipo_documento = Column(String(20), nullable=True)
    num_documento = Column(String(15), nullable=True)
    direccion = Column(String(70), nullable=True)
    telefono = Column(String(10), nullable=True)
    email = Column(String(50), nullable=True)
    url = Column(String(100), nullable=True)
    
# Modelo de Empleado
class Empleado(Base):
    __tablename__ = 'empleado'
    idempleado = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    telefono = Column(String(10), nullable=True)
    direccion = Column(String(70), nullable=True)
    disponible = Column(Boolean, nullable=False, default=True)

#Modelo Horario
class Horario(Base):
    __tablename__ = "horario"
    
    idhorario = Column(Integer, primary_key=True, index=True)
    idusuario = Column(Integer, ForeignKey('usuario.idusuario'))
    dia = Column(Enum('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'), nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)
    
    usuario = relationship("Usuario", back_populates="horarios")

#Modelo Venta
class Venta(Base):
    __tablename__ = "venta"
    
    idventa = Column(Integer, primary_key=True, index=True)
    idcliente = Column(Integer, ForeignKey('cliente.idcliente'))
    idusuario = Column(Integer, ForeignKey('usuario.idusuario'))
    tipo_comprobante = Column(String(20))
    serie_comprobante = Column(String(7))
    num_comprobante = Column(String(10))
    fecha = Column(Date, nullable=False)
    impuesto = Column(Decimal(4, 2), nullable=False)
    
    cliente = relationship("Cliente", back_populates="ventas")
    usuario = relationship("Usuario", back_populates="ventas")
