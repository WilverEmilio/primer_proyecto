-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS abarroteria;
USE abarroteria;

-- Tabla Categoria
CREATE TABLE categoria (
    idcategoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(256) NOT NULL
);

-- Tabla Presentacion
CREATE TABLE presentacion (
    idpresentacion INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(256) NOT NULL
);

-- Tabla Proveedor
CREATE TABLE proveedor (
    idproveedor INT AUTO_INCREMENT PRIMARY KEY,
    razon_social VARCHAR(100) NOT NULL,
    tipo_documento VARCHAR(20),
    num_documento VARCHAR(15),
    direccion VARCHAR(70),
    telefono VARCHAR(10),
    email VARCHAR(50),
    url VARCHAR(100)
);

-- Tabla Articulo
CREATE TABLE articulo (
    idarticulo INT AUTO_INCREMENT PRIMARY KEY,
    idcategoria INT,
    idpresentacion INT,
    codigo VARCHAR(50),
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(256) NOT NULL,
    perecedero BOOLEAN NOT NULL,
    FOREIGN KEY (idcategoria) REFERENCES categoria(idcategoria),
    FOREIGN KEY (idpresentacion) REFERENCES presentacion(idpresentacion)
);

-- Tabla Lote (para productos perecederos)
CREATE TABLE lote (
    idlote INT AUTO_INCREMENT PRIMARY KEY,
    idarticulo INT,
    numero_lote VARCHAR(50) NOT NULL,
    cantidad INT NOT NULL,
    fecha_vencimiento DATE,
    FOREIGN KEY (idarticulo) REFERENCES articulo(idarticulo)
);

-- Trigger para verificar si el artículo es perecedero antes de insertar en lote
DELIMITER //

CREATE TRIGGER verificar_lote_perecedero
BEFORE INSERT ON lote
FOR EACH ROW
BEGIN
    DECLARE perecedero BOOLEAN;
    
    -- Verificar si el artículo es perecedero
    SELECT perecedero INTO perecedero FROM articulo WHERE idarticulo = NEW.idarticulo;
    
    -- Si no es perecedero, lanzar un error
    IF perecedero = FALSE THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se puede crear un lote para un producto no perecedero';
    END IF;
END;
//

DELIMITER ;

-- Tabla Cliente
CREATE TABLE cliente (
    idcliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    run_documento VARCHAR(15),
    direccion VARCHAR(70),
    telefono VARCHAR(10),
    email VARCHAR(50)
);

-- Tabla Empleado
CREATE TABLE empleado (
    idempleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    telefono VARCHAR(10),
    direccion VARCHAR(70),
    disponible BOOLEAN NOT NULL
);

-- Tabla Usuario (Relacionada con Empleado)
CREATE TABLE usuario (
    idusuario INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL,
    contrasena VARCHAR(50) NOT NULL,
    rol VARCHAR(20),
    email VARCHAR(50),
    disponible BOOLEAN NOT NULL,
    idempleado INT,
    FOREIGN KEY (idempleado) REFERENCES empleado(idempleado)
);

-- Tabla Horario (Relacionada con Usuario)
CREATE TABLE horario (
    idhorario INT AUTO_INCREMENT PRIMARY KEY,
    idusuario INT,
    dia ENUM('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo') NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    FOREIGN KEY (idusuario) REFERENCES usuario(idusuario)
);

-- Trigger para Verificar Horas Semanales (Usuario)
DELIMITER //

CREATE TRIGGER verificar_horas_semanales
BEFORE INSERT ON horario
FOR EACH ROW
BEGIN
    DECLARE total_horas INT;
    
    -- Calcular las horas que el usuario ya tiene asignadas en la semana
    SELECT IFNULL(SUM(TIMESTAMPDIFF(HOUR, hora_inicio, hora_fin)), 0)
    INTO total_horas
    FROM horario
    WHERE idusuario = NEW.idusuario;

    -- Calcular las horas que se quieren asignar con el nuevo registro
    SET total_horas = total_horas + TIMESTAMPDIFF(HOUR, NEW.hora_inicio, NEW.hora_fin);

    -- Si las horas exceden 40, lanzar un error
    IF total_horas > 40 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El usuario no puede tener más de 40 horas asignadas en la semana';
    END IF;
END;
//

DELIMITER ;

-- Tabla Ingreso
CREATE TABLE ingreso (
    idingreso INT AUTO_INCREMENT PRIMARY KEY,
    idproveedor INT,
    idusuario INT,
    tipo_comprobante VARCHAR(20),
    serie_comprobante VARCHAR(7),
    num_comprobante VARCHAR(10),
    fecha DATE NOT NULL,
    impuesto DECIMAL(4, 2) NOT NULL,
    FOREIGN KEY (idproveedor) REFERENCES proveedor(idproveedor),
    FOREIGN KEY (idusuario) REFERENCES usuario(idusuario)
);

-- Tabla Detalle_Ingreso
CREATE TABLE detalle_ingreso (
    iddetalle_ingreso INT AUTO_INCREMENT PRIMARY KEY,
    idingreso INT,
    idproducto INT,
    precio_compra DECIMAL(10, 2) NOT NULL,
    precio_venta DECIMAL(10, 2) NOT NULL,
    stock_inicial INT NOT NULL,
    stock_actual INT NOT NULL,
    fecha_produccion DATE,
    fecha_vencimiento DATE,
    FOREIGN KEY (idingreso) REFERENCES ingreso(idingreso),
    FOREIGN KEY (idproducto) REFERENCES articulo(idarticulo)
);

-- Tabla Venta
CREATE TABLE venta (
    idventa INT AUTO_INCREMENT PRIMARY KEY,
    idcliente INT,
    idusuario INT,
    tipo_comprobante VARCHAR(20),
    serie_comprobante VARCHAR(7),
    num_comprobante VARCHAR(10),
    fecha DATE NOT NULL,
    impuesto DECIMAL(4, 2) NOT NULL,
    FOREIGN KEY (idcliente) REFERENCES cliente(idcliente),
    FOREIGN KEY (idusuario) REFERENCES usuario(idusuario)
);

-- Tabla Detalle_Venta (Relacionada con Detalle_Ingreso)
CREATE TABLE detalle_venta (
    iddetalle_venta INT AUTO_INCREMENT PRIMARY KEY,
    idventa INT,
    iddetalle_ingreso INT,
    cantidad INT NOT NULL,
    precio_venta DECIMAL(10, 2) NOT NULL,
    descuento DECIMAL(10, 2),
    FOREIGN KEY (idventa) REFERENCES venta(idventa),
    FOREIGN KEY (iddetalle_ingreso) REFERENCES detalle_ingreso(iddetalle_ingreso)
);
