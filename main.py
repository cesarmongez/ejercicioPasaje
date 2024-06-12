asientos = [
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24],
    [25,26,27,28,29,30],
    [31,32,33,34,35,36],
    [37,38,39,40,41,42]
]

def verAsientos():
    for fila in asientos:
        contadorSilla = 1
        for silla in fila:

            print(silla, end="\t")
            if contadorSilla == 3:
                print(end="\t\t")
            contadorSilla = contadorSilla+1

        print()


while True:
    print("****VENTA PASAJES****")
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")

    opcionMenu = int(input("Seleccione una opción:"))

    if opcionMenu == 1:
        verAsientos()
    elif opcionMenu == 2:
        print("Comprar asiento")


    elif opcionMenu == 3:
        print("Anular vuelo")
    elif opcionMenu == 4:
        print("Modificar datos de pasajero")
    elif opcionMenu == 5:
        print("Saliendo...")
        break
    else:
        print("Por favor, seleccione una opción valida")