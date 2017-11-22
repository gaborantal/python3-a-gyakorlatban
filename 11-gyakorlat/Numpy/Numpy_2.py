import numpy as np 

a = np.array([0,30,45,60,90]) 

sin = np.sin(a*np.pi/180) 
#print(sin)

tan = np.tan(a*np.pi/180) 
#print(tan)

ceil_sin = np.ceil( np.sin([20,30,40,50]) )
floor_tan = np.floor(np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0]))
recip = np.reciprocal(5.0)
pow_ex = np.power(2,4)
mod_ex = np.mod(16,7)
std_dev_ex = np.std(a)
#print(ceil_sin, floor_tan, float(recip), pow_ex, mod_ex, std_dev_ex)

b = np.array([[30,65,70],[80,95,10],[50,90,60]]) 
med = np.median(b) 
mean = np.mean(b)
#print(b)
#print(med, mean)


c = np.array([[6,1,1], [4, -2, 5], [2,8,7]]) 
"""print(c)
print(np.linalg.det(c))
print(6*(-2*7 - 5*8) - 1*(4*7 - 5*2) + 1*(4*8 - -2*2))"""