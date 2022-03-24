def primos(num1, num2):
    resultado = []
    for i in range(num1, num2+1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                resultado.append(i)
    return resultado
