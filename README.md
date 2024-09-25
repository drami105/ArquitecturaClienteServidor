# ArquitecturaClienteServidor

Actividad 3 - Arquitectura Cliente Servidor
Gestión de tareas

Elaborado por Duban Ferney Ramírez Suárez

- Montaje y Herramientas Utilizadas:
Este proyecto trabajado sobre la arquitectura cliente-servidor, está implementado en Python, utilizando las bibliotecas socket y thread. El servidor se encarga de gestionar las conexiones de varios clientes y procesar las solicitudes para agregar, ver y eliminar tareas de una lista en memoria. El cliente, por su parte, interactúa con el servidor a través de comandos específicos (1. Agregar, 2. Ver, 3. Eliminar, 4. Salir). La arquitectura de red se establece mediante sockets, permitiendo la comunicación entre el cliente y el servidor.


- Aplicación y Objetivo del Ejercicio:
El objetivo del ejercicio es crear un sistema sencillo de gestión de tareas que permita a los usuarios agregar, visualizar y eliminar tareas a través de la línea de comandos. En este se puede apreciar la importancia de la arquitectura cliente-servidor, ya que permite la separación de responsabilidades: el servidor maneja la lógica de negocio y el acceso a los de datos, mientras que el cliente se centra en la interacción del usuario. Esta estructura facilita la escalabilidad, modularidad y el mantenimiento del sistema, al permitir que múltiples clientes accedan a los mismos servicios de forma centralizada.
