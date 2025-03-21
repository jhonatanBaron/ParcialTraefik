from neo4j import GraphDatabase

def extract_data():
    uri = "bolt://neo4j:7687"
    user = "neo4j"
    password = "password"

    driver = GraphDatabase.driver(uri, auth=(user, password))
    with driver.session() as session:
        result = session.run("MATCH (p:Pelicula) RETURN p.id AS id, p.nombre AS nombre, p.calificacion AS calificacion, p.año_lanzamiento AS año_lanzamiento")
        data = [dict(record) for record in result]  # Acceder a los alias correctamente
    driver.close()
    return data
