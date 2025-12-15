#Del archivo "database.py" importo la función get_db_connection para probar la conexión a la base de datos.
from backend.app.config.settings import DB_USER, DB_PASSWORD

print("DB_USER:", DB_USER)
print("DB_PASSWORD:", DB_PASSWORD)
