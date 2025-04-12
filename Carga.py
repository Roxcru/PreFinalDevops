import GestionSQLite as gs
import pandas as pd

#SQLite

def carga_cliente(df_datos):
    #Creamos una conexion a la base de datos
    base_datos = 'base_ventas.db'
    tabla = 'cliente'
    conexion = gs.create_connection(base_datos)

    #Verificamos que la conexion se ha realizado
    if conexion:

        #Verificamos que el dataframe no se encuentre vacio
        if df_datos is not None:

            #Creamos la tabla en la base de datos
            gs.preparar_tabla_para_insertar_datos_cliente(conexion, tabla)

            #Insertamos los registros en la tabla creada
            gs.insertar_datos_desde_dataframe_cliente(conexion, tabla, df_datos)
        
        #Cerramos la conexion a la base de datos
        gs.close_connection(conexion)

def carga_proveedor(df_datos):
    #Creamos una conexion a la base de datos
    base_datos = 'base_ventas.db'
    tabla = 'proveedor'
    conexion = gs.create_connection(base_datos)

    #Verificamos que la conexion se ha realizado
    if conexion:

        #Verificamos que el dataframe no se encuentre vacio
        if df_datos is not None:

            #Creamos la tabla en la base de datos
            gs.preparar_tabla_para_insertar_datos_proveedores(conexion, tabla)

            #Insertamos los registros en la tabla creada
            gs.insertar_datos_desde_dataframe_proveedores(conexion, tabla, df_datos)
        
        #Cerramos la conexion a la base de datos
        gs.close_connection(conexion)

def carga_registro_ventas(df_datos):
    #Creamos una conexion a la base de datos
    base_datos = 'base_ventas.db'
    tabla = 'registroVentas'
    conexion = gs.create_connection(base_datos)

    #Verificamos que la conexion se ha realizado
    if conexion:

        #Verificamos que el dataframe no se encuentre vacio
        if df_datos is not None:

            #Creamos la tabla en la base de datos
            gs.preparar_tabla_para_insertar_datos_registro_ventas(conexion, tabla)

            #Insertamos los registros en la tabla creada
            gs.insertar_datos_desde_dataframe_registro_ventas(conexion, tabla, df_datos)
        
        #Cerramos la conexion a la base de datos
        gs.close_connection(conexion)

def carga_registro_grupo(df_datos):
    #Creamos una conexion a la base de datos
    base_datos = 'base_ventas.db'
    tabla = 'grupos'
    conexion = gs.create_connection(base_datos)

    #Verificamos que la conexion se ha realizado
    if conexion:

        #Verificamos que el dataframe no se encuentre vacio
        if df_datos is not None:

            #Creamos la tabla en la base de datos
            gs.preparar_tabla_para_insertar_datos_grupos(conexion, tabla)

            #Insertamos los registros en la tabla creada
            gs.insertar_datos_desde_dataframe_grupos(conexion, tabla, df_datos)
        
        #Cerramos la conexion a la base de datos
        gs.close_connection(conexion)
