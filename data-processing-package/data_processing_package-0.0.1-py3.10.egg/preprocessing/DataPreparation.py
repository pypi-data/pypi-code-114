import pandas as pd
import numpy as np
def loadDataset(file):
    df = pd.read_csv(file)
    X = df.iloc[:,:-1].values
    y = df.iloc[:,-1].values
    return X, y

def fillMissingData(X):
    print("Preenchendo dados que estão faltando...")
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(missing_values=np.nan, strategy='median')
    X[:,1:] = imputer.fit_transform(X[:,1:])
    print("ok!")
    return X

def computeNormalization(X):
    print("Computando Normalização...")
    from sklearn.preprocessing import StandardScaler
    scaleX = StandardScaler()
    X = scaleX.fit_transform(X)
    print("ok!")
    return X
