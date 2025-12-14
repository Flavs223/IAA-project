# Librería para manejar rutas y variables de entorno  
from pathlib import Path
# Librería para cargar variables de entorno desde un archivo .env
from dotenv import load_dotenv
# Librería para interactuar con el sistema operativo
import os

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parents[3]

# Cargar variables de entorno desde .env
# El "BASE_DIR" evita rutas hardcodeadas
load_dotenv(BASE_DIR / ".env")

# Configuración de base de datos
# El "os.getenv" obtiene el valor de una variable de entorno,
# si no existe, puede asignar un valor por defecto.   
DB_HOST = os.getenv("DB_HOST", "localhost") # Valor por defecto localhost
DB_PORT = int(os.getenv("DB_PORT", 3306)) # Valor por defecto 3306
DB_USER = os.getenv("DB_USER") # Usuario de la base de datos
DB_PASSWORD = os.getenv("DB_PASSWORD") # Contraseña de la base de datos
DB_NAME = os.getenv("DB_NAME") # Nombre de la base de datos
