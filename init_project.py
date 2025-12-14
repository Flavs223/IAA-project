from pathlib import Path

BASE_DIR = Path("iia-system")
# Definir las carpetas y archivos a crear
folders = [
    "backend/app/config",
    "backend/app/core",
    "backend/app/api",
    "backend/app/schemas",
    "backend/app/utils",
    "backend/tests",
    "frontend",
    "docs",
    "scripts",
]
# Archivos con contenido inicial
files = {
    "backend/app/main.py": "",
    "backend/README.md": "# Backend IIA\n",
    "README.md": "# IIA System\n", # Archivo README principal
    ".gitignore": ".venv/\n__pycache__/\n.env\n*.pyc\n.vscode/\n"
}

def create_structure():
      # Crear las carpetas
      for folder in folders:
            # Une la ruta base con la carpeta y crea la carpeta.
            #El "/" es un operador para dividir objetos Path, actua como un join inteligente.c
            path = BASE_DIR / folder
            path.mkdir(parents=True, exist_ok=True)
      
      # Crear los archivos con contenido inicial si no existen 
      # ya para evitar sobreescritura accidental de datos previos 
      for file, content in files.items():
            path = BASE_DIR / file
            path.parent.mkdir(parents=True, exist_ok=True)
            if not path.exists():
                  path.write_text(content, encoding="utf-8")

      # Mensaje de confirmación en console
      print("✔ Estructura del proyecto creada correctamente")

if __name__ == "__main__":
    create_structure()
