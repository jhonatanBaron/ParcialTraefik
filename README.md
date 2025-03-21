# ParcialTraefik
Creado por Jhonatan Steven Baron Suarez
##

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- (Opcional) [Neo4j Desktop](https://neo4j.com/download/) y [PostgreSQL](https://www.postgresql.org/download/) para pruebas locales.


## Clonar el Repositorio
git clone https://github.com/jhonatanBaron/ParcialTraefik.git && cd ParcialTraefik
#ubicate en la rama main
##ubicate en: 
cd ParcialTraefik/ParcialTraefik


##crea la red  de DOcker
docker network create etl_network || true

##construye y levanta los contenedores
docker-compose up -d --build
 ## verifica los contenedores activos
 docker ps

#####Accede a los Servicios
-Traefik Dashboard → http://localhost:8080
-Neo4j → http://neo4j.localhost (Usuario: neo4j, Contraseña: password)
-PostgreSQL → Host: postgresql.localhost, Usuario: admin, Contraseña: admin, DB: etl_db, Puerto: 5432
-API ETL → curl http://localhost/jhonatan-baron/


#####Detener y limpiar los contendores
-docker-compose down;
-docker system prune -a
