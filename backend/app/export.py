import csv
import psycopg2

## Exportar datos a CSV
def export_to_csv():
    conn = psycopg2.connect("dbname=etl_db user=admin password=admin host=postgres")
    cur = conn.cursor()
    cur.execute("SELECT * FROM etl_data")
    
    ## ABRE EL ARCHIVO CSV Y ESCRIBE LOS DATOS
    with open("/app/data/recap.csv", "w", newline="") as file:  # Asegurar un path accesible en Docker
        writer = csv.writer(file)
        writer.writerow([desc[0] for desc in cur.description])
        writer.writerows(cur.fetchall())

    cur.close()
    conn.close()
