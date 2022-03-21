def createDofile(doscript):
    f = open('pystata_song.do','w')
    f.write('import delimited "dataframe.csv", encoding(ISO-8859-9) clear'+'\n')
    for ele in doscript:
        f.write(ele+'\n')

def runDofile(doscript,dataframe):
    import os 
    dataframe.to_csv('dataframe.csv')
    createDofile(doscript)
    os.system('stata /e do pystata_song.do')
        
    with open(r'pystata_song.log') as f:
        lines = f.readlines()
        for row in lines:
            print(row.strip('\n'))