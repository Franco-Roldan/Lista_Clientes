intrucciones = (
    """
        CREATE TABLE if not exists usuario(
            id_user INT PRIMARY KEY AUTO_INCREMENT,
            name_user VARCHAR(50) NOT NULL,
            apel_user VARCHAR(50) NULL,
            mail VARCHAR(100) NOT NULL,
            fecha_nac DATE NOT NULL,
            tel VARCHAR(50) NOT NULL,
            direccion VARCHAR(100) NOT NULL,
            password VARCHAR(150) NOT NULL
        );
    """,
    """
        CREATE TABLE if not exists cliente(
            id_cliente INT PRIMARY KEY AUTO_INCREMENT,
            dni_cliente INT NOT NULL,
            name_cliente VARCHAR(50) NOT NULL,
            apel_cliente VARCHAR(50) NOT NULL,
            CUIT VARCHAR(50) NOT NULL,
            mail VARCHAR(100) NOT NULL,
            tel VARCHAR(50) NOT NULL,
            direccion VARCHAR(100) NOT NULL,
            localidad VARCHAR(100) NOT NULL
        );
    """,
    """
        CREATE TABLE if not exists proveedor(
            id_prov INT PRIMARY KEY AUTO_INCREMENT,
            razon_social INT NOT NULL,
            CUIT VARCHAR(50) NOT NULL,
            mail VARCHAR(100) NOT NULL,
            tel VARCHAR(50) NOT NULL,
            direccion VARCHAR(100) NOT NULL,
            localidad VARCHAR(100) NOT NULL
        );
    """,
    """
        CREATE TABLE if not exists compra_proveedor(
            id_compra INT PRIMARY KEY AUTO_INCREMENT,
            id_prov INT NOT NULL,
            id_user INT NOT NULL,
            codigo_prod INT NOT NULL,
            unidad INT NOT NULL,
            fecha_compra TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            iva VARCHAR(50) NOT NULL,
            precio_unidad FLOAT NOT NULL 
        );
    """,
    """
        CREATE TABLE if not exists venta_cliente(
            id_venta INT PRIMARY KEY AUTO_INCREMENT,
            id_cliente INT NOT NULL,
            id_user INT NOT NULL,
            codigo_prod INT NOT NULL,
            unidad INT NOT NULL,
            fecha_venta TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            iva VARCHAR(50) NOT NULL,
            precio_unidad FLOAT NOT NULL 
        );
    """,
    """
        CREATE TABLE if not exists producto(
            codigo_prod INT PRIMARY KEY AUTO_INCREMENT,
            name_prod VARCHAR(50) NOT NULL,
            marca VARCHAR(50) NOT NULL,
            modelo VARCHAR(50) NOT NULL,
            auto VARCHAR(50) NOT NULL,
            stock INT NOT NULL,
            precio_compra FLOAT NOT NULL,
            iva VARCHAR(50) NOT NULL,
            descripcion VARCHAR(400) NOT NULL
        );
    """
)