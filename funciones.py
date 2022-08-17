def org_lista(todas_listas):
    nombre = input("Ingrese el nombre de la lista\n>>>")
    cantidad = int(input("Ingrese la cantidad de graficas de este tipo que tiene\n>>>"))
    marca = input("Ingrese la marca que vende el producto\n>>>")
    chipset = input("Ingrese el fabricante\n>>>")
    modelo = input("Ingrese el modelo\n>>>")
    memoria = int(input("Ingrese la cantidad de memoria\n>>>"))
    refrigeracion = input(
        "Especifique el tipo de refrigeracion y en caso de tener disipadores especifique cuantos\n>>>")
    puertos = int(input("Ingrese la cantidad de puertos\n>>>"))
    rgb = input("Especifique si cuenta con retroiluminacion\n>>>")
    precio = int(input("Ingrese el precio del producto\n>>>"))
    todas_listas.append([
        ("Nombre de la Lista:", nombre),
        ("Cantidad de graficas:", cantidad),
        ("Marca que vende el producto:", marca),
        ("Cantidad de graficas:", cantidad),
        ("Marca que vende el producto:", marca),
        ("Fabircante del Chipset:", chipset),
        ("Modelo de la grafica:", modelo),
        ("Cantidad de Mmeoria:", memoria),
        ("Info de refrigeracion:", refrigeracion),
        ("Cantidad de Puertos:", puertos),
        ("Cuenta con RGB:", rgb),
        ("Precio del producto:", precio),
    ])


def mostrar_lista(lista):
    for sub_lista in lista:
        for elemento in sub_lista:
            print(elemento[0], " ", elemento[1])
        print("-"*50)

def cambiar_datos(todas_listas):
    nombre = input("Ingrese el nombre de la lista\n>>>")
    for sub_lista in todas_listas:
        if sub_lista[0][1] == nombre:
            elemento_1= input("Ingrese que parte de la lista quiere cambiar\n>>> ")
            for j in sub_lista:
                if j[0] == elemento_1:
                    j[1] = input("Ingrese el nuevo dato\n>>>")







