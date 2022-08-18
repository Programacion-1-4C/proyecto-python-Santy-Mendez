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
def compras(todas_listas):
    name = input("Ingrese el modelo de la grafica\n>>>")
    for sub_lista in todas_listas:
        if sub_lista[13][14] == name:
            print(sub_lista)
            pregunta = input("Lo vas a compras\n>>>? ")
            if pregunta == "si":
                print("compra")
                print("Opciones de Pago:")
                print(">>>1.Paypal")
                print(">>>2.Mercado Pago")
                print(">>>3.Targeta de Credito/Debito")
                print(">>>4.Tranferencia")
                print(">>>5. Efectivo")
                metodo = int(input("Ingrese la opcion\n>>>"))
                if metodo == 1:
                    print("Para enviar los dolares equivalente al precio del producto envielo a la siguiente direccion de email")
                    print("Y envie el comprbante por ese mismo email")
                    print(">>>Email:GraficasOn@gmail.com")
                if metodo == 2:
                    print("Para pagar por mercado pago hagalo por medio del CBU o ALIAS")
                    print(">>> CBU: 0000003100093985126731"
                          ">>> ALIAS : casa.pc.1")
                    print("Enviar comprobante por Whatsapp al siguiente numero")
                    print(">>> Numero: 3518579473")
                if metodo == 3:
                    pass
                if metodo == 4:
                    print("Para Transferencias por favor mandelo a el siguiente CBU")
                    print(">>>CBU:0000003100093985126731")
                if metodo == 5:
                    print("Por favor abone el monto del producto en caja")
        else:
            pregunta_2 = input("Quieres buscar otra grafica?\n>>>")
            if pregunta_2 == "si":
                print(todas_listas)
                pregunta_3=input("Encontraste algo para comprar?")
                if pregunta_3 == "si":
                    print("comprar")
                    print("Opciones de Pago:")
                    print(">>>1.Paypal")
                    print(">>>2.Mercado Pago")
                    print(">>>3.Targeta de Credito/Debito")
                    print(">>>4.Tranferencia")
                    print(">>>5. Efectivo")
                    metodo = int(input("Ingrese la opcion\n>>>"))
                    if metodo == 1:
                        print(
                            "Para enviar los dolares equivalente al precio del producto envielo a la siguiente direccion de email")
                        print("Y envie el comprbante por ese mismo email")
                        print(">>>Email:GraficasOn@gmail.com")
                    if metodo == 2:
                        print("Para pagar por mercado pago hagalo por medio del CBU o ALIAS")
                        print(">>> CBU: 0000003100093985126731"
                              ">>> ALIAS : casa.pc.1")
                        print("Enviar comprobante por Whatsapp al siguiente numero")
                        print(">>> Numero: 3518579473")
                    if metodo == 3:
                        pass
                    if metodo == 4:
                        print("Para Transferencias por favor mandelo a el siguiente CBU")
                        print(">>>CBU:0000003100093985126731")
                    if metodo == 5:
                        print("Por favor abone el monto del producto en caja")
                else:
                    print("No tenemos la grafica que buscas, disiculpanos :(")
            else:
                print("No tenemos la grafica que buscas, disiculpanos :(")