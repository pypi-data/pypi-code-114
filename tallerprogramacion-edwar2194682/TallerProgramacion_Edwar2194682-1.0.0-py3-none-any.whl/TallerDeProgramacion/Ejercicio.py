import numpy as np

def about():
    print("Las funciones son maximoyminimo(), igualdad() y modulo()")

def maximoyminimo(lista1,lista2,lista3):
    matrix = np.matrix([lista1,lista2,lista3])
    print("El maximo de la matrix es",matrix.argmax())
    print("El mnimo de la matrix es",matrix.argmin())

def igualdad(matrix,matrix2):
    matrix = np.matrix(matrix)
    matrix2 = np.matrix(matrix2)
    print(matrix==matrix2)

def Modulo(lista):
    matrix = np.array(lista)
    matrixFinal = np.empty((matrix.size,1))
    for i in range(matrix.size):
        matrixFinal[i] = matrix[i]**2
    print(np.sqrt(matrixFinal.sum()))

#Modulo([1,2,3])
#maximoyminimo([0,1,2],[3,4,5],[6,7,8])
#igualdad([[0,1,2],[3,4,5],[6,7,8]],[[0,1,2],[3,4,5],[6,7,8]])