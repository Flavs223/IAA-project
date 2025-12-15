# backend/app/repositories/producto_repository.py
    
    #Repositorio de acceso a datos para la tabla productos (sku_maestro en SQL, ya
    # que en esta se registran los datos de los artículos: nombre, marca, unidad de medida, estado, etc).
    # Encapsula todas las operaciones SQL relacionadas con productos.

from backend.app.core.database import get_db_connection
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
      def create(codigo_sku, nombre_producto, categoria, unidad_medida):
            #OJO: Asegúrate de que los nombres de las columnas coincidan con los de tu tabla SQL
            #OJO2: Esta función asume que la tabla tiene una columna autoincremental para el ID
            #OJO3: Ajusta los parámetros según los campos reales de la tabla sku_maestro
            #Los %s son placeholders para los valores que se insertarán, protegiendo contra inyecciones SQL
            #Estos valores se pasan como una tupla, siempre serán %s para cada valor (int, str, bool, etc)
            query = """
            INSERT INTO sku_maestro
            (codigo_sku, nombre_producto, categoria, unidad_medida)
            VALUES (%s, %s, %s, %s)
            """

            conn = get_db_connection()
            if not conn:
                  return None

            try:
                  cursor = conn.cursor()
                  cursor.execute(
                  query,
                  (codigo_sku, nombre_producto, categoria, unidad_medida)
                  )
                  conn.commit()
                  return cursor.lastrowid
            finally:
                  cursor.close()
                  conn.close()