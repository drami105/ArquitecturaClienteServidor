#Elaborado por Duban Ferney Ramírez Suárez

#Importo las librerías a utilizar
from socket import *
from _thread import *
import json

# Defino arreglo para almacenar las tareas en la memoria del servidor
tareas = []

# Inicialización del el servidor
def iniciar_servidor(host, puerto):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((host, puerto))
    s.listen(5)
    print(f"Servidor escuchando en {host}:{puerto}")
    return s

# Manejo conexiones del cliente
def manejar_cliente(conn, addr):
    print(f"Conexión establecida: {addr}")
    while True:
        try:
            #se decodifica el mensaje
            solicitud = conn.recv(1024).decode('utf-8')
            #Validación para identificar cuando el cliente se ha desconectado
            if not solicitud:
                print(f"El cliente {addr} se ha desconectado.")
                break

            # Procesamiento de la solicitud
            respuesta = procesar_solicitud(solicitud)
            conn.send(respuesta.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            break
    conn.close()

# Proceso las solicitudes de los clientes
def procesar_solicitud(solicitud):
    #defino delimitadcor para separar los datos
    parts = solicitud.split('|')
    comando = parts[0]

    #Defino condición para la opción Agregar tarea
    if comando == 'AGREGAR':
        tarea = parts[1]
        tareas.append(tarea)
        return f"Tarea '{tarea}' añadida."
    
    #Defino condición para la opción Ver tarea
    elif comando == 'VER':
        #Retorno la lista de tareas en un JSON
        return json.dumps(tareas)  
    
    #Defino condición para la opción Eliminar tarea
    elif comando == 'ELIMINAR':
        tarea = parts[1]
        #identifico si el nombre de la tarea existe para determinar si se elimina o si no existe
        if tarea in tareas:
            tareas.remove(tarea)
            return f"Tarea '{tarea}' eliminada."
        else:
            return f"Tarea '{tarea}' no encontrada."

    return "Comando no reconocido."

# Función principal
def main():
    #En host establezco la dirección ip local 127.0.0.1 o localhost
    host = '127.0.0.1'
    #En el puerto utilizo el 8089
    puerto = 8089
    servidor = iniciar_servidor(host, puerto)

    #Servidor escuhando las peticiones de los clientes
    while True:
        conn, addr = servidor.accept()
        start_new_thread(manejar_cliente, (conn, addr))

if __name__ == "__main__":
    main()
