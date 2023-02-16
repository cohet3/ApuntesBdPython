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
            sentencia = 'INSERT INTO persona(nombre, apellido , email)VALUES(%s, %s, %s)'
            valores = (
                ('Carlos', 'Lara', 'lara@pedritro.com'),
                ('Pepito', 'Pepe', 'pepon@pedritro.com'),
                ('paquito', 'chocolater', 'elcholo@pedritro.com')
            )
            cursor.executemany(sentencia, valores)
            #conexion.commit() .- al usar with no hace falta declara el commit
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()