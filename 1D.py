import numpy as np
import matplotlib.pyplot as plt

def D1(N):
    N=5
    C=3
    L=10
    Dx=L/N
    a=[1,-2,1]+[0]*(N-2)
    A=[[1]+[0]*N]
    for i in range(1,N):
        A.append(a)
        a=[0]+a
        a.pop(-1)
    A.append([0]*N+[1])
    B= np.array([0]+[C*(Dx)**2]*(N-1)+[1])
    y = np.linalg.solve(A, B)
    x = np.linspace(0,L,N+1)
    t = np.linspace(0, L, 10*N)
    z = [C/2*(i)**2 + (1/L-C*L/2)*i for i in t]
    plt.plot(x,y,label="approx")
    plt.plot(t,z,label = 'solution')
    plt.legend()
    plt.show()

