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
    []
]

# Bucle infinito para mostrar el menú de opciones hasta que el usuario decida salir.
while True:
    # Mostrar el menú de opciones.
    print("****VENTA PASAJES****")
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")

    # Solicitar al usuario que seleccione una opción del menú.
    opcionMenu = int(input("Seleccione una opción:"))

    # Opción 1: Ver asientos disponibles.
    if opcionMenu == 1:
        contadorFila = 0  # Contador para controlar las filas de asientos.

        # Recorrer cada asiento en la lista de asientos.
        for i in range(len(asientos)):
            contadorFila = contadorFila + 1  # Incrementar el contador de fila.

            # Si el asiento está vacío (sin pasajero), mostrar el número del asiento.
            if len(asientos[i]) == 0:
                print(i + 1, end="\t")
            else:
                # Si el asiento está ocupado, mostrar una "X".
                print("X", end="\t")

            # Formatear la salida para mostrar 6 asientos por fila.
            if contadorFila == 6:
                print("")
                contadorFila = 0
            # Añadir un espacio adicional en el medio de la fila para simular el pasillo.
            elif contadorFila == 3:
                print(end="\t\t")

    # Opción 2: Comprar asiento.
    elif opcionMenu == 2:
        print("Comprar asiento")

        # Solicitar al usuario los datos del pasajero.
        nroAsiento = int(input("Ingrese número de asiento: "))
        nombrePasajero = input("Ingrese nombre pasajero: ")
        rutPasajero = input("Ingrese RUT pasajero 12345678-9: ")
        telefonoPasajero = input("Ingrese teléfono pasajero: ")
        bancoPasajero = input("Ingrese banco pasajero: ")

        # Crear una lista con los datos del nuevo pasajero.
        nuevoPasajero = [nombrePasajero, rutPasajero,
                         telefonoPasajero, bancoPasajero]

        # Insertar la lista del nuevo pasajero en el asiento correspondiente.
        asientos[nroAsiento - 1] = nuevoPasajero

    # Opción 3: Anular vuelo 
    elif opcionMenu == 3:
        print("Anular vuelo")

    # Opción 4: Modificar datos de pasajero 
    elif opcionMenu == 4:
        print("Modificar datos de pasajero")

    # Opción 5: Salir del programa.
    elif opcionMenu == 5:
        print("Saliendo...")
        break  # Romper el bucle infinito para salir del programa.

    # Opción inválida: Mostrar mensaje de error.
    else:
        print("Por favor, seleccione una opción válida")
