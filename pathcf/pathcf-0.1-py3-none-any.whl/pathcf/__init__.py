
def pathcf(x):
    s2=x
    s3=s2.replace('\\','/')
    print( 'pd.read_csv'+'('+'r'+'"'+s3+'"'+')')