import Extraccion as ex
import pandas as pd

def transformacion_clientes():

    lista_clientes = ex.extraccion_lista_clientes()
    lista_clientes['Fecha de nacimiento'] = pd.to_datetime(lista_clientes['Fecha de nacimiento'], errors='coerce', dayfirst = True).dt.strftime('%Y/%m/%d') 

    #retornar lista de clientes
    return lista_clientes

def transformacion_proveedores():

    lista_proveedores = ex.extraccion_lista_proveedores()
    lista_proveedores['Fecha de última compra'] = pd.to_datetime(lista_proveedores['Fecha de última compra'], errors='coerce', dayfirst = True).dt.strftime('%Y/%m/%d') 

    #retornar lista de proveedores
    return lista_proveedores

def transformacion_grupos():

    lista_grupos = ex.extraccion_lista_grupos()
    #retornar lista de grupos
    return lista_grupos

def transformacion_registros_ventas():

    lista_registros_venta = ex.extraccion_lista_registros_venta()
    lista_registros_venta['Fecha pedido'] = pd.to_datetime(lista_registros_venta['Fecha pedido'], errors='coerce', dayfirst = True).dt.strftime('%Y/%m/%d') 
    lista_registros_venta['Fecha envío'] = pd.to_datetime(lista_registros_venta['Fecha envío'], errors='coerce', dayfirst = True).dt.strftime('%Y/%m/%d') 

    #retornar lista de grupos
    return lista_registros_venta


# lista_grupos = ex.extraccion_lista_grupos()
# print(lista_grupos)
# print("="*100)

# print(lista_clientes.info())
# print("="*100)

# print(lista_clientes_2['Fecha de nacimiento'])
# print("="*100)

# print(transformacion_clientes())
# print("="*100)
# print(transformacion_proveedores())
# print("="*100)
# print(transformacion_grupos())
# print("="*100)
# print(transformacion_registros_ventas())
# print("="*100)