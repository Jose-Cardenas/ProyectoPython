import json
from infoCoinMarketCap import esmoneda, resumirMoneda

def balanceMonedas():
    moneda=input("Ingrese el nombre o símbolo de la moneda que va consultar: ") #se pide al usuario la criptomoneda que desea consultar
    dataMoneda=resumirMoneda(moneda) #con la función resumirMoneda se verifica que sea una moneda válida y se obtiene un resumen de su información con su valor en el mercado
    simboloMoneda=dataMoneda["simbolo"] #se guarda el simbolo de la criptomoneda a partir de la información obtenida e -dataMoneda-     
    with open("saldoMonedas.json",'r+') as f: #se abre el archivo saldoMonedas.json en modo de lectura y se guarda en la variable -f-
        data_saldo=json.load(f)  #con el modulo json se decodifica el objeto que contiene el archivo -f- para obtener un dicionario
    if simboloMoneda in data_saldo.keys(): #se verica que el usuario posea ese tipo de criptomoneda
        equivalenciaMoneda=data_saldo[simboloMoneda]*float(dataMoneda["valorUSD"]) #se convierte la cantidad poseida de la criptomoneda a dolares con la información obtenida con la función resumirMoneda
        print("De la moneda "+dataMoneda["nombre"]+" posee un total de "+str(round(data_saldo[simboloMoneda],3))+" que equivale a $"+ str(round(equivalenciaMoneda,3))+" USD") #se imprime un mensaje para indicar el valor en dolares del monto de la criptomoneda seleccionada
    else:
        print("--¡No posee este tipo de criptomoneda!--") #mensaje cuando se elige una criptomoneda que el usuario no posee

    
        
    
