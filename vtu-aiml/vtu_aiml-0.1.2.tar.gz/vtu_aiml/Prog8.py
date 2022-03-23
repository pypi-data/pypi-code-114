'''

8. Write a program to implement k-Nearest Neighbour algorithm to classify the iris data set. Print
both correct and wrong predictions. Java/Python ML library classes can be used for this problem.

'''

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split
iris_dataset=load_iris()
X_train,X_test,Y_train,Y_test=train_test_split(iris_dataset["data"],iris_dataset["target"],random_state=0)
kn=KNeighborsClassifier(n_neighbors=1)
kn.fit(X_train,Y_train)
print("\nActual and Predicted values for testsets \n")
for i in range(len(X_test)):
    x=X_test[i]
    x_new=np.array([x])
    prediction=kn.predict(x_new)
    print("\nActual :{0}{1},predicted:{2}{3}".format(Y_test[i],iris_dataset["target_names"][[Y_test[i]]],prediction,iris_dataset["target_names"][prediction]))
    print("\nTest score[Accuracy]:{:.2f}\n".format(kn.score(X_test,Y_test)))