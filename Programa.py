from funciones import org_lista, mostrar_lista, cambiar_datos, compras, leer_desde_archivo

todas_listas = leer_desde_archivo()

print("|--------------------------------------|")
print("|              VENTAS                  |")
print("|                DE                    |")
print("|         TARJETAS GRAFICAS            |")
print("|--------------------------------------|")
persona = input("Ingrese VENDEDOR si usted es el vendedor de lo contrario escriba CONSUMIDOR\n>>>")
persona_1 = persona.upper()
if persona_1== "VENDEDOR" or persona_1 == "ADMIN":
    usuario = input("Ingrese usuario\n>>>")
    contraseña = input("Ingrese la contraseña\n>>>")
    if (usuario == "over" and contraseña == "over145@") or persona_1 == "ADMIN":
        sesion = "activada"
        while sesion == "activada":
            print(" -------------------------------------")
            print("|         1. Poner Stock               |")
            print("|         2. Ver listas                |")
            print("|         3. Cambiar Informacion       |")
            print("|         4. Salir                     |")
            print(" --------------------------------------")
            opcion = int(input("Ingrese una opcion\n>>>"))
            if opcion == 1:
                org_lista(todas_listas)
            if opcion == 2:
                mostrar_lista(todas_listas)
            if opcion == 3:
                mostrar_lista(todas_listas)
                cambiar_datos(todas_listas)
            if opcion == 4:
                print("Salir")
                break
if persona_1 == "CONSUMIDOR":
    sesion = "no activada"
    while sesion == "no activada":
        print(" -------------------------------------")
        print("|         1. Comprar Grafica           |")
        print("|         2. Consultar Precio          |")
        print("|         3. Salir                     |")
        print(" --------------------------------------")
        opcions = int(input("Ingrese una opcion\n>>>"))
        if opcions == 1:
            mostrar_lista(todas_listas)
            compras(todas_listas)
        if opcions == 2:
            mostrar_lista(todas_listas)
        if opcions == 3:
            print("Vuelva Pronto!")
            break