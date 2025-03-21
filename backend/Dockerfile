# Imagen base
FROM python:3.9-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt requirements.txt
COPY app app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Crear directorio para CSV
RUN mkdir -p /app/data

# Exponer el puerto de la API
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "app/main.py"]
