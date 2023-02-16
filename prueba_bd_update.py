import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='Deivid_2020',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia= 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores= ('Brutus', 'wseislabo', 'djbruto@pedrido.com',5)
            cursor.execute(sentencia, valores)
            #conexion.commit() .- al usar with no hace falta declara el commit
            #para varios registros habría q crear la tupla de tuplas,y
            # cambiar el metodo cursor.executemany(sentencia, valoresy
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()