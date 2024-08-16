from pydantic import BaseModel
from typing import Optional
from datetime import date, time
import enum
from decimal import Decimal

# Esquemas de Usuario
class Datos_Usuarios(BaseModel): 
    usuario: str
    contrasena: str
    rol: str
    email: str
    disponible: bool
    idempleado: int
    
    class Config: 
        from_attributes = True
    
class Buscar_Usuario(Datos_Usuarios): 
    idusuario: int

    class Config: 
        from_attributes = True
        
class Login(BaseModel): 
    usuario: str
    contrasena: str

    class Config: 
        from_attributes = True
        
class LoginResponse(BaseModel): 
    message: str
    usuario: str
    token: str
    
    class Config: 
        from_attributes = True

class CategoriaBase(BaseModel):
    nombre: str
    descripcion: str
    
    class Config: 
        from_attributes = True


class Categoria(CategoriaBase):
    idcategoria: int

    class Config: 
        from_attributes = True

class PresentacionBase(BaseModel):
    nombre: str
    descripcion: str
    
    class Config: 
        from_attributes = True



class Presentacion(PresentacionBase):
    idpresentacion: int

    class Config: 
        from_attributes = True

class LoteBase(BaseModel):
     idarticulo: int
     numero_lote: str
     cantidad: int
     fecha_vencimiento: Optional[date] = None



class Lote(LoteBase):
     idlote: int

     class Config: 
         from_attributes = True

# Esquemas de Cliente
class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    run_documento: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None



class Cliente(ClienteBase):
    idcliente: int

    class Config: 
        from_attributes = True
        
class ProveedorBase(BaseModel):
    razon_social: str
    tipo_documento: Optional[str] = None
    num_documento: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    url: Optional[str] = None
    
class Proveedor(ProveedorBase):
    idproveedor: int

    class Config: 
        from_attributes = True
        
class EmpleadoBase(BaseModel):
    nombre: str
    apellidos: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    disponible: bool
    
    class Config: 
        from_attributes = True
        
class Empleado(EmpleadoBase):
    idempleado: int

    class Config: 
        from_attributes = True
        
class ArticuloBase(BaseModel):
    idcategoria: int
    idpresentacion: int
    codigo: str
    nombre: str
    descripcion: str
    perecedero : bool
    
    class Config: 
        from_attributes = True
        
class Articulo(ArticuloBase):
    idarticulo: int

    class Config:
        from_attributes = True

#Esquema Horario
class DiaEnum(str, enum.Enum):
    Lunes = 'Lunes'
    Martes = 'Martes'
    Miércoles = 'Miércoles'
    Jueves = 'Jueves'
    Viernes = 'Viernes'
    Sábado = 'Sábado'
    Domingo = 'Domingo'
    
    
class HorarioBase(BaseModel):
    idusuario: int
    dia: DiaEnum
    hora_inicio: time
    hora_fin: time

    class Config:
        from_attributes = True


class Horario(HorarioBase):
    idhorario: int

    class Config:
        from_attributes = True
#Esquema Venta
class VentaBase(BaseModel):
    idcliente: int
    idusuario: int
    tipo_comprobante: str
    serie_comprobante: str
    num_comprobante: str
    fecha: date
    impuesto: Decimal

    class Config:
        from_attributes = True


class Venta(VentaBase):
    idventa: int

    class Config:
        from_attributes = True

#Esquema Detalle_venta
class DetalleVentaBase(BaseModel):
    idventa: int
    iddetalle_ingreso: int
    cantidad: int
    precio_venta: Decimal
    descuento: Decimal | None = None

    class Config:
        from_attributes = True


class DetalleVenta(DetalleVentaBase):
    iddetalle_venta: int

    class Config:
        from_attributes = True

class IngresoBase(BaseModel):
    idproveedor: int
    idusuario: int
    tipo_comprobante: str
    serie_comprobante: str
    num_comprobante: str
    fecha: date
    impuesto: Decimal

    class Config:
        from_attributes = True
        
class Ingreso(IngresoBase):
    idingreso: int

    class Config:
        from_attributes = True
        
class DetalleIngresoBase(BaseModel):
    idingreso: int
    idproducto: int
    precio_compra: Decimal
    precio_venta: Decimal
    stock_inicial: int
    stock_actual: int
    fecha_produccion: date
    fecha_vencimiento: date

    class Config:
        from_attributes = True
        
class DetalleIngreso(DetalleIngresoBase):
    iddetalle_ingreso: int

    class Config:
        from_attributes = True