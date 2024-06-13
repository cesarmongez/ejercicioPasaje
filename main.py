from funciones import anular_pasaje,ver_asiento_disponible,comprar_pasajes,modificar_datos_pasajero, guardar_datos_pasajeros,cargar_datos_pasajeros

# Precios de los asientos
precioAsientoNormal = 78900
precioAsientoVIP = 240000
totalPasaje = 0

# Bucle infinito para mostrar el menú de opciones hasta que el usuario decida salir.
while True:
    try:
        # Intentamos cargar los datos de los pasajeros desde el archivo CSV
        asientos = cargar_datos_pasajeros()
    except:
        print("Error al cargar los datos de pasajeros.\n")

    # Mostramos el menú principal con las opciones disponibles
    print("****VENTA PASAJES****")
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")

    # Solicitamos la opción del usuario
    while True:
        try:
            opcionMenu = int(input("Seleccione una opción: "))
            break
        except ValueError:
            print("Por favor, ingrese solo numeros.\n")

    # Opción 1: Mostrar los asientos disponibles
    if opcionMenu == 1:
        ver_asiento_disponible(asientos)
        
    # Opción 2: Comprar un asiento
    elif opcionMenu == 2:
        ver_asiento_disponible(asientos)
        comprar_pasajes(asientos,precioAsientoVIP,precioAsientoNormal)

    # Opción 3: Anular un vuelo
    elif opcionMenu == 3:
        print("Anular vuelo")
        anular_pasaje(asientos)

    # Opción 4: Modificar los datos de un pasajero
    elif opcionMenu == 4:
        print("Modificar datos de pasajero")
        modificar_datos_pasajero(asientos)

    # Opción 5: Salir del programa
    elif opcionMenu == 5:
        print("Saliendo...\n")
        break  # Terminamos el bucle infinito y salimos del programa

    # Manejamos cualquier otra opción no válida
    else:
        print("Por favor, seleccione una opción valida")