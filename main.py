from funciones import Poner_stock

if __name__ == "__main__":
    print("BIENVENIDO AL ALGORITMO PARA GRAFICAS")
    persona = input("Ingrese VENDEDOR si ustdes es el vendedor de lo contrario escriba CONSUMIDOR\n>>>")
    if persona == "VENDEDOR":
        usuario = input("Ingrese usuario\n>>>")
        contraseña = input("Ingrese la contraseña\n>>>")
        if usuario == "over" and contraseña == "over145@":
            sesion = "activada"
            while sesion == "activada":
                print("1. Poner Stock")
                print("2. Cambiar Stock")
                print("3. Salir")
                opcion = int(input("Ingrese una opcion\n>>>"))