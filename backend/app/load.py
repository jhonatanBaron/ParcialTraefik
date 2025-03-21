import psycopg2

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
