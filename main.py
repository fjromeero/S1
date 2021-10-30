import pyodbc

try: 
    conexion = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=oracle0.ugr.es;Service Name=practbd.oracle0.ugr.es;User ID=x4276227;Password=x4276227')
    print("Conectado a la base de datos")
    # Aquí continuais vuestro codigo

except Exception as ex:
    print(ex)
finally:
    conexion.close()
    print("Desconectado de la base de datos")