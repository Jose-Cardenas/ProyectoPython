import json
from infoCoinMarketCap import resumirMoneda


def balanceGeneralMonedas():   
    with open("saldoMonedas.json",'r+') as f: #se abre el archivo saldoMonedas.json en modo de lectura y se guarda en la variable -f-
        data_saldo=json.load(f) #con el modulo json se decodifica el objeto que contiene el archivo -f- para obtener un dicionario
    totalUSD=0 #Se inicializa una variable -totalUSD- con valor 0
    for i in data_saldo.keys(): #con este for, -i- toma por valor cada clave (es decir simbolo de criptomoneda) en el diccionario -data_saldo-
        dataMoneda=resumirMoneda(i) #con resumir moneda se obtiene un el valor actual en el mercado de cada criptomoneda en el diccionario
        equivalenciaMoneda=data_saldo[i]*float(dataMoneda["valorUSD"]) #se convierte a dolares cada cantidad de criptomoneda
        totalUSD=totalUSD+equivalenciaMoneda #se agrega al total, la equivalencia en dolares de cada criptomoneda
        print("De la moneda "+dataMoneda["nombre"]+" posee un total de "+str(round(data_saldo[i],3))+" que equivale a $"+ str(round(equivalenciaMoneda,3))+" USD") #se imprime un mensaje con la equivalencia en dolares de la cantidad de criptomonedas que posee por cada tipo
    print("--¡Posee un total de $"+str(round(totalUSD,3))+" USD!--")  # se imprime un mensaje con el total en dolares