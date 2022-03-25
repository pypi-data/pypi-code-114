import translators as ts


# Função de tradução Português => Inglês
def pt_en(text):
    texto = ts.google(text, from_language='pt', to_language='en')
    return texto


#print(pt_en('O que você quer traduzir para português'))
