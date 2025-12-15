#Mando a llamar la función get_db_connection del módulo database.py
from backend.app.core.database import get_db_connection

class UsuariosService:

      @staticmethod
      def get_all():
            conn = get_db_connection()
            if not conn:
                  return []

            try:
                  cursor = conn.cursor(dictionary=True)
                  cursor.execute("SELECT * FROM usuarios")
                  return cursor.fetchall()
            finally:
                  cursor.close()
                  conn.close()

      #Función para obtener un usuario por su id
      @staticmethod
      def get_by_id(usuario_id: int):
            conn = get_db_connection()
            if not conn:
                  return None

            try:
                  cursor = conn.cursor(dictionary=True)
                  cursor.execute(
                  "SELECT * FROM usuarios WHERE id_usuario = %s",
                  (usuario_id,)
                  )
                  return cursor.fetchone()
            finally:
                  cursor.close()
                  conn.close()
                  
      @staticmethod
      def es_admin(usuario_id: int) -> bool:
            #print("\n\n####################################\nEstos son los user que son admin\n####################################")
            usuario = UsuariosService.get_by_id(usuario_id)
            if not usuario:
                  return False
            return usuario.get("rol") == "admin"
