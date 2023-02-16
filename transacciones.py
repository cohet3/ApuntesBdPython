import psycopg2 as bd

conexion = bd.connect(
    user='postgres',
    password='Deivid_2020',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VAlUES (%s,%s,%s)'
            valores = ('Doble', 'Cerveza', 'friajaja@gmail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Carls', 'DONcosta', 'romerogil@gmail.com', 11)
            cursor.execute(sentencia, valores)
except Exception as e:
    print(f'Ocurrio un error: se hizo rollback {e}')
finally:
    conexion.close()
print('TErmina la transaccion se hizo commit')
