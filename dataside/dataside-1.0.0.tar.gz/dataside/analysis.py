import pandas as pd
from termcolor import colored


def exploratory(dataset):
    print(colored('AMOSTRA DAS 5 PRIMEIRAS LINHAS DO DATASET', "blue"))
    dataset.head()
    print('\n')
    print(colored('DESCRIÇÃO ESTATISTICA DO DATASET', "blue"))
    dataset.describe()
    print('\n')
    print(colored('LINHAS X COLUNAS', "blue"))
    print(f"O seu dataset contém:\ntotal de linhas = {dataset.shape[0]}, \nTotal de colunas = {dataset.shape[1]}")
    print('\n')
    print(colored('INFORMAÇÕES SOBRE AS COLUNAS', "blue"))
    dataset.info()
    print('\n')
    print(colored('CONTAGEM DE VALORES NÃO NULOS', "blue"))
    print(dataset.isna().count())
