from neo4j import GraphDatabase
import psycopg2 # type: ignore
import os

def get_neo4j_connection():
    return GraphDatabase.driver("bolt://neo4j:7687", auth=("neo4j", "password"))

# Conexión a Neo4j
def get_neo4j_session():
    uri = os.getenv("NEO4J_URI", "bolt://neo4j:7687")
    user = os.getenv("NEO4J_USER", "neo4j")
    password = os.getenv("NEO4J_PASSWORD", "password")

    driver = GraphDatabase.driver(uri, auth=(user, password))
    return driver.session()

# Conexión a PostgreSQL
def get_postgres_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "etl_db"),
        user=os.getenv("POSTGRES_USER", "admin"),
        password=os.getenv("POSTGRES_PASSWORD", "admin"),
        host=os.getenv("POSTGRES_HOST", "postgres")
    )
