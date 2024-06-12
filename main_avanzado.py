
# Lista de asientos inicializada con 42 listas vacías, representando cada asiento.
asientos = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

# Bucle infinito para mostrar el menú de opciones hasta que el usuario decida salir.
while True:
    # Mostrar el menú principal con las opciones disponibles.
    print("****VENTA PASAJES****")
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")

    # Obtener la opción del usuario
    opcionMenu = int(input("Seleccione una opción:"))

    # Opción 1: Ver asientos disponibles
    if opcionMenu == 1:
        contadorFila = 0  # Contador para controlar la cantidad de asientos mostrados en cada fila

        # Recorrer los asientos
        for i in range(len(asientos)):
            contadorFila = contadorFila + 1  # Incrementar el contador de fila

            # Mostrar el número del asiento si está disponible, de lo contrario mostrar 'X'
            if len(asientos[i]) == 0:  # Si la lista del asiento está vacía, está disponible
                print(i + 1, end="\t")  # Mostrar el número del asiento (i + 1 para ajustar a base 1)
            else:  # Si la lista del asiento no está vacía, está ocupado
                print("X", end="\t")  # Mostrar 'X' para indicar que el asiento está ocupado

            # Imprimir un salto de línea cada 6 asientos para organizar la vista en filas
            if contadorFila == 6:
                print("")  # Salto de línea
                contadorFila = 0  # Reiniciar el contador de fila
            # Imprimir una tabulación extra cada 3 asientos (simulando el pasillo)
            elif contadorFila == 3:
                print(end="\t\t")  # Tabulación extra para simular el pasillo
        print()  # Salto de línea final después de mostrar todos los asientos

    # Opción 2: Comprar asiento
    elif opcionMenu == 2:
        print("Comprar asiento")

        # Solicitar el número de asiento y datos del pasajero
        nroAsiento = int(input("Ingrese numero asiento: "))
        nombrePasajero = input("Ingrese nombre pasajero: ")
        rutPasajero = input("Ingrese rut pasajero (sin guiones ni puntos)): ")
        telefonoPasajero = input("Ingrese telefono pasajero: ")
        bancoPasajero = input("Ingrese banco pasajero: ")

        # Crear una lista con los datos del nuevo pasajero
        nuevoPasajero = [nombrePasajero, rutPasajero, telefonoPasajero, bancoPasajero]

        # Asignar los datos del pasajero al asiento correspondiente 
        asientos[nroAsiento - 1] = nuevoPasajero

    # Opción 3: Anular vuelo
    elif opcionMenu == 3:
        print("Anular vuelo")

        # Solicitar el número del asiento a anular
        nroAsientoAAnular = int(input("Ingrese numero del asiento del pasaje a anular: "))

        # Anular el asiento (vaciar la lista para indicar que está disponible)
        asientos[nroAsientoAAnular - 1] = []

    # Opción 4: Modificar datos de pasajero
    elif opcionMenu == 4:
        print("Modificar datos de pasajero")

        # Solicitar el número de asiento y el RUT del pasajero
        nroAsiento = int(input("Ingrese numero asiento: "))
        rutPasajero = input("Ingrese rut pasajero (sin guiones ni puntos)): ")

        # Verificar que el RUT del pasajero coincida con el registrado en el asiento
        if asientos[nroAsiento - 1][1] == rutPasajero:
            print("RUT valido")

            while True:
                # Mostrar el menú de modificación de datos del pasajero
                print("****Modificar datos pasajero****")
                print("1. Modificar nombre pasajero")
                print("2. Modificar telefono pasajero")
                print("3. Salir")

                # Obtener la opción del usuario para modificar datos
                opcionMenuPasajero = int(input("Seleccione una opción: "))

                # Modificar el nombre del pasajero
                if opcionMenuPasajero == 1:
                    nuevoNombrePasajero = input("Ingrese el nuevo nombre del pasajero: ")
                    # Acceder a la lista del asiento y cambiar el nombre (índice 0 de la lista del asiento)
                    asientos[nroAsiento - 1][0] = nuevoNombrePasajero

                # Modificar el teléfono del pasajero
                elif opcionMenuPasajero == 2:
                    nuevoTelefonoPasajero = input("Ingrese el nuevo telefono del pasajero: ")
                    # Acceder a la lista del asiento y cambiar el teléfono (índice 2 de la lista del asiento)
                    asientos[nroAsiento - 1][2] = nuevoTelefonoPasajero

                # Salir del menú de modificación de datos del pasajero
                elif opcionMenuPasajero == 3:
                    print("Saliendo...")
                    break
                else:
                    # Opción no válida
                    print("Seleccione una opcion valida.")
        else:
            print("Rut no encontrado.")

    # Opción 5: Salir del programa
    elif opcionMenu == 5:
        print("Saliendo...")
        break  # Terminar el bucle infinito y salir del programa

    # Manejar cualquier otra opción no válida
    else:
        print("Por favor, seleccione una opción valida")
