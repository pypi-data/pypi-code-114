import mylib_donghao.myNN as NN
import torch
from torch.autograd import Variable
import numpy as np
import myMatrix
import myDimReduce
import myRBM
from myMatrix import myMatrix
import basic_function as bf
from myPerceptron import *

model = NN.myNetwork([ ["Linear", [2, 3, False]] , ["softmax"], ["Linear", [3, 3, False]] , ["softmax"] ])
l = [[2, 3], [3, 2], [2, 1]]
y = [[1, 0, 0], [1, 0, 0], [0, 0, 1]]
for i in range(500):
    model.training_of_single_batch(model.expected_input(l), model.expected_input(y))
print(model.forward_input_list_or_numpy(l))

layer1 = ["CNN", [1, 2, 3, 2, 0]]
layer2 = ["CNN", [2, 4, 5, 3, 2]]
layer3 = ["batchnorm2d", [4, None, None, None]]
model2 = NN.myNetwork([layer1, layer2, layer3])
r = torch.rand([2, 1, 16, 16])
print(model2.forward(r))

mm = myRBM.RBM(5, 3)
mm.a.print()
mm.b.print()
for i in range(100):
    mm.train(myMatrix([[0, 1, 0, 1, 1]]).transpose(), 0.01)
    mm.train(myMatrix([[0, 1, 1, 1, 1]]).transpose(), 0.01)
#    mm.train(myMatrix([[1, 1, 0, 1, 1]]).transpose(), 0.01)
#    mm.train(myMatrix([[0, 0, 0, 0, 1]]).transpose(), 0.01)
#    mm.train(myMatrix([[1, 1, 1, 1, 1]]).transpose(), 0.01)
mm.a.print()
mm.b.print()
mm.visibled(mm.hiddened(myMatrix([[0], [1], [0], [1], [1]]))).print()

print("-------------------------------")
a = myPerceptron(2, 1)
loader = myMatrixLoader()
loader.append(myMatrix([[2, 3], [-2, 3]]).transpose(), myMatrix([[1, 1]]))
loader.append(myMatrix([[-2, -3], [2, -3]]).transpose(), myMatrix([[-1, -1]]))
a.forward(loader.matlist[0]).print()
a.forward(loader.matlist[1]).print()
a.forward(loader.matlist[2]).print()
a.forward(loader.matlist[3]).print()
a.train(loader, 0.01, 10000)
a.forward(loader.matlist[0]).print()
a.forward(loader.matlist[1]).print()
a.forward(loader.matlist[2]).print()
a.forward(loader.matlist[3]).print()









