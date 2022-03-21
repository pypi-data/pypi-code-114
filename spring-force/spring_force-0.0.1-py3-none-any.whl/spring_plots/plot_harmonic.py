import matplotlib.pyplot as plt
import random
import math


def plot_harmonic_oscillator(m,k,A):
    x = []
    omega = (k / m) ** 0.5
    t = []
    while len(t) <= 100:
        t_i = random.randint(0, 100)
        if t_i not in t:
            t.append(t_i)
            t.sort()

    for i in t:
        X = A * math.cos(omega * i)
        x.append(X)


    plt.plot(t, x)
