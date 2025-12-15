from backend.app.repositories.repos_user import UsuariosService

usuarios = UsuariosService.get_all()

"""if usuarios:
      print("Usuarios encontrados:")
      #Ciclo for para imprimir cada usuario
      for u in usuarios:
            print("\n",u)
            
else:
    print("No hay usuarios o no se pudo conectar")
#Llama a la clase UsuariosService y a la función get_all para imrimir todos los usuarios
usuarios = UsuariosService.get_all()
print("\n-------------------------------------------------")
print("Lista de usuarios:")
print("\n-------------------------------------------------")      
"""
print(usuarios)
print("\n-------------------------------------------------")

if usuarios:
      #Obtengo el id del primer usuario
      print("Usuario encontrado:\n")
      uid = usuarios[0]["id_usuario"]
      print("Es admin:", UsuariosService.es_admin(uid))
