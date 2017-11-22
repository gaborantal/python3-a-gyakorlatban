from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np


# 1-D interpolation

x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')

xnew = np.linspace(0, 10, num=41, endpoint=True)
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()




from scipy import interpolate

x = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
y = np.sin(x)
tck = interpolate.splrep(x, y, s=0)
xnew = np.arange(0, 2*np.pi, np.pi/50)
ynew = interpolate.splev(xnew, tck, der=0)

plt.figure()
plt.plot(x, y, 'x', xnew, ynew, xnew, np.sin(xnew), x, y, 'b')
plt.legend(['Linear', 'Cubic Spline', 'True'])
plt.axis([-0.05, 6.33, -1.05, 1.05])
plt.title('Cubic-spline interpolation')
plt.show()



import numpy as np
from scipy import linalg
A = np.array([[1, 2], [3, 4]])
b = np.array([[5], [6]])
print(linalg.inv(A).dot(b))  # slow
print(A.dot(linalg.inv(A).dot(b)) - b)  # check
print(np.linalg.solve(A, b))  # fast
print(A.dot(np.linalg.solve(A, b)) - b)  # check