def calcular(preco, taxa, casas_decimais=2):

    assert type(preco) in [float, int] and preco > 0
    assert type(taxa) in [float, int] and taxa > 0
    assert type(casas_decimais) == int and casas_decimais >= 0

    preco_com_taxa = preco * 100 / (100 - taxa)
    return round(preco_com_taxa, casas_decimais)

if __name__ == '__main__':

    preco = float(input('Digite o valor que deseja obter com a venda: R$ ').replace(',', '.'))
    taxa = float(input('Taxa total cobrada pela maquina de cartão: ').replace(',', '.'))
    valor_a_ser_cobrado = str(calcular(preco, taxa)).replace('.', ',')
    
    print(f'Valor a ser cobrado: R$ {valor_a_ser_cobrado}')