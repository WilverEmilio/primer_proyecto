from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from datetime import datetime

from models import Producto, Usuario, Venta, Inventario
from conexion import SessionLocal, engine, Base
from schemas import Producto as ProductoSchema, Usuario as UsuarioSchema, Venta as VentaSchema, Inventario as InventarioSchema, CrearUsuario, IngresoUsuario

Base.metadata.create_all(bind=engine)

app = FastAPI()

def obtener_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/productos/", response_model=ProductoSchema)
def crear_producto(producto: ProductoSchema, db: Session = Depends(obtener_db)):
    db_producto = Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@app.get("/productos/", response_model=List[ProductoSchema])
def leer_productos(skip: int = 0, limit: int = 100, db: Session = Depends(obtener_db)):
    productos = db.query(Producto).offset(skip).limit(limit).all()
    return productos

@app.get("/productos/{producto_id}", response_model=ProductoSchema)
def leer_producto(producto_id: int, db: Session = Depends(obtener_db)):
    db_producto = db.query(Producto).filter(Producto.id_producto == producto_id).first()
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@app.put("/productos/{producto_id}", response_model=ProductoSchema)
def actualizar_producto(producto_id: int, producto: ProductoSchema, db: Session = Depends(obtener_db)):
    db_producto = db.query(Producto).filter(Producto.id_producto == producto_id).first()
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    for key, value in producto.dict().items():
        setattr(db_producto, key, value)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@app.delete("/productos/{producto_id}", response_model=ProductoSchema)
def eliminar_producto(producto_id: int, db: Session = Depends(obtener_db)):
    db_producto = db.query(Producto).filter(Producto.id_producto == producto_id).first()
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(db_producto)
    db.commit()
    return db_producto

@app.post("/usuarios/", response_model=UsuarioSchema)
def crear_usuario(usuario: CrearUsuario, db: Session = Depends(obtener_db)):
    db_usuario = Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@app.get("/usuarios/", response_model=List[UsuarioSchema])
def leer_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(obtener_db)):
    usuarios = db.query(Usuario).offset(skip).limit(limit).all()
    return usuarios

@app.get("/usuarios/{usuario_id}", response_model=UsuarioSchema)
def leer_usuario(usuario_id: int, db: Session = Depends(obtener_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@app.put("/usuarios/{usuario_id}", response_model=UsuarioSchema)
def actualizar_usuario(usuario_id: int, usuario: UsuarioSchema, db: Session = Depends(obtener_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in usuario.dict().items():
        setattr(db_usuario, key, value)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@app.delete("/usuarios/{usuario_id}", response_model=UsuarioSchema)
def eliminar_usuario(usuario_id: int, db: Session = Depends(obtener_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(db_usuario)
    db.commit()
    return db_usuario

@app.post("/ventas/", response_model=VentaSchema)
def crear_venta(venta: VentaSchema, db: Session = Depends(obtener_db)):
    db_venta = Venta(**venta.dict())
    db.add(db_venta)
    db.commit()
    db.refresh(db_venta)
    return db_venta

@app.get("/ventas/", response_model=List[VentaSchema])
def leer_ventas(skip: int = 0, limit: int = 100, db: Session = Depends(obtener_db)):
    ventas = db.query(Venta).offset(skip).limit(limit).all()
    return ventas

@app.get("/ventas/{venta_id}", response_model=VentaSchema)
def leer_venta(venta_id: int, db: Session = Depends(obtener_db)):
    db_venta = db.query(Venta).filter(Venta.id_venta == venta_id).first()
    if db_venta is None:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return db_venta

@app.put("/ventas/{venta_id}", response_model=VentaSchema)
def actualizar_venta(venta_id: int, venta: VentaSchema, db: Session = Depends(obtener_db)):
    db_venta = db.query(Venta).filter(Venta.id_venta == venta_id).first()
    if db_venta is None:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    for key, value in venta.dict().items():
        setattr(db_venta, key, value)
    db.commit()
    db.refresh(db_venta)
    return db_venta

@app.delete("/ventas/{venta_id}", response_model=VentaSchema)
def eliminar_venta(venta_id: int, db: Session = Depends(obtener_db)):
    db_venta = db.query(Venta).filter(Venta.id_venta == venta_id).first()
    if db_venta is None:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    db.delete(db_venta)
    db.commit()
    return db_venta

@app.post("/inventarios/", response_model=InventarioSchema)
def crear_inventario(inventario: InventarioSchema, db: Session = Depends(obtener_db)):
    db_inventario = Inventario(**inventario.dict())
    db.add(db_inventario)
    db.commit()
    db.refresh(db_inventario)
    return db_inventario

@app.get("/inventarios/", response_model=List[InventarioSchema])
def leer_inventarios(skip: int = 0, limit: int = 100, db: Session = Depends(obtener_db)):
    inventarios = db.query(Inventario).offset(skip).limit(limit).all()
    return inventarios

@app.get("/inventarios/{inventario_id}", response_model=InventarioSchema)
def leer_inventario(inventario_id: int, db: Session = Depends(obtener_db)):
    db_inventario = db.query(Inventario).filter(Inventario.id_inventario == inventario_id).first()
    if db_inventario is None:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return db_inventario

@app.put("/inventarios/{inventario_id}", response_model=InventarioSchema)
def actualizar_inventario(inventario_id: int, inventario: InventarioSchema, db: Session = Depends(obtener_db)):
    db_inventario = db.query(Inventario).filter(Inventario.id_inventario == inventario_id).first()
    if db_inventario is None:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    for key, value in inventario.dict().items():
        setattr(db_inventario, key, value)
    db.commit()
    db.refresh(db_inventario)
    return db_inventario

@app.delete("/inventarios/{inventario_id}", response_model=InventarioSchema)
def eliminar_inventario(inventario_id: int, db: Session = Depends(obtener_db)):
    db_inventario = db.query(Inventario).filter(Inventario.id_inventario == inventario_id).first()
    if db_inventario is None:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    db.delete(db_inventario)
    db.commit()
    return db_inventario

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
