# backend/app/repositories/producto_repository.py
    
    #Repositorio de acceso a datos para la tabla productos (sku_maestro en SQL, ya
    # que en esta se registran los datos de los artículos: nombre, marca, unidad de medida, estado, etc).
    # Encapsula todas las operaciones SQL relacionadas con productos.
from backend.app.core.database import get_db_connection
#Excepciónes de MySQL
import mysql.connector
from mysql.connector import IntegrityError, Error


class SkuMaestroRepository:

      #Devuelve todos los productos en la base de datos
      @staticmethod
      def get_all():
            query = "SELECT * FROM sku_maestro"
            print("\nEjecutando consulta para obtener todos los productos...\n")
            conn = get_db_connection()
            
            if not conn:
                  print("No se pudo establecer conexión a la base de datos.")
                  return []

            try:
                  print("Conexión establecida. Ejecutando consulta...")
                  cursor = conn.cursor(dictionary=True)
                  cursor.execute(query)
                  return cursor.fetchall()
            finally:
                  print("Cerrando conexión a la base de datos...")
                  cursor.close()
                  conn.close()

      #Devuelve un producto por su id
      @staticmethod
      def get_by_id(producto_id):
            query = "SELECT * FROM sku_maestro WHERE id_sku = %s"

            conn = get_db_connection()
            if not conn:
                  return None

            try:
                  cursor = conn.cursor(dictionary=True)
                  cursor.execute(query, (producto_id,))
                  return cursor.fetchone()
            finally:
                  cursor.close()
                  conn.close()

      @staticmethod
      def create(
            codigo_sku,
            nombre_producto,
            categoria_id,
            subcategoria_id,
            unidad_medida_id,
            marca_id,
            estado="activo"
            ):
            query = """
            INSERT INTO sku_maestro
            (
                  codigo_sku,
                  nombre_producto,
                  CATEGORIA_ID,
                  SUBCATEGORIA_ID,
                  UNIDAD_MEDIDA_ID,
                  MARCA_ID,
                  estado
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            conn = get_db_connection()
            if not conn:
                  return None

            try:
                  cursor = conn.cursor()
                  cursor.execute(
                        query,
                        (
                        codigo_sku,
                        nombre_producto,
                        categoria_id,
                        subcategoria_id,
                        unidad_medida_id,
                        marca_id,
                        estado
                        )
                  )
                  conn.commit()
                  return cursor.lastrowid
            finally:
                  cursor.close()
                  conn.close()

      #Nueva función para actualizar un producto por su id
      @staticmethod
      def update(id_sku: int, data: dict) -> bool:
            """
            Actualiza un SKU existente en la tabla sku_maestro.
            Retorna True si se actualizó al menos un registro, False en caso contrario.
            """

            if not data:
                  return False

            # Lista blanca de campos permitidos
            allowed_fields = {
                  "codigo_sku": "CODIGO_SKU",
                  "nombre_producto": "NOMBRE_PRODUCTO",
                  "categoria_id": "CATEGORIA_ID",
                  "subcategoria_id": "SUBCATEGORIA_ID",
                  "unidad_medida_id": "UNIDAD_MEDIDA_ID",
                  "marca_id": "MARCA_ID",
                  "estado": "ESTADO",
            }

            fields = []
            values = []

            for key, value in data.items():
                  if key not in allowed_fields:
                        continue  # ignora campos no permitidos

                  fields.append(f"{allowed_fields[key]} = %s")
                  values.append(value)

            if not fields:
                  return False

            query = f"""
                  UPDATE sku_maestro
                  SET {', '.join(fields)}
                  WHERE id_sku = %s
            """

            values.append(id_sku)

            try:
                  connection = get_db_connection()
                  cursor = connection.cursor()
                  cursor.execute(query, tuple(values))
                  connection.commit()

                  return cursor.rowcount > 0

            except mysql.connector.IntegrityError as e:
                  print(f"Error de integridad (FK): {e}")
                  return False

            except Exception as e:
                  print(f"Error inesperado en update SKU: {e}")
                  return False

            finally:
                  try:
                        cursor.close()
                        connection.close()
                  except Exception:
                        pass
