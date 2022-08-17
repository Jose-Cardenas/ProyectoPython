import json
from infoCoinMarketCap import esmoneda, resumirMoneda
from datetime import datetime

date=datetime.now() #Se crea una variable para obtener la información del tiempo en que se raliza la transacción
fecha=date.strftime("%A %d/%m/%y %H:%M:%S") #con esta variable se asigna formato de dia de la semana, día/mes/año hora:minuto:segundo

def esdigito(a): #se crea una función para validar que al pedir una cantidad estos sean números
	return a.replace('.','',1).isdigit() #de esta forma se reemplaza el primer punto que se encuentra por un espacio vacio, si esto es un digito retorna true

def recibirMonedas(codigoPropio): #Se crea una función para recibir monedas que está en función de la variable codigoPropio la cual representa el código del usuario
    moneda=input("Ingrese el nombre o símbolo de la moneda que está recibiendo: ") #Se le pide al usuario ingresar nombre o simbolo de una criptomoneda que va a recibir
    dataMoneda=resumirMoneda(moneda) #se llama a la función 'resumirMoneda' en función de la variable 'moneda' para obtener la información de simbolo, nombre y valor en dolares.
    if dataMoneda: #se debe ingresar una moneda válida para que se ejecute el siguiente codigo
        cantidadMoneda=input("Indique la cantidad de la criptomoneda "+dataMoneda['nombre']+" que va a recibir: ") #se hace la petición de la cantidad de criptomoneda que se va a recibir
        while not esdigito(cantidadMoneda): # verificación de que la cantidad ingresada sea un numero, de lo contrario solicita la información de nuevo
            print()
            print("Cantidad inválida, ingrese solo números")
            cantidadMoneda=input("Indique la cantidad de la criptomoneda "+dataMoneda['nombre']+" que va a recibir: ")
        else:
            codigoEnviador=input("Indique el código del enviador: ") #luego se ingresa el codigo del enviador
        while codigoEnviador==codigoPropio: #se verifica que el codigo del enviador sea diferente al codigo propio
            print("Código inválido, debe ser diferente al código propio")
            codigoEnviador=input("Indique el código del enviador: ")
        else: #al ingresar una cantidad de moneda y un codigo de enviador validos se obtiene el simbolo de la criptomoneda elegida en la linea 12
            simboloMoneda=dataMoneda["simbolo"] #el simbolo se obtiene del diccionario dataMoneda el cual se importa desde infoCoinMarketCap.py
            
        with open("saldoMonedas.json",'r+') as f: #se abre el archivo saldoMonedas.json en modo de lectura y se guarda en la variable -f-
            data_saldo=json.load(f)  #con el modulo json se decodifica el objeto que contiene el archivo -f- para obtener un dicionario
            if simboloMoneda in data_saldo.keys():  #se busca si la moneda ya existe guardada en el archivo 
                data_saldo[simboloMoneda]=data_saldo[simboloMoneda]+float(cantidadMoneda) #en caso de que la moneda ya exista, se actualiza su valor con la cantidad de monedas recibidas
                
            else:
                data_saldo.update({simboloMoneda:float(cantidadMoneda)}) #en caso de que no exista la moneda, se actualiza el diccionario con la clave:valor -simbolo de la moneda: cantidad recibida-
                f.seek(0)      
        with open('saldoMonedas.json','w') as f: #se abre el archivo que contiene el saldo de todas las monedas en modo escritura en la variable -f-
            f.write(json.dumps(data_saldo)) #se reescribe f con el diccionario data_saldo haciendo uso del modulo json.


        with open('historialTransaccion.json','r+') as f: #se abre el archivo que contiene el hisotiral de transacciones en modo lectura en la variable -f-
            historico=json.load(f) #con el modulo json se decodifica el objeto que contiene el archivo -f- para obtener un dicionario en la variable -historico-
            transaccion={    #se crea el diccionario -transaccion- que contiene toda la información de la transacción realizada
                len(historico):{
                    "fecha":fecha,
                    "tipo":"Recepcion",
                    "moneda":dataMoneda["nombre"],
                    "usuario":codigoEnviador,
                    "cantidad":float(cantidadMoneda),
                    "montoUSD":float(cantidadMoneda)*float(dataMoneda["valorUSD"])
                }
            }
            historico.update(transaccion) #el diccionario -historico- es actualizado con la información del diccionario -transaccion-
            f.seek(0)
        with open('historialTransaccion.json','w') as f:  #se abre el archivo que contiene el hisotiral de transacciones en modo escritura en la variable -f-
            f.write(json.dumps(historico)) #se reescribe f con el diccionario -historico- haciendo uso del modulo json.

    return print("---Criptomoneda recibida con éxito---") #al finalizar la operación de recibir moneda se imprime un mensaje
        
    
