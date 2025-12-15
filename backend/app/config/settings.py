# backend/app/config/settings.py
import os
# Importo el módulo de configuración central para mantener la coherencia de las variables de entorno.
from backend.app.core import setting_core  # ← ESTO ES LO IMPORTANTE
# Lo que hace es cargar las variables de entorno desde el archivo .env
# ubicado en la raíz del proyecto (iia-system). 
# Carga explícita del .env (side-effect controlado)


# =========================
# Configuración general
# =========================

#Nombre de la aplicación
APP_NAME = "IIA - Integra Inventario AWS"

# Entorno de ejecución: development, staging, production
# Es decir, estas variables contienen las variables de entorno cargadas desde el .env
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = ENVIRONMENT == "development"

# =========================
# Helpers internos
# =========================

def _require_env(var_name: str, value: str | None) -> str:
      if not value:
            raise RuntimeError(
                  f"Variable de entorno requerida no definida: {var_name}"
            )
      return value

# =========================
# Base de datos
# =========================

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = _require_env("DB_USER", os.getenv("DB_USER"))
DB_PASSWORD = _require_env("DB_PASSWORD", os.getenv("DB_PASSWORD"))
DB_NAME = _require_env("DB_NAME", os.getenv("DB_NAME"))
