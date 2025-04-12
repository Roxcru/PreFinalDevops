#improtación de pandas
import pandas as pd
import pathlib
import numpy as np

def extraccion_lista_clientes():
    ruta_cliente_csv = f'{pathlib.Path(__file__).parents[0]}/1.Datos/ListaClientes.csv'
    #cargar lista de clientes
    lista_clientes = pd.read_csv(ruta_cliente_csv, sep = ';')
    
    return lista_clientes

def extraccion_lista_proveedores():
    ruta_proveedor_json = f'{pathlib.Path(__file__).parents[0]}/1.Datos/ListaProveedores.json'
    #Cargar lista de proveedores
    lista_proveedores = pd.read_json(ruta_proveedor_json, lines=True)

    return lista_proveedores

def extraccion_lista_grupos():
    ruta_grupo_excel = f'{pathlib.Path(__file__).parents[0]}/1.Datos/GrupoClientes.xml'
    #Cargar lista de grupos
    lista_grupos = pd.read_xml(ruta_grupo_excel)

    return lista_grupos

def extraccion_lista_registros_venta():
    ruta_cliente_csv = f'{pathlib.Path(__file__).parents[0]}/1.Datos/RegistroVentas.csv'
    #cargar lista de clientes
    lista_clientes = pd.read_csv(ruta_cliente_csv, sep = ';')

    return lista_clientes

# print(extraccion_lista_clientes())
# print("="*100)
# print(extraccion_lista_proveedores())
# print("="*100)
# print(extraccion_lista_grupos())
# print("="*100)
# print(extraccion_lista_registros_venta())
# print("="*100)