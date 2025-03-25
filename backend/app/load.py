import psycopg2
import json

def load_data(data):
    conn = psycopg2.connect("dbname=etl_db user=admin password=admin host=postgres")
    cur = conn.cursor()

    for movie in data:
        cur.execute("""
            INSERT INTO etl_data (id, nombre_formateado, categoria_calificacion, decada, puntuacion_ajustada, fecha_procesamiento)
            VALUES (%s, %s, %s, %s, %s, CURRENT_DATE)
        """, (movie["id"], movie["nombre_formateado"], movie["categoria_calificacion"], movie["decada"], movie["puntuacion_ajustada"]))

    conn.commit()
    cur.close()
    conn.close()
    
def load_data_from_file(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    load_data(data)

# Llamada a la función con la ruta del archivo
load_data_from_file('/home/jhona/Documentos/ParcialTraefik/Data/dataset_a_peliculas')