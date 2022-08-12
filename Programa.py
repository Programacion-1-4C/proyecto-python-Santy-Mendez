from funciones import org_lista
todas_listas= { }
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
            print("2. Cambiar Stock")
            print("3. Salir")
            opcion = int(input("Ingrese una opcion\n>>>"))
            if opcion == 1:
                pass
            if opcion == 2:
                pass
            if opcion == 3:
                pass
            if opcion == 4:
                break



