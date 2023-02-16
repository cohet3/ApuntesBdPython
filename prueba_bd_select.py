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
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            # llaves_primarias = ((1,2,3),)
            entrada= input('Proporciona los id/s a buscar (separado por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)
            #id_persona = input('Proporciona el id_persona: ')
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()