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
]

while True:
    print("****VENTA PASAJES****")
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")

    opcionMenu = int(input("Seleccione una opción:"))

    if opcionMenu == 1:
        contadorFila = 0

        for i in range(len(asientos)):

            contadorFila = contadorFila + 1 
            
            if len(asientos[i]) == 0:
                print(i+1, end="\t")
            else:
                print("X",end="\t")

            if contadorFila == 6:
                print("")
                contadorFila = 0
            elif contadorFila == 3:
                print(end="\t\t")
                contadorPasillo = 0
    elif opcionMenu == 2:
        print("Comprar asiento")

        nroAsiento= int(input("Ingrese numero asiento: "))
        nombrePasajero = input("Ingrese nombre pasajero: ")
        rutPasajero = input("Ingrese rut pasajero 12345678-9: ")
        telefonoPasajero = input("Ingrese telefono pasajero: ")
        bancoPasajero = input("Ingrese banco pasajero: ")

        nuevoPasajero = [nombrePasajero, rutPasajero, telefonoPasajero, bancoPasajero]

        asientos.insert(nroAsiento-1, nuevoPasajero)

    elif opcionMenu == 3:
        print("Anular vuelo")
    elif opcionMenu == 4:
        print("Modificar datos de pasajero")
    elif opcionMenu == 5:
        print("Saliendo...")
        break
    else:
        print("Por favor, seleccione una opción valida")


