import json
from infoCoinMarketCap import esmoneda, resumirMoneda
from datetime import datetime

date=datetime.now() #Se crea una variable para obtener la información del tiempo en que se raliza la transacción
fecha=date.strftime("%A %d/%m/%y %H:%M:%S") #con esta variable se asigna formato de dia de la semana, día/mes/año hora:minuto:segundo

def esdigito(a): #se crea una función para validar que al pedir una cantidad estos sean números
	return a.replace('.','',1).isdigit()

def enviarMonedas(codigoPropio):#Se crea una función para enviar monedas que está en función de la variable -codigoPropio- la cual representa el código del usuario
    moneda=input("Ingrese el nombre o símbolo de la moneda que va enviar: ") #Se le pide al usuario ingresar nombre o simbolo de una criptomoneda que va a enviar
    dataMoneda=resumirMoneda(moneda)  #se llama a la función 'resumirMoneda' en función de la variable 'moneda' para obtener la información de simbolo, nombre y valor en dolares.
    simboloMoneda=dataMoneda["simbolo"]  #el simbolo se obtiene del diccionario dataMoneda el cual se importa desde infoCoinMarketCap.py
    with open("saldoMonedas.json",'r+') as f:  #se abre el archivo saldoMonedas.json en modo de lectura y se guarda en la variable -f-
        data_saldo=json.load(f) #con el modulo json se decodifica el objeto que contiene el archivo -f- para obtener un dicionario
    
    if simboloMoneda in data_saldo.keys(): #Se verifica que la criptomoneda elegida exista dentro del saldo de monedas que posee el usuario
        cantidadMoneda=input("Indique el monto en dolares que va a enviar de la moneda "+dataMoneda['nombre']+" : ") #se hace la petición de la cantidad de dolares que se va a enviar
        while not esdigito(cantidadMoneda): # verificación de que la cantidad ingresada sea un numero, de lo contrario solicita la información de nuevo
            print()
            print("Cantidad inválida, ingrese solo números")
            cantidadMoneda=input("Indique el monto en dolares que va a enviar: ")
        else:
            equivalenciaMoneda=float(cantidadMoneda)/float(dataMoneda["valorUSD"]) #los dolares enviados se convierten en criptomoneda segun su valor del mercado
        if equivalenciaMoneda>data_saldo[simboloMoneda]: #se verifica que la cantidad a transferir no sea superior al saldo disponible de la criptomoneda
            print()
            print("--¡No posee la cantidad suficiente de "+dataMoneda['nombre']+"!--")
        else:
            codigoRecibidor=input("Indique el código de quien va recibir: ") #se pide el codigo de la persona a la cual se enviará dinero
            while codigoRecibidor==codigoPropio: # se verifica que el codigo sea diferente al codigo propio
                print("Código inválido, debe ser diferente al código propio")
                codigoRecibidor=input("Indique el código de quien va recibir: ")
            else: 
                data_saldo[simboloMoneda]=data_saldo[simboloMoneda]-equivalenciaMoneda # al ingresar una moneda y monto validos, se descuenta la cantidad de criptomoneda del saldo de la moneda específica
                        
            with open('saldoMonedas.json','w') as f: #se abre el archivo que contiene el saldo de todas las monedas en modo escritura en la variable -f-
                f.write(json.dumps(data_saldo))  #se reescribe f con el diccionario data_saldo haciendo uso del modulo json.


            with open('historialTransaccion.json','r+') as f:  #se abre el archivo que contiene el hisotiral de transacciones en modo lectura en la variable -f-
                historico=json.load(f) #con el modulo json se decodifica el objeto que contiene el archivo -f- para obtener un dicionario en la variable -historico-
                transaccion={ #se crea el diccionario -transaccion- que contiene toda la información de la transacción realizada
                    len(historico):{
                        "fecha":fecha,
                        "tipo":"Envío",
                        "moneda":dataMoneda["nombre"],
                        "usuario":codigoRecibidor,
                        "cantidad":float(cantidadMoneda)/float(dataMoneda["valorUSD"]),
                        "montoUSD":float(cantidadMoneda)
                    }
                }
                historico.update(transaccion) #el diccionario -historico- es actualizado con la información del diccionario -transaccion-
                f.seek(0)
            with open('historialTransaccion.json','w') as f: #se abre el archivo que contiene el hisotiral de transacciones en modo escritura en la variable -f-
                f.write(json.dumps(historico)) #se reescribe f con el diccionario -historico- haciendo uso del modulo json.
            
            return print("---Criptomoneda enviada con éxito---") #al finalizar la operación de enviar moneda se imprime un mensaje
    else:
        print("--¡No posee este tipo de criptomoneda!--") #cuando no se posee la monea seleccionada se imprime un mensaje

    
        
    
