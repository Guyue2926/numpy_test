import numpy as np

import matplotlib.pyplot as plt

B=np.array([[1],[2],[2],[3]])

A=np.array([[1,1],[1,2],[1,3],[1,4]])

X=A[:,0]

Y=A[:,1]

AA=np.dot(A.T,A)

AB=np.dot(A.T,B)

x=np.linalg.solve(AA,AB)

x2=np.linspace(0,4,66)

y2=x[0]*x2+x[1]

plt.plot(x2,y2,'r')

plt.plot(Y,B,'m',lw=0,marker='o')

plt.show()
#


