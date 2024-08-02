from pydantic import BaseModel
from typing import Optional
from datetime import date, time, datetime
from enum import Enum

# Enum para los tipos de productos
class TipoProducto(str, Enum):
    perecedero = "perecedero"
    no_perecedero = "no perecedero"

# Enum para los días de la semana
class DiaSemana(str, Enum):
    lunes = "lunes"
    martes = "martes"
    miercoles = "miércoles"
    jueves = "jueves"
    viernes = "viernes"
    sabado = "sábado"
    domingo = "domingo"

# Esquema para el modelo Producto
class Producto(BaseModel):
    id_producto: Optional[int]
    nombre: str
    tipo: TipoProducto
    precio: float
    stock: int

    class Config:
        from_attributes = True

# Esquema para el modelo Perecedero
class Perecedero(BaseModel):
    id_perecedero: Optional[int]
    id_producto: int
    fecha_caducidad: date
    lote: str

    class Config:
        from_attributes = True

# Esquema para el modelo NoPerecedero
class NoPerecedero(BaseModel):
    id_no_perecedero: Optional[int]
    id_producto: int
    descripcion: Optional[str]

    class Config:
        from_attributes = True

# Esquema para el modelo Inventario
class Inventario(BaseModel):
    id_inventario: Optional[int]
    id_producto: int
    cantidad: int
    fecha_actualizacion: Optional[datetime]

    class Config:
        from_attributes = True

# Esquema para el modelo Venta
class Venta(BaseModel):
    id_venta: Optional[int]
    id_producto: int
    cantidad: int
    fecha_venta: Optional[datetime]
    total: float

    class Config:
        from_attributes = True

# Esquema para el modelo Usuario
class Usuario(BaseModel):
    id_usuario: Optional[int]
    nombre: str
    correo: str
    contrasena: str

    class Config:
        from_attributes = True

# Esquema para el modelo Horario
class Horario(BaseModel):
    id_horario: Optional[int]
    id_usuario: int
    dia_semana: DiaSemana
    hora_inicio: time
    hora_fin: time

    class Config:
        from_attributes = True

# Esquema para crear un nuevo usuario (sin id_usuario)
class CrearUsuario(BaseModel):
    nombre: str
    correo: str
    contrasena: str

    class Config:
        from_attributes = True

# Esquema para la autenticación de usuarios (solo usuario y contrasena)
class IngresoUsuario(BaseModel):
    correo: str
    contrasena: str

    class Config:
        from_attributes = True
