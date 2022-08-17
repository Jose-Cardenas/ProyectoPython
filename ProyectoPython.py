from recibirMoneda import recibirMonedas #Función que contiene el cógido para recibir una cantidad de criptomonedas
from enviarMoneda import enviarMonedas #Función que contiene el cógido para enviar una cantidad de criptomonedas
from balanceMoneda import balanceMonedas #Función que contiene el cógido para ver el balance específico de una moneda
from balanceGeneral import balanceGeneralMonedas #Función que contiene el cógido para ver el balance general de todas las criptomonedas
from historicoTransaccion import historicoTransacciones  #Función que contiene el cógido para ver el histórico de transacciones

#Función para mostrar el mensaje menú inicial
def mensajeMenu():
    print("Elija una opción del menú mediante el dígito (1-6)")
    print("1. Recibir monedas")
    print("2. Transferir monedas")
    print("3. Mostrar balance de moneda")
    print("4. Mostrar balance general")
    print("5. Mostrar histórico de transacciones")
    print("6. Salir del programa")
    print("") #espacio en blanco para estilo



def seleccionarOpcion():
    print()#espacio en blanco para estilo
    mensajeMenu()
    opciones= ["1","2","3","4","5","6"]
    global seleccion
    seleccion=input("Elija una opción del menú: ")
    print("")#espacio en blanco para estilo
    while not seleccion in opciones: #while para asegurar que se digite una opción válida del menú
        print("") #espacio en blanco para estilo
        print("--Opción no válida--")
        mensajeMenu()
        print("") #espacio en blanco para estilo
        seleccion=input("Elija una opción válida: ")
    return seleccion

print("") #espacio vacio para formato
codigoPropio="1234" #codigo asignado para el usuario

codigoUsuario=str(input("Ingrese su codigo de usuario: ")) # codigo propio del usuario
while not codigoPropio==codigoUsuario: #condicional para verificar que se ingresa el codigo propio del usuario válido
    print("Codigo inválido")
    codigoUsuario=str(input("Ingrese su codigo de usario: "))

seleccionarOpcion() #se ejecuta una función en la que se valida que la opción elegida sea válida


#Condicional para ejecutar una función según la elección del dígito en el menú
while not seleccion=="6": #al elegir 6 se cierra la aplicacion
    if seleccion=="1": 
        recibirMonedas(codigoUsuario)
        seleccionarOpcion()
    elif seleccion=="2":
        enviarMonedas(codigoUsuario)
        print("")#espacio en blanco para estilo
        seleccionarOpcion()
    elif seleccion=="3":
        balanceMonedas()
        print("")#espacio en blanco para estilo
        seleccionarOpcion()
    elif seleccion=="4":
        balanceGeneralMonedas()
        print("")#espacio en blanco para estilo
        seleccionarOpcion()
    else:
        historicoTransacciones()
        print("")#espacio en blanco para estilo
        seleccionarOpcion()
    
print("Fin de la operación")

