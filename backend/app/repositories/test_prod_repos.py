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

# Función para probar la obtención de un producto por su ID
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
# REVISAR: Permite crear un nuevo SKU en la tabla sku_maestro aun cuando no existe categoria, subcategoria, unidad de medida o marca con los IDs indicados.
def test_create_sku():
      print("=== CREAR NUEVO SKU ===")
      codigo = input("Código SKU: ")
      nombre = input("Nombre del producto: ")
      categoria_id = int(input("Categoria ID: "))
      subcategoria_id = int(input("Subcategoria ID: "))
      unidad_medida_id = int(input("Unidad de medida ID: "))
      marca_id = int(input("Marca ID: "))

      sku_id = SkuMaestroRepository.create(
            codigo_sku=codigo,
            nombre_producto=nombre,
            categoria_id=categoria_id,
            subcategoria_id=subcategoria_id,
            unidad_medida_id=unidad_medida_id,
            marca_id=marca_id
      )

      if sku_id:
            print(f"SKU creado con ID {sku_id}")
      else:
            print("Error al crear SKU")
#Protipo de función para actualizar un producto buscandolo por su id
#De momento te permite que actualices todos los campos de los productos
# Posteriormente se podrá mejorar solo cierto campo que se desee actualizar, no todos.
def test_update_sku():
      print("=== ACTUALIZAR SKU ===")
      id_sku = int(input("ID del SKU a actualizar: "))

      data = {}

      if input("¿Cambiar código? (s/n): ").lower() == 's':
            data["codigo_sku"] = input("Nuevo código SKU: ")

      if input("¿Cambiar nombre? (s/n): ").lower() == 's':
            data["nombre_producto"] = input("Nuevo nombre del producto: ")

      if input("¿Cambiar categoria ID? (s/n): ").lower() == 's':
            data["CATEGORIA_ID"] = int(input("Nueva categoria ID: "))

      if input("¿Cambiar subcategoria ID? (s/n): ").lower() == 's':
            data["SUBCATEGORIA_ID"] = int(input("Nueva subcategoria ID: "))

      if input("¿Cambiar unidad de medida ID? (s/n): ").lower() == 's':
            data["UNIDAD_MEDIDA_ID"] = int(input("Nueva unidad de medida ID: "))

      if input("¿Cambiar marca ID? (s/n): ").lower() == 's':
            data["MARCA_ID"] = int(input("Nueva marca ID: "))

      if input("¿Cambiar estado? (s/n): ").lower() == 's':
            data["estado"] = input("Nuevo estado (activo / inactivo): ")

      if not data:
            print("Nada para actualizar.")
            return

      actualizado = SkuMaestroRepository.update(id_sku, data)
      if actualizado:
            print("SKU actualizado correctamente")
      else:
            print("No se actualizó ningún SKU")
        
if __name__ == "__main__":
      #test_get_all_productos()
      #test_get_producto_by_id()
      #test_create_sku()
      test_update_sku()
      
      