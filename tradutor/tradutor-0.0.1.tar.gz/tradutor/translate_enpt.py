import translators as ts


# Função de tradução Inglês => Português
def en_pt(text):
    new_text = ts.google(text, from_language='en', to_language='pt')
    return new_text

#print(en_pt('what you want translate to portuguese '))
