# Usa la imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo en /app
WORKDIR /app

# Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el contenido de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto 8000 para que la aplicación pueda ser accedida desde fuera del contenedor
EXPOSE 8000

# Comando para ejecutar la aplicación cuando el contenedor se inicia
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]