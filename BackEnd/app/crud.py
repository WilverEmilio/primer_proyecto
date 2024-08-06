from sqlalchemy.orm import Session


from .models import Usuario
from .schemas import Datos_Usuarios

def get_usuarios(db: Session):
    return db.query(Usuario).all()

def get_usuario_by_id(db: Session, id_usuario: int):
    return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()

def get_usur_by_name(db: Session, nombre: str):
    return db.query(Usuario).filter(Usuario.nombre == nombre).first()

def create_usuario(db: Session, usuario: Datos_Usuarios):
    new_user = Usuario(nombre=usuario.nombre, cargo=usuario.cargo, correo=usuario.correo, contrasena=usuario.contrasena)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
