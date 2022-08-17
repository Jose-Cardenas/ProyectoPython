import requests
#función para validar si un simbolo es un tipo valido de criptomoneda
def esmoneda(cripto):
    
    #Se crean listas vacias las cuales van a recibir el simbolo, el nombre y la cotización de las diferentes criptomonedas en coinmarketcap
    monedas_list=[]
    nombre_list=[]
    valor_list=[]

    COINMARKET_API_KEY = "e9cd2032-9013-4b92-8059-cbcf291c6969" #clave api de coinmarketcap
    headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': COINMARKET_API_KEY}
    #headers son los crecenciales de acceso necesarios para acceder al API

    #Con la función requests.get() accedo a los datos que proporciona el API
    retorno=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()

    #la variable retorno en este momento representa un diccionario con toda la informa que arroja el API.

    for i in retorno["data"]: #i en esta línea toma el valor de la clave "data" dentro del diccionario otenido por el API (diccionario retorno)
        monedas_list.append(i["symbol"]) #a la lista monedas_list le agrega el valor de la clave "symbol" en cada diccionario que tome valor la variable i
        nombre_list.append(i["name"]) #la lista moneda le agregue el valor de la clave "name" en cada diccionario que tome valor la variable i
        valor_list.append(i["quote"]['USD']['price'])# a la lista valor_list le agrega el valor de la clave "price" en cada diccionario que tome valor la variable i
        
    global monedas  #se crean 3 variables globales -monedas, nombre y valormoneda- las cuales serán tuplas en donde se consultará la información en otra función
    global nombre
    global valormoneda
    monedas=tuple(monedas_list) #crea una tupla que se llama monedas a partir de la lista de simbolos completada con el for
    nombre=tuple(nombre_list) #crea una tupla que se llama nombre a partir de la lista nombre_list completada con el for que contiene el nombre de las monedas
    valormoneda=tuple(valor_list)#crea una tupla que se llama valormoneda a partir de la lista valor_list completada con el for que contiene el valor de las monedas
    return (cripto.upper() in monedas) or (cripto.capitalize() in nombre) #devuelve verdadero o falso si el simbolo o el nombre ingresado hace parte de las tuplas que se contruirán con los simbolos y nombres de criptomonedas disponibles en coinmarketcap

#moneda=input("Indique el simbolo de la criptomoneda: ")#Linea para que el usuario ingrese el symbolo de la criptomoneda

def resumirMoneda(moneda):   #función para resumir la información de coinmarket según una moneda elegida
    while not esmoneda(moneda): #con esta función se verifica que la moneda exista en coinmarket es decir la moneda ingresada debe pertencer a la tupla -monedas- o la tupla -nombre-
            print("Moneda Invalida.")
            moneda=input("Ingrese una moneda válida: ")
    
    if (moneda.upper() in monedas): #con la función upper() y la función capitlize() se permite que el usuario ingrese el simbolo o nombre de la criptomoneda sin un estilo de mayusculas o minusculas definido
        ind=monedas.index(moneda.upper()) #si se ingresa el simbolo de la criptomoneda, se encontrará su posición en la tupla -monedas-
    else:
        ind=nombre.index(moneda.capitalize())#si se ingresa el nombre de la criptomoneda, se encontrará su posición en la tupla -nombre-

    nom=nombre[ind]  #con la posición obtenida en el if anterior se obtiene la información de la moneda de las 3 tuplas y se construye un diccionario que contiene solo la información necesaria de la criptomoneda elegida
    simb=monedas[ind]
    valueUSD=valormoneda[ind]
    resumenMoneda={"nombre":nom,"simbolo":simb,"valorUSD":valueUSD}
    return resumenMoneda #este diccionario es lo que se va a exportar para usarlo en los otros archivos .py


