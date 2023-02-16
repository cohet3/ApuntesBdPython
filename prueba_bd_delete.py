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
            sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            entrada = input('Proporciona el id:persona a eliminar: ')
            valores = (entrada,)
            cursor.execute(sentencia, valores)
            #conexion.commit() .- al usar with no hace falta declara el commit
            #para varios registros habría q crear la tupla de tuplas,y
            # cambiar el metodo cursor.executemany(sentencia, valores) en las sentencia habría q cambiar el = por in
            #y en valores = (tuple(entrada.split(',')),)
            registros_borrados = cursor.rowcount
            print(f'Registros Borrados: {registros_borrados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()