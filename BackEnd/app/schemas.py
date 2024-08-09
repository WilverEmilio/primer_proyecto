from pydantic import BaseModel
from typing import Optional

class Datos_Usuarios(BaseModel): 
    nombre: str
    cargo: str
    correo: str
    contrasena: str
    
    class Config: 
        from_attributes = True
    
#buscar por id
class Buscar_Usuario(Datos_Usuarios): 
    id_usuario: int

    class Config: 
        from_attributes = True
        
#login
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