
def encontrarPrimos(n):
    primos = []
    #recorremos todos los numeros que hay hasta n
    for numero in range(2, n+1):
        contador = 0
        for div in range(2, numero):
            #como excluimos dividir por 1 y por si mismo, si el resto es 0 quiere decir que no es primo
            if numero % div == 0:
                contador += 1
        #comprobamos que no haya habido numeros divisibles
        if contador == 0:
            primos.append(numero)
    
    return primos
