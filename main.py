import pandas as pd

# ? pip install pandas openpyxl

def get_data_neuma():
    db_general = pd.read_excel('neuma_db.xlsx')

    print(db_general.head())




def get_data_main():
    db_general = pd.read_csv('PUB_NOMBRES_PJ.txt', sep="\t")

    # Crear la nueva columna "RUT_2" concatenando el valor de "rut" con un string
    db_general['codigo_sn'] = 'CN'+db_general['RUT'].astype(str) + '-' +db_general['DV']

    # Seleccionar solo los primeros 5 registros
    data_limited = db_general.head(5)

    # Exportar a un archivo Excel
    output_file = "archivo_actualizado.xlsx"
    data_limited.to_excel(output_file, index=False, engine="openpyxl")


    # print(pb_nombre.head())
    print('terminado.........')

def demo():
    # Leer el archivo de texto (PUB_NOMBRES_PJ.txt)
    db_general = pd.read_csv('PUB_NOMBRES_PJ.txt', sep="\t")

    # Crear la nueva columna "codigo_sn" concatenando el valor de "RUT" y "DV"
    db_general['codigo_sn'] = 'CN' + db_general['RUT'].astype(str) + '-' + db_general['DV']

    # Leer el archivo Excel (neuma_db.xlsx)
    db_neuma = pd.read_excel('neuma_db.xlsx')

    # Eliminar espacios extras en los nombres de las columnas

    # Limpiar valores de 'nombre_sn' eliminando comillas dobles y espacios adicionales

    # Filtrar registros donde 'FECHA_INICIO_VIG' y 'FECHA_TG_VIG' no sean vacíos
    db_general = db_general.loc[
        (db_general['FECHA_INICIO_VIG'].notna()) & (db_general['FECHA_INICIO_VIG'] != '') &
        (db_general['FECHA_TG_VIG'].notna()) & (db_general['FECHA_TG_VIG'] != '')
    ]

    # Realizar el merge para incluir 'codigo_sn' y 'nombre_sn'
    merged_data = pd.merge(
        db_general[['codigo_sn', 'FECHA_INICIO_VIG', 'FECHA_TG_VIG', 'RAZON_SOCIAL']],
        db_neuma[['codigo_sn', 'nombre_sn']],
        on='codigo_sn',
        how='left'
    )

    # Reorganizar las columnas para que 'nombre_sn' esté al lado de 'codigo_sn'
    columns_order = ['codigo_sn', 'RAZON_SOCIAL', 'FECHA_INICIO_VIG', 'FECHA_TG_VIG']
    merged_data = merged_data[columns_order]

   

    # Seleccionar solo las primeras 10 filas para pruebas
    data_limited = merged_data.head(10)

    # Exportar a un archivo Excel
    output_file = "archivo_actualizado.xlsx"
    merged_data.to_excel(output_file, index=False, engine="openpyxl")

    print('Exportación a Excel completada.')
    print('Archivo generado: ', output_file)

demo()