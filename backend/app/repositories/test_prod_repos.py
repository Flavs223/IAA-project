# backend/app/repositories/test_producto_repos.py
"""Este archivo es para probar las funciones del repositorio de productos.
(Tabla en SQL: sku_maestro)"""

from backend.app.repositories.producto_repository import SkuMaestroRepository


# Prueba para obtener todos los productos
def test_get_all_productos():
      print("Probando obtención de todos los productos...")
      productos = SkuMaestroRepository.get_all()

      if not productos:
            print("No hay productos o no se pudo conectar")
            return

      print("Listado de productos:")
      for producto in productos:
            print(producto)


def test_get_producto_by_id():
      producto_id= int(input("ID del SKU a buscar: "))
      #producto_id = 100  # AJUSTA a un ID que exista en tu BD
      producto = SkuMaestroRepository.get_by_id(producto_id)

      if not producto:
            print("\n---------------------------------------------")
            print(f"No se encontró el producto con ID {producto_id}")
      else:
            print("Producto encontrado:")
            print(producto)

##Función para probar la creación de un nuevo producto
def test_create_sku():
      #Crear función para crear un SKU en automático con los datos de la tabla. Usaré el SELECT eso es seguro para un norte
      codigo = input("Código SKU: ")
      nombre = input("Nombre del producto: ")
      categoria = input("Categoría: ")
      unidad = input("Unidad de medida: ")

      sku_id = SkuMaestroRepository.create(
            codigo_sku=codigo,
            nombre_producto=nombre,
            categoria=categoria,
            unidad_medida=unidad
      )

      if sku_id:
            print(f"SKU creado con ID {sku_id}")
      else:
            print("Error al crear SKU")

#Protipo de función para actualizar un producto buscandolo por su id
#De momento te permite que actualices todos los campos de los productos
# Posteriormente se podrá mejorar solo cierto campo que se desee actualizar, no todos.
def test_update_sku():
      id_sku = int(input("ID del SKU a actualizar: "))
      codigo = input("Nuevo código SKU: ")
      nombre = input("Nuevo nombre del producto: ")
      categoria = input("Nueva categoría: ")
      unidad = input("Nueva unidad de medida: ")
      estado = input("Estado (activo / inactivo): ")

      actualizado = SkuMaestroRepository.update(
            id_sku,
            codigo,
            nombre,
            categoria,
            unidad,
            estado
      )

      if actualizado:
            print("SKU actualizado correctamente")
      else:
            print("No se actualizó ningún SKU")


if __name__ == "__main__":
      #test_get_all_productos()
      test_get_producto_by_id()
      #test_create_sku()
      #test_update_sku()
      
      