import numpy as np
import matplotlib.pyplot as plt

def check_vector(lista_vetores):
    comp_x_eq = None
    comp_y_eq = None

    verif = str(type(lista_vetores[0]))
    if verif == "<class 'tuple'>":
        for i in range(len(lista_vetores)):
            x = lista_vetores[i][0]
            y = lista_vetores[i][1]
            comp_x = lista_vetores[i][2] - lista_vetores[i][0]
            comp_y = lista_vetores[i][3] - lista_vetores[i][1]

            if (comp_x_eq == None) and (comp_y_eq == None):
                comp_x_eq = comp_x
                comp_y_eq = comp_y
            else:
                if (comp_x_eq != comp_x) or (comp_y_eq != comp_y):
                    return False
        return True
    else:
        for vector in lista_vetores:
            comp_x = vector[0]
            comp_y = vector[1]
            if (comp_x_eq == None) and (comp_y_eq == None):
                comp_x_eq = comp_x
                comp_y_eq = comp_y
            else:
                if (comp_x_eq != comp_x) or (comp_y_eq != comp_y):
                    return False
        return True


def plot2d(lista_vetores, lista_cores, lista_limites):
    plt.figure()
    plt.axvline(x=0, color='#A9A9A9', zorder=0)
    plt.axhline(y=0, color='#A9A9A9', zorder=0)

    verif = str(type(lista_vetores[0]))
    if verif == "<class 'tuple'>":
        for i in range(len(lista_vetores)):
            plt.quiver([lista_vetores[i][0]],
                       [lista_vetores[i][1]],
                       [lista_vetores[i][2] - lista_vetores[i][0]],
                       [lista_vetores[i][3] - lista_vetores[i][1]],
                       angles='xy', scale_units='xy', scale=1, color=lista_cores[i],
                       alpha=1)
    else:
        for i in range(len(lista_vetores)):
            x = np.concatenate([[0, 0], lista_vetores[i]])
            plt.quiver([x[0]],
                       [x[1]],
                       [x[2]],
                       [x[3]],
                       angles='xy', scale_units='xy', scale=1, color=lista_cores[i],
                       alpha=1)



    plt.grid()
    plt.axis([lista_limites[0],lista_limites[1],lista_limites[2],lista_limites[3]])
    plt.show()

def plot3d(lista_vetores, lista_cores, lista_limites):
    fig = plt.figure()
    ax = fig.gca(projection='3d')[-10,10,-10,10]
    ax.set_xlim3d(lista_limites[0], lista_limites[1])
    ax.set_ylim3d(lista_limites[2], lista_limites[3])
    ax.set_zlim3d(lista_limites[4], lista_limites[5])
    i = 0
    for vector in lista_vetores:
        ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], length=1, normalize=False, color=lista_cores[i])
        i += 1
    plt.show()
