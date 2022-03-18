import sqlite3

con = sqlite3.connect('aiscpy/DataBases/shapes_AISC.db')
cur = con.cursor()
min = 90
max = 100
cons = cur.execute(
    '''
    SELECT Shape FROM `W-M-S-HP_shapes_AISC`
    WHERE A BETWEEN ? AND ?
    ORDER BY `tf` ASC
    ''', (min, max)
)
lista = []
for i in cons:
    lista.append(i[0])

print(lista)


'''for i in range(len(lista)):
    print(lista[i][0])'''
con.commit()
con.close()


def value_by_A(min, max, order = ''):
    con = sqlite3.connect('aiscpy/DataBases/shapes_AISC.db')
    cur = con.cursor()
    if order != '':
        ordered = 'ORDER BY `'+order+'` ASC'
    else:
        ordered = ''
    cons = cur.execute(
        '''
        SELECT Shape FROM `W-M-S-HP_shapes_AISC`
        WHERE A BETWEEN ? AND ?
        '''+ ordered, (min, max)
    )
    lista = []
    for i in cons:
        lista.append(i[0])

    print(lista)
    con.commit()
    con.close()

value_by_A(90, 100, order='tf')