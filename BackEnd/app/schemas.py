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