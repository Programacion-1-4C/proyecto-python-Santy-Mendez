import json


LISTA_MOSTRAR = {
    "nombre": "1. Nombre de la Lista:",
    "cantidad": "2. Cantidad de graficas:",
    "marca": "3. Marca que vende el producto:",
    "chipset": "4. Fabircante del Chipset:",
    "modelo": "5. Modelo de la grafica:",
    "memoria": "6. Cantidad de Mmeoria:",
    "refrigeracion": "7. Info de refrigeracion:",
    "puertos": "8. Cantidad de Puertos:",
    "rgb": "9. Cuenta con RGB:",
    "precio": "10 Precio del producto:"


}


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
    todas_listas.append(
        {
            "nombre": nombre,
            "cantidad": cantidad,
            "marca": marca,
            "chipset": chipset,
            "modelo": modelo,
            "memoria": memoria,
            "refrigeracion": refrigeracion,
            "puertos": puertos,
            "rgb": rgb,
            "precio": precio
        }
    )
    with open('json_data.json', 'w') as outfile:
        json.dump({"productos": todas_listas}, outfile)

def mostrar_lista(lista):
    for sub_lista in lista:
        for elemento in sub_lista:
            print(LISTA_MOSTRAR[elemento], " ", sub_lista[elemento])
        print("-"*50)

def leer_desde_archivo():
    try:
        with open('json_data.json') as json_file:
            data = json.load(json_file)
            return data["productos"]
    except FileNotFoundError:
        return []

def cambiar_datos(todas_listas):
    nombre = input("Ingrese el nombre de la lista\n>>>")
    for sub_lista in todas_listas:
        if sub_lista["nombre"] == nombre:
            elemento_1 = input("Ingrese el numero de la párte en la que quieres cambiar los datos\n>>> ")
            elemento_1 = list(sub_lista.keys())[int(elemento_1) -1]
            if elemento_1 in sub_lista:
                sub_lista[elemento_1] = input("Ingrese el nuevo dato\n>>>")

    with open('json_data.json', 'w') as outfile:
        json.dump({"productos": todas_listas}, outfile)

def compras(todas_listas):
    name = input("Ingrese el modelo de la grafica\n>>>")
    for sub_lista in todas_listas:
        if sub_lista["modelo"] == name:
            print(LISTA_MOSTRAR, " ", sub_lista)
            print("-" * 50)
            pregunta = input("Lo vas a compras?\n>>> ")
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
                    primeros_4 = int(input("Ingrese los primeros 4 nuermos de la tarjeta \n>>>"))
                    contador_1 = len(str(primeros_4))
                    segundos_4 = int(input("Ingrese los segundos 4 nuermos de la tarjeta \n>>>"))
                    contador_2 = len(str(segundos_4))
                    terceros_4 = int(input("Ingrese los terceros 4 nuermos de la tarjeta \n>>>"))
                    contador_3 = len(str(terceros_4))
                    ultimos_4 = int(input("Ingrese los cuartos 4 nuermos de la tarjeta \n>>>"))
                    contador_4 = len(str(ultimos_4))
                    nombre_y_apellido = input("Ingrese el nombre y apelido del titular\n>>>")
                    nombre_y_apellido_2 = nombre_y_apellido.upper()
                    mes_cvv = int(input("Ingrese el mes del vencimiento \n>>>"))
                    año_cvv = int(input("Ingrese el año de vencimiento\n>>>"))
                    if mes_cvv != 8 and año_cvv != 22 and contador_1 == 4 and contador_2 == 4 and contador_3 == 4 and contador_4 == 4:
                        print("Datos aceptados ")
                        print("La compra fue correctamente hecha!")
                    else:
                        print("ERROR: Revisa los datos.....")
                if metodo == 4:
                    print("Para Transferencias por favor mandelo a el siguiente CVU")
                    print(">>>CVU:0000003100093985126731")
                if metodo == 5:
                    print("Por favor abone el monto del producto en caja")
        else:
            pregunta_2 = input("Quieres buscar otra grafica?\n>>>")
            if pregunta_2 == "si":
                print(todas_listas)
                pregunta_3=input("Encontraste algo para comprar?\n>>>")
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
                        print("Para pagar por mercado pago hagalo por medio del CVU o ALIAS")
                        print(">>> CVU: 0000003100093985126731"
                              ">>> ALIAS : casa.pc.1")
                        print("Enviar comprobante por Whatsapp al siguiente numero")
                        print(">>> Numero: 3518579473")
                    if metodo == 3:
                        primeros_4 = int(input("Ingrese los primeros 4 nuermos de la tarjeta \n>>>"))
                        contador_1 = len(str(primeros_4))
                        segundos_4 = int(input("Ingrese los segundos 4 nuermos de la tarjeta \n>>>"))
                        contador_2 = len(str(segundos_4))
                        terceros_4 = int(input("Ingrese los terceros 4 nuermos de la tarjeta \n>>>"))
                        contador_3 = len(str(terceros_4))
                        ultimos_4 = int(input("Ingrese los cuartos 4 nuermos de la tarjeta \n>>>"))
                        contador_4 = len(str(ultimos_4))
                        nombre_y_apellido = input("Ingrese el nombre y apellido del titular\n>>>")
                        nombre_y_apellido_2 = nombre_y_apellido.upper()
                        mes_cvv = int(input("Ingrese el mes del vencimiento \n>>>"))
                        año_cvv = int(input("Ingrese el año de vencimiento\n>>>"))
                        if mes_cvv != 8 and año_cvv != 22 and contador_1 == 4 and contador_2 == 4 and contador_3 == 4 and contador_4 == 4:
                            print("Datos aceptados ")
                            print("La compra fue correctamente hecha!")
                        else:
                            print("ERROR: Revisa los datos.....")
                    if metodo == 4:
                        print("Para Transferencias por favor mandelo a el siguiente CBU")
                        print(">>>CBU:0000003100093985126731")
                    if metodo == 5:
                        print("Por favor abone el monto del producto en caja")
                else:
                    print("No tenemos la grafica que buscas, disiculpanos :(")
            else:
                print("No tenemos la grafica que buscas, disiculpanos :(")