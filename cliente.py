#Elaborado por Duban Ferney Ramírez Suárez

#Importo las librerías a utilizar
from socket import *

#Creo conexión al servidor
def conectar_servidor(host, puerto):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((host, puerto))
    return s

#Función permite enviar comandos al servidor
def enviar_comando(s, comando):
    s.send(comando.encode('utf-8'))
    respuesta = s.recv(1024).decode('utf-8')
    print(respuesta)

#Función principal
def main():
    #En host establezco la dirección ip que establecí en el servidor: 127.0.0.1 o localhost
    host = '127.0.0.1'
    #En puerto establezco el mismo puerto que se habilitó en el servidor
    puerto = 8089
    s = conectar_servidor(host, puerto)


    while True:
        #Se muestra las opciones que se pueden utilizar
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        #Una vez el cliente ha selecionado la opción, se determina que comando usa el servidor
        if opcion == '1':
            tarea = input("Ingrese la tarea a agregar: ")
            enviar_comando(s, f"AGREGAR|{tarea}")
        elif opcion == '2':
            enviar_comando(s, "VER")
        elif opcion == '3':
            tarea = input("Ingrese la tarea a eliminar: ")
            enviar_comando(s, f"ELIMINAR|{tarea}")
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            #Vaso para cuando el usuario selecciona una opción que no existe
            print("Opción no válida.")
    #Cierre de la conexión
    s.close()

if __name__ == "__main__":
    main()
