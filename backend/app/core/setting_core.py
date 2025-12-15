from pathlib import Path
from dotenv import load_dotenv

def load_env():
    current_path = Path(__file__).resolve()

    for parent in [current_path] + list(current_path.parents):
        env_file = parent / ".env"
        if env_file.exists():
            load_dotenv(env_file)
            return

    raise FileNotFoundError(
        "No se encontró el archivo .env en ninguna carpeta padre"
    )

load_env()
