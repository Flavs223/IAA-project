# backend/app/repositories/test_producto_repo.py
"""Este archivo es para probar las funciones del repositorio de productos.
(Tabla en SQL: sku_maestro)"""

from backend.app.repositories.producto_repository import ProductoRepository


# Prueba para obtener todos los productos
def test_get_all_productos():
      print("Probando obtención de todos los productos...")
      productos = ProductoRepository.get_all()

      if not productos:
            print("No hay productos o no se pudo conectar")
            return

      print("Listado de productos:")
      for producto in productos:
            print(producto)


def test_get_producto_by_id():
      producto_id = 100  # AJUSTA a un ID que exista en tu BD
      producto = ProductoRepository.get_by_id(producto_id)

      if not producto:
            print("\n---------------------------------------------")
            print(f"No se encontró el producto con ID {producto_id}")
      else:
            print("Producto encontrado:")
            print(producto)


if __name__ == "__main__":
    test_get_all_productos()
    test_get_producto_by_id()
