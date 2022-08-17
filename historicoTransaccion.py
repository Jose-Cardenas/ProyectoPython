import json
from infoCoinMarketCap import resumirMoneda


def historicoTransacciones():
     
    with open("historialTransaccion.json",'r+') as f: #se abre el archivo que contiene el historial de transacciones en modo lectura en la variable -f-
        historial=json.load(f) #con el modulo json se decodifica el objeto que contiene el archivo -f- para obtener un dicionario en la variable -historial-
    for i in historial.keys(): #con el for se recorre por cada clave del diccionario -historial-
        if i=="0": #se debe ignorar cuando -i- vale 0
            pass
        else:
            fecha=historial[i]["fecha"]  #de cada clave se obtiene la información relacionada con la transacción
            tipo=historial[i]["tipo"]
            moneda=historial[i]["moneda"]
            usuario=historial[i]["usuario"]
            cantidad=historial[i]["cantidad"]
            montoUSD=historial[i]["montoUSD"]
            print(i+". El "+fecha+" se realizó una operación de tipo "+tipo+" con la moneda "+moneda+" y una cantidad de "+str(round(cantidad,3))+" con el usuario "+usuario+". El monto en USD era de: $"+str(round(montoUSD,3))+"." ) # la información de cada transacción se imprime en este mensaje
            print() #espacio en blanco para estilo

