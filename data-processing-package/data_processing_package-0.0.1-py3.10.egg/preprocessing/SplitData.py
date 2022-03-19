def splitTrainTestSets(X, y, testSize):
    print("Separando conjuntos de teste e treino...")
    from sklearn.model_selection import train_test_split
    XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size = testSize)
    print("ok!")
    return XTrain, XTest, yTrain, yTest

    
