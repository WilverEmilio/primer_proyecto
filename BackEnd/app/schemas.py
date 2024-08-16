from pydantic import BaseModel
from typing import Optional
from datetime import date

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
     
     class Config: 
        from_attributes = True

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
