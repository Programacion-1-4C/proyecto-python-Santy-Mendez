from funciones import org_lista
print("BIENVENIDO AL ALGORITMO PARA GRAFICAS")
persona = input("Ingrese VENDEDOR si usted es el vendedor de lo contrario escriba CONSUMIDOR\n>>>")
if persona == "VENDEDOR":
    usuario = input("Ingrese usuario\n>>>")
    contraseña = input("Ingrese la contraseña\n>>>")
    if usuario == "over" and contraseña == "over145@":
        sesion = "activada"
        while sesion == "activada":
            print("1. Crear lista")
            print("2. Poner Stock")
            print("3. Cambiar Stock")
            print("4. Salir")
            opcion = int(input("Ingrese una opcion\n>>>"))
            if opcion == 1:
                org_lista()
            if opcion == "2":
                pass
            if opcion == "3":
                pass
            if opcion == "4":
                break


