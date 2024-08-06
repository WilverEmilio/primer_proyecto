from sqlalchemy import Column, Integer, String, DateTime
from .conexion import Base

class Usuario(Base): 
    __tablename__ = 'usuarios'
    id_usuario = Column(Integer, primary_key = True, index = True)
    nombre = Column(String(255), index = True)
    cargo = Column(String(255), index = True)
    correo = Column(String(255), index = True)
    contrasena = Column(String(255), index = True)