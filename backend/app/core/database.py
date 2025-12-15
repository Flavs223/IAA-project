""" Módulo de acceso a base de datos.

Este archivo centraliza la creación de conexiones a la base de datos MySQL
del sistema IIA. Su responsabilidad es exclusivamente técnica y forma parte
de la capa de infraestructura del backend.

Funcionamiento general:
- Consume los parámetros de conexión (host, puerto, usuario, contraseña y
  nombre de la base de datos) desde el módulo de configuración de la aplicación.
- Crea y devuelve una conexión activa a MySQL utilizando mysql-connector.
- Maneja errores de conexión para evitar que fallos de base de datos detengan
  la ejecución del sistema.

Decisiones de diseño:
- Este módulo NO lee directamente variables de entorno ni archivos .env.
  La carga de configuración se realiza previamente en el núcleo del sistema.
- Se importan únicamente las variables necesarias de configuración para mantener
  un bajo acoplamiento y facilitar el mantenimiento.
- La función get_db_connection() está pensada para ser reutilizada por repositorios,
  servicios o casos de uso que requieran acceso a la base de datos.

Este enfoque permite:
- Centralizar el acceso a la base de datos.
- Facilitar pruebas y cambios futuros (por ejemplo, pools de conexión).
- Mantener una arquitectura limpia y escalable.
"""

# backend/app/core/database.py

import mysql.connector
from mysql.connector import Error
from backend.app.config.settings import (
    DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME
)



def get_db_connection():
      """ Crea y devuelve una conexión activa a la base de datos MySQL.
      
      Returns:
            mysql.connector.connection.MySQLConnection | None:
            Objeto de conexión si la conexión es exitosa, None si ocurre un error.
      """
      try:
            connection = mysql.connector.connect(
                  host=DB_HOST,
                  port=DB_PORT,
                  user=DB_USER,
                  password=DB_PASSWORD,
                  database=DB_NAME,
            )
            return connection
      
      except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
      return None
