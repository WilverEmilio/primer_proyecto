from sqlalchemy import Column, Integer, String, Float, Date, Time, TIMESTAMP, ForeignKey, Enum, func
from sqlalchemy.orm import relationship
from .conexion import Base
import enum

class TipoProducto(enum.Enum):
    perecedero = 'perecedero'
    no_perecedero = 'no perecedero'

class DiaSemana(enum.Enum):
    lunes = 'lunes'
    martes = 'martes'
    miercoles = 'miércoles'
    jueves = 'jueves'
    viernes = 'viernes'
    sabado = 'sábado'
    domingo = 'domingo'

class Producto(Base):
    __tablename__ = "productos"
    id_producto = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    tipo = Column(Enum(TipoProducto), nullable=False)
    precio = Column(Float(precision=2), nullable=False)
    stock = Column(Integer, nullable=False)

class Perecedero(Base):
    __tablename__ = "perecederos"
    id_perecedero = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_producto = Column(Integer, ForeignKey('productos.id_producto'))
    fecha_caducidad = Column(Date, nullable=False)
    lote = Column(String(50), nullable=False)
    producto = relationship("Producto")

class NoPerecedero(Base):
    __tablename__ = "noperecederos"
    id_no_perecedero = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_producto = Column(Integer, ForeignKey('productos.id_producto'))
    descripcion = Column(String(255))
    producto = relationship("Producto")

class Inventario(Base):
    __tablename__ = "inventarios"
    id_inventario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_producto = Column(Integer, ForeignKey('productos.id_producto'))
    cantidad = Column(Integer, nullable=False)
    fecha_actualizacion = Column(TIMESTAMP, default=func.now())  # Corregido
    producto = relationship("Producto")

class Venta(Base):
    __tablename__ = "ventas"
    id_venta = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_producto = Column(Integer, ForeignKey('productos.id_producto'))
    cantidad = Column(Integer, nullable=False)
    fecha_venta = Column(TIMESTAMP, default=func.now())  # Corregido
    total = Column(Float(precision=2), nullable=False)
    producto = relationship("Producto")

class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    correo = Column(String(255), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)

class Horario(Base):
    __tablename__ = "horarios"
    id_horario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    dia_semana = Column(Enum(DiaSemana), nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)
    usuario = relationship("Usuario")
