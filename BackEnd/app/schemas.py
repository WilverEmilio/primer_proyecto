from pydantic import BaseModel
from typing import Optional
from datetime import date

# Esquemas de Usuario
class Datos_Usuarios(BaseModel): 
    nombre: str
    cargo: str
    correo: str
    contrasena: str
    
    class Config: 
        from_attributes = True
    
class Buscar_Usuario(Datos_Usuarios): 
    id_usuario: int

    class Config: 
        from_attributes = True
        
class Login(BaseModel): 
    nombre: str
    contrasena: str

    class Config: 
        from_attributes = True
        
class LoginResponse(BaseModel): 
    nombre: str
    token: str
    
    class Config: 
        from_attributes = True

class CategoriaBase(BaseModel):
    nombre: str
    descripcion: str

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    idcategoria: int

    class Config:
        orm_mode = True

class PresentacionBase(BaseModel):
    nombre: str
    descripcion: str

class PresentacionCreate(PresentacionBase):
    pass

class Presentacion(PresentacionBase):
    idpresentacion: int

    class Config:
        orm_mode = True

class LoteBase(BaseModel):
    idarticulo: int
    numero_lote: str
    cantidad: int
    fecha_vencimiento: Optional[date] = None

class LoteCreate(LoteBase):
    pass

class Lote(LoteBase):
    idlote: int

    class Config:
        orm_mode = True

# Esquemas de Cliente
class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    run_documento: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    idcliente: int

    class Config:
        orm_mode = True

class ProveedorBase(BaseModel):
    razon_social: str
    tipo_documento: Optional[str] = None
    num_documento: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    url: Optional[str] = None

class ProveedorCreate(ProveedorBase):
    pass

class Proveedor(ProveedorBase):
    idproveedor: int

    class Config:
        orm_mode = True
