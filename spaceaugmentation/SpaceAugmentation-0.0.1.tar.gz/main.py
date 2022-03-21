# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import Augmentation

import numpy as np


list_1 = [np.random.uniform(0.0,1.0,size=(768,)) ,np.random.uniform(0.0,1.0,size=(768,)),np.random.uniform(0.0,1.0,size=(768,)),np.random.uniform(0.0,1.0,size=(768,))]
list_2 = [0,1,0,0]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Before Augmentation", "Train Embed size",len(list_1), "Train Label size" ,len(list_2))
    ag = Augmentation.Augmentation()
    #l1, l2 = ag.add_noise(list_1, list_2)
    l1, l2 = ag.delta_S(list_1, list_2,0)
    print("After Augmentation", "Train Embed size",len(l1), "Train Label size" ,len(l2))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
