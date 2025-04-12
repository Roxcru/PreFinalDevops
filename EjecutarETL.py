import Carga as ca
import Transformacion as tr
lst_clientes = tr.transformacion_clientes()
lst_proveedores = tr.transformacion_proveedores()
lst_registros_ventas = tr.transformacion_registros_ventas()


print("="*100)
print("Cargar datos en SQLite")
print("="*100)

ca.carga_cliente(tr.transformacion_clientes())

ca.carga_proveedor(tr.transformacion_proveedores())

ca.carga_registro_ventas(tr.transformacion_registros_ventas())

ca.carga_registro_grupo(tr.transformacion_grupos())

print("="*100)
print("Cargar datos en SQL Server")
print("="*100)

ca.cargar_cliente_sql(tr.transformacion_clientes())

ca.cargar_proveedores_sql(tr.transformacion_proveedores())

ca.cargar_registros_venta_sql(tr.transformacion_registros_ventas())

ca.cargar_registros_grupos_sql(tr.transformacion_grupos())

print("="*100)