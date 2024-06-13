import csv

# Definimos esta función para guardar los datos de los pasajeros en un archivo CSV
def guardar_datos_pasajeros(asientos):
    # Abrimos el archivo 'datos_vuelo.csv' en modo escritura (usamos 'w' como segundo argumento para indicar que vamos a escribir)
    with open('datos_vuelo.csv', 'w', newline="") as archivo:
        # Creamos un objeto escritor de CSV
        escritor = csv.writer(archivo)
        # Escribimos todas las filas de la lista 'asientos' en el archivo CSV
        escritor.writerows(asientos)
    
    print("Datos guardados.\n")

# Definimos esta función para cargar los datos de los pasajeros desde un archivo CSV
def cargar_datos_pasajeros():
    try:
        # Intentamos abrir el archivo 'datos_vuelo.csv' en modo lectura (usamos 'r' como segundo argumento para indicar que vamos a escribir)
        asientos = []
        with open('datos_vuelo.csv', 'r', newline='') as archivo:
            # Creamos un objeto lector de CSV
            lector = csv.reader(archivo)
            # Inicializamos la lista 'asientos' para almacenar los datos leídos
            # Recorremos cada fila del archivo CSV, transformamos el rut y el telefono a entero, añadimos los datos a la lista datos_pasajero y esa lista la añadimos a la lista 'asientos'
            for fila in lector:
                if len(fila)< 4: #Si el largo de la fila es menor a 4 significa que esta vacia asi que simplemente agregamos una lista vacia a asientos.
                    asientos.append([])
                else: #sino Convertimos los campos rut y teléfono a enteros si es posible

                
                    nombre = fila[0]
                    rut = int(fila[1])  # Convertimos rut a entero
                    telefono = int(fila[2])  # Convertimos telefono a entero
                    banco = fila[3]
                    # Creamos una lista con los datos convertidos
                    datos_pasajero = [nombre, rut, telefono, banco]
                    # Añadimos la lista de datos del pasajero a la lista 'asientos'
                    asientos.append(datos_pasajero)

    except FileNotFoundError:
        # Si el archivo no se encuentra se va a lanzar una excepcion llamada FileNotFoundError, la atraparemos e imprimiremos un mensaje y creamos la lista 'asientos' vacía
        print("Archivo 'datos_vuelo.csv' no encontrado. Inicializando asientos vacíos.\n")
        # Inicializamos 'asientos' con 42 listas vacías
        asientos = []
        for i in range(42):
            asientos.append([])
    except Exception as e:
        print(e)

    # Retornamos la lista 'asientos' cargada o inicializada
    return asientos

# Definimos esta función para anular un pasaje
def anular_pasaje(asientos):
    # Solicitamos el número del asiento a anular
    nroAsientoAAnular = int(input("Ingrese numero del asiento del pasaje a anular: "))
    # Verificamos si el asiento está vacío (no se ha comprado
    if len(asientos[nroAsientoAAnular - 1])==0: # este if analiza si hay algo dentro de la lista que guarda la lista de ese asiento
        print(" No existe la compra de este pasaje ") # Entonces si el rango es igual a 0 es porque no existe la compra de ese pasaje 
    else:
        # Mostramos los datos del pasajero antes de anular el pasaje
        print("Datos del pasajero a anular:")
        print("Nombre:", asientos[nroAsientoAAnular - 1][0])
        print("RUT:", asientos[nroAsientoAAnular - 1][1])
        print("Teléfono:", asientos[nroAsientoAAnular - 1][2])
        confirmacion = input("¿Está seguro que desea anular este pasaje? (si/no): ").lower()
        if confirmacion == 'si':
            # Anulamos el asiento (reemplazamos la lista que contiene los datos del pasaje por una lista vacía para indicar que está disponible)
            asientos[nroAsientoAAnular - 1] = []
            guardar_datos_pasajeros(asientos)
            print("Su pasaje ha sido anulado con éxito.\n")
        else:
            print("Operación cancelada.\n")

# Definimos esta función para visualizar los asientos disponibles
def ver_asiento_disponible(asientos): # Esta función visualiza asientos disponibles
    print()
    print("Asientos disponibles: ")
    contadorFila = 0  # Contador para controlar la cantidad de asientos mostrados en cada fila

    # Recorremos los asientos
    for i in range(len(asientos)):
        #Si el contador es 0 significa que la fila esta empezando asi que imprmimimos la pared de la izquierda
        if contadorFila == 0:
            print("|", end="\t")
        contadorFila = contadorFila + 1  # Incrementar el contador de fila

        # Mostramos el número del asiento si está disponible, de lo contrario mostramos 'X'
        if len(asientos[i]) == 0:  # Si la lista del asiento está vacía, significa que el asiento esta disponible
            print(i + 1, end="\t")  # Imprimimos el indice y le sumamos 1 para que coincida con el asiento ya que el asiento 1 esta en realidad en la posicion 0 de la lista asientos
        else:  # Si la lista del asiento no está vacía significa que está ocupado
            print("X", end="\t")  # Mostramos 'X' para indicar que el asiento está ocupado

        # Imprimimos un salto de línea cada 6 asientos para organizar la vista en filas
        if contadorFila == 6:
            print("|")#antes del salto de linea imprimimos la pared de la derecha
            print("")  # Salto de línea para iniciar una nueva fila
            contadorFila = 0  # Reiniciamos el contador de fila
        # Imprimimos una tabulación extra cada 3 asientos para simular el pasillo
        elif contadorFila == 3:
            print(end="\t\t")  # Tabulación extra para simular el pasillo

        if i ==29: # Para crear la division entre pasajes normales y VIP
            print("|","_"*23,"\t\t\t","_"*22,"|")
            print()
            print("|","_"*23,"\t\t\t","_"*22,"|")
            print()

    print()  # Salto de línea final después de mostrar todos los asientos

# Definimos esta función para comprar pasajes
def comprar_pasajes(asientos, precioAsientoVIP, precioAsientoNormal):
    # Solicitamos al usuario ingresar el número de asiento y los datos del pasajero
    print("Precio asientos:")
    print("- Asiento normal (DESDE ASIENTO 1 AL 30): $", precioAsientoNormal)
    print("- Asiento VIP (DESDE ASIENTO 31 AL 42): $", precioAsientoVIP)
    while True:
        try:
            nroAsiento = int(input("Ingrese el número de asiento a comprar: "))
            
            #Validamos que el asiento este entre 1 y 42.
            if nroAsiento > 0 and nroAsiento <=42:
                

                # Validamos que el asiento esté disponible para la compra
                if len(asientos[nroAsiento - 1]) != 0:
                    print("El asiento seleccionado ya está ocupado. Por favor, seleccione otro asiento. \n")
                else:
                    break
            else:
                print("Por favor, ingrese un numero de asiento valido (entre 1 y 42). .\n")
        except ValueError: 
            print("Por favor, ingrese solo números para el asiento.\n")


    # Determinamos el tipo de asiento seleccionado y calculamos el total del pasaje
    if nroAsiento > 0 and nroAsiento <= 30:
        print("Seleccionaste asiento normal.\n")
        totalPasaje = precioAsientoNormal
    elif nroAsiento > 30 and nroAsiento <= 42:
        print("Seleccionaste asiento VIP.\n")
        totalPasaje = precioAsientoVIP
        
    nombrePasajero = input("Ingrese nombre pasajero: ")
    # Validamos el RUT del pasajero
    while True: 
        try:
            rutPasajero = int(input("Ingrese rut pasajero (sin punto ni guión)): "))
            break
        except ValueError:
            print("Por favor, ingrese solo números para el rut.\n")
    # Validamos el teléfono del pasajero
    while True:
        try:
            telefonoPasajero = int(input("Ingrese teléfono pasajero : "))
            break
        except ValueError:
            print("Por favor, ingrese solo números para el telefono.\n")
            
    bancoPasajero = input("Ingrese banco pasajero (bancoDuoc / Otro) : ").lower()



    # Calculamos el descuento si corresponde
    if bancoPasajero == "bancoduoc":
        descuento = totalPasaje*.15
    else:
        descuento = 0
    # Calculamos el total a pagar luego de aplicar el descuento
    totalAPagar = totalPasaje - descuento

    # Mostramos el total a pagar al usuario
    print("El total a pagar es de $", totalAPagar)
    confirmarCompra = input("¿Desea comprar el pasaje? (si/no): ").lower()
    if confirmarCompra == "si":
        # Creamos una lista con los datos del nuevo pasajero
        nuevoPasajero = [nombrePasajero, rutPasajero, telefonoPasajero, bancoPasajero]
        #  Asignamos los datos del pasajero al asiento correspondiente en la lista de asientos
        asientos[nroAsiento - 1] = nuevoPasajero
        # Guardamos los datos actualizados de los pasajeros en el archivo CSV
        print("Pasaje comprado, gracias.\n")
        guardar_datos_pasajeros(asientos)
    else:
        print("Compra anulada. \n")

    
# Definimos esta función para modificar los datos de los pasajeros
def modificar_datos_pasajero(asientos):
    # Solicitamos el número de asiento 
    while True: 
        try:
            nroAsiento = int(input("Ingrese el numero de asiento a modificar: "))
            if nroAsiento > 0 and nroAsiento <=42:
                print()
                break

            else:
                print("Por favor, ingrese un numero de asiento valido (entre 1 y 42). .\n")
        except ValueError:
            print("Por favor, ingrese solo números para el numero de asiento.\n")
    if len(asientos[nroAsiento - 1])==0: # Si el largo es igual a 0, la lista esta vacia y el pasaje no existe
        print("Pasaje a modificar no existe. ")
    else: # El codigo se ejecutará solo si el pasaje existe o si el largo de la lista es distinta de 0
        
        #Solicitamos y validamos el RUT del pasajero a modificar
        while True: 
            try:
                rutPasajero = int(input("Ingrese rut pasajero (sin punto ni guión)): "))
                break
            except ValueError:
                print("Por favor, ingrese solo números para el rut.\n")

        # Verificamos que el RUT del pasajero coincida con el registrado en el asiento
        if asientos[nroAsiento - 1][1] == rutPasajero:
            print("RUT valido.\n")

            while True:
                # Mostramos los datos del pasajero antes de anular el pasaje
                print("Datos del pasajero a anular:")
                print("Nombre:", asientos[nroAsiento - 1][0])
                print("RUT:", asientos[nroAsiento - 1][1])
                print("Teléfono:", asientos[nroAsiento - 1][2])
                print("")
                # Mostramos el menú de modificación de datos del pasajero
                print("****Modificar datos pasajero****")
                print("1. Modificar nombre pasajero.")
                print("2. Modificar telefono pasajero.")
                print("3. Salir.")

                # Obtenemos la opción del usuario para modificar datos
                opcionMenuPasajero = int(input("Seleccione una opción: "))

                # Modificamos el nombre del pasajero
                if opcionMenuPasajero == 1:
                    nuevoNombrePasajero = input("Ingrese el nuevo nombre del pasajero: ")
                    # Accedemos a la lista del asiento y cambiamos el nombre (índice 0 de la lista del asiento)
                    asientos[nroAsiento - 1][0] = nuevoNombrePasajero
                    guardar_datos_pasajeros(asientos)
                    print("Nombre modificado con exito.\n")

                # Modificamos el teléfono del pasajero
                elif opcionMenuPasajero == 2:
                    nuevoTelefonoPasajero = input("Ingrese el nuevo telefono del pasajero: ")
                    # Accedemos a la lista del asiento y cambiamos el teléfono (índice 2 de la lista del asiento)
                    asientos[nroAsiento - 1][2] = nuevoTelefonoPasajero
                    guardar_datos_pasajeros(asientos)
                    print("telefono modificado con exito.\n")


                # Salimos del menú de modificación de datos del pasajero
                elif opcionMenuPasajero == 3:
                    print("Saliendo...")
                    break
                else:
                    # Opción no válida
                    print("Seleccione una opcion valida.\n")
        else:
            print("Rut no encontrado.\n")