import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

if __name__ == '__main__':
    N = float(input('Population Size = '))
    t = int(input('Unit Time in days = '))
    t = np.linspace(0, t)
    beta = float(input('β = '))
    eps = float(input('γ = '))
    eps = eps/10
    Io = float(input('Io = '))
    fiN = float(input('μN = '))
    fiN = N * fiN
    fiS = float(input('μS = '))
    fiI = float(input('μI = '))
    fiR = float(input('μR = '))
    Ro = 0
    So = N - Io - Ro

    def calcGraph(y, t, N, beta, eps):
        S, I, R = y
        dsdt = fiN - fiS - beta * S * I / N
        didt = beta * S * I / N - eps * I - fiI
        drdt = eps * I + fiR
        # dsdt = (fi * N - fi * S) - beta * S * I / N
        # didt = beta * S * I / N - eps * I - (fi * I)
        # drdt = eps * I - (1)
        return dsdt, didt, drdt

    y0 = So, Io, Ro
    ret = odeint(calcGraph, y0, t, args=(N, beta, eps))
    S, I, R = ret.T
    # plotting different subplots
    fig = plt.figure(facecolor='w')
    ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
    ax.plot(t, S/10000, 'b', alpha=0.5, lw=2, label='Susceptible')
    ax.plot(t, I/10000, 'r', alpha=0.5, lw=2, label='Infected')
    ax.plot(t, R/10000, 'g', alpha=0.5, lw=2, label='Recovered')
    ax.set_xlabel('Time /days')
    ax.set_ylabel('Number')
    ax.set_ylim(0, 1.2)
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        ax.spines[spine].set_visible(False)
    plt.show()


