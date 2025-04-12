import sqlite3

#Crea una conexión a la base de datos SQLite
def create_connection(db_name):
    
    connection = None
    try:
        connection = sqlite3.connect(db_name)
        #print(f"Conexión exitosa a {db_name}")
    except sqlite3.Error as e:
        print(f"Error al conectar: {e}")
    return connection

#Cierra la conexión a la base de datos SQLite
def close_connection(connection):
    
    if connection:
        connection.close()
        #print("Conexión cerrada.")

#Prepara la tabla para insertar los datos de la URL
def preparar_tabla_para_insertar_datos_cliente(connection: sqlite3.Connection, table_name):
    
    cursor = connection.cursor()
    # Crear la tabla si no existe
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            ID TEXT PRIMARY KEY,
            NombreCompleto TEXT,
            FechaNacimiento TEXT,
            Direccion TEXT,
            Localidad TEXT,
            Telefono TEXT,
            Correo TEXT,
            FchAlta TEXT,
            Grupo TEXT
        )
    """)
    cursor.execute(f"DELETE FROM {table_name}")
    connection.commit()
    print(f"Se preparo la tabla {table_name} para insertar los datos")
    
#Inserta datos en una tabla de SQLite desde un DataFrame
def insertar_datos_desde_dataframe_cliente(connection: sqlite3.Connection, table_name: str, df_datos):
    
    cursor = connection.cursor()
    
    # Insertar cada registro en la tabla
    for index, record in df_datos.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (ID, NombreCompleto, FechaNacimiento, Direccion, Localidad, Telefono, Correo, FchAlta, Grupo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (record['ID'], record['Nombre completo'], record['Fecha de nacimiento'], record['Dirección'], record['Localidad y Código postal'], record['Teléfono'], record['Correo electrónico'], record['Fecha de alta'], record['Grupo de clientes']))
    
    connection.commit()
    print("Datos insertados correctamente.")

#Prepara la tabla para insertar los datos de la URL
def preparar_tabla_para_insertar_datos_proveedores(connection: sqlite3.Connection, table_name):
    
    cursor = connection.cursor()
    # Crear la tabla si no existe
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            ID TEXT PRIMARY KEY,
            Proveedor TEXT,
            ContactoComercial TEXT,
            Email TEXT,
            Telefono TEXT,
            SaldoPendiente REAL,
            FechaUltimaCompra TEXT
        )
    """)
    cursor.execute(f"DELETE FROM {table_name}")
    connection.commit()
    print(f"Se preparo la tabla {table_name} para insertar los datos")
    
#Inserta datos en una tabla de SQLite desde un DataFrame
def insertar_datos_desde_dataframe_proveedores(connection: sqlite3.Connection, table_name: str, df_datos):
    
    cursor = connection.cursor()
    
    # Insertar cada registro en la tabla
    for index, record in df_datos.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (ID, Proveedor, ContactoComercial, Email, Telefono, SaldoPendiente, FechaUltimaCompra)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (record['ID'], record['Proveedor'], record['Contacto comercial'], record['Email'], record['Teléfono'], record['Saldo pendiente'], record['Fecha de última compra']))
    
    connection.commit()
    print("Datos insertados correctamente.")


#Prepara la tabla para insertar los datos de la URL
def preparar_tabla_para_insertar_datos_registro_ventas(connection: sqlite3.Connection, table_name):
    
    cursor = connection.cursor()
    # Crear la tabla si no existe
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            IdCliente TEXT,
            Zona  TEXT,
            Pais TEXT,
            TipoProducto  TEXT,
            IdProveedor TEXT,
            Prioridad TEXT,
            FechaPedido TEXT,
            IdPedido TEXT,
            FechaEnvio TEXT,
            Unidades REAL,
            PrecioUnitario REAL,
            CosteUnitario REAL,
            ImporteVentaTotal REAL,
            ImporteCosteTotal REAL
        )
    """)
    cursor.execute(f"DELETE FROM {table_name}")
    connection.commit()
    print(f"Se preparo la tabla {table_name} para insertar los datos")
    
#Inserta datos en una tabla de SQLite desde un DataFrame
def insertar_datos_desde_dataframe_registro_ventas(connection: sqlite3.Connection, table_name: str, df_datos):
    
    cursor = connection.cursor()
    
    # Insertar cada registro en la tabla
    for index, record in df_datos.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (IdCliente, Zona, Pais, TipoProducto, IdProveedor, Prioridad, FechaPedido, IdPedido, FechaEnvio, Unidades, PrecioUnitario, CosteUnitario, ImporteVentaTotal, ImporteCosteTotal)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (record['ID Cliente'], record['Zona'], record['País'], record['Tipo de producto'], record['ID Proveedor'], record['Prioridad'], record['Fecha pedido'], record['ID Pedido'], record['Fecha envío'], record['Unidades'], record['Precio Unitario'], record['Coste unitario'], record['Importe venta total'], record['Importe Coste total']))
       
    connection.commit()
    print("Datos insertados correctamente.")

#Prepara la tabla para insertar los datos de la URL
def preparar_tabla_para_insertar_datos_grupos(connection: sqlite3.Connection, table_name):
    
    cursor = connection.cursor()
    # Crear la tabla si no existe
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
                tipo TEXT PRIMARY KEY,
                descripcion  TEXT,
                Estado TEXT
        )
    """)
    cursor.execute(f"DELETE FROM {table_name}")
    connection.commit()
    print(f"Se preparo la tabla {table_name} para insertar los datos")
    
#Inserta datos en una tabla de SQLite desde un DataFrame
def insertar_datos_desde_dataframe_grupos(connection: sqlite3.Connection, table_name: str, df_datos):
    
    cursor = connection.cursor()
    
    # Insertar cada registro en la tabla
    for index, record in df_datos.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (tipo, descripcion, estado)
            VALUES (?, ?, ?)
        """, (record['tipo'], record['descripcion'], record['estado']))
    
    connection.commit()
    print("Datos insertados correctamente.")    