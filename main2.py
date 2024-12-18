import pandas as pd
import mysql.connector
from mysql.connector import Error

# PUB_NOMBRES_PJ
def insert_data():
    # Leer el archivo CSV (separado por tabulaciones)
    db_general = pd.read_csv('PUB_NOMBRES_PJ.txt', sep="\t")

    # Reemplazar valores NaN por cadenas vacías
    db_general = db_general.fillna("")

    # Inicializar la variable connection como None para evitar el error de referencia
    connection = None

    try:
        # Conexión a la base de datos MySQL con puerto 3307 y tiempos de espera extendidos
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='taoista',
            password='7340458',
            database='fiama',
            port=3307,
            connection_timeout=3600  # Tiempo de espera para la conexión (1 hora)
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")

            cursor = connection.cursor()

            # Nombre de la tabla en la base de datos
            table_name = 'pub_nombres_pj'

            # Iterar sobre cada fila en el archivo CSV
            for index, row in db_general.iterrows():
                # Crear una tupla con los valores de cada fila
                data = tuple(row)

                # Establecer las columnas de acuerdo a las del CSV
                columns = ', '.join(db_general.columns)  # Las columnas en el CSV
                placeholders = ', '.join(['%s'] * len(db_general.columns))  # Los placeholders para los datos

                # Ajustar la consulta SQL para insertar los datos
                sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                
                # Insertar una fila a la vez
                cursor.execute(sql, data)

                # Confirmar los cambios después de cada inserción
                connection.commit()

                print(f"Fila {index + 1} insertada exitosamente")

    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
    finally:
        # Asegurarse de cerrar la conexión solo si se abrió correctamente
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

# Llamar a la función para insertar los datos
insert_data()
