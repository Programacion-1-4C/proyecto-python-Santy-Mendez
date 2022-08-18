from funciones import org_lista, mostrar_lista,cambiar_datos, compras
todas_listas =[]
print("BIENVENIDO AL ALGORITMO PARA GRAFICAS")
persona = input("Ingrese VENDEDOR si usted es el vendedor de lo contrario escriba CONSUMIDOR\n>>>")
persona_1 = persona.upper()
if persona_1== "VENDEDOR":
    usuario = input("Ingrese usuario\n>>>")
    contraseña = input("Ingrese la contraseña\n>>>")
    if usuario == "over" and contraseña == "over145@":
        sesion = "activada"
        while sesion == "activada":
            print("1. Poner Stock")
            print("2. Ver Listas")
            print("3. Cambiar Informacion")
            print("4. Salir")
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
        print("1 . Comprar Grafica")
        print("2.  Consultar Precio")
        print("3 .  Salir")
        opcions = int(input("Ingrese una opcion\n>>>"))
        if opcions == 1:
            compras(todas_listas)
        if opcions == 2:
            mostrar_lista(todas_listas)
        if opcions == 3:
            print("Vuelva Pronto!")
            break