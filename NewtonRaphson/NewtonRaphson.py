'''
Newton Raphson Method 
Language: Python

Motahare Soltani 
soltani.wse@gmail.com

Parameters
----------
f(x) : function
        The function for which we are trying to approximate a solution f(x)=0.

df : Derivative of the function (f) 

xm_list : It Uses for an initial guess of the root.

N : number of iterations

eps : Acceptable Error

Epsilon : (xm_list(new)-xm_list(old))/xm_list(new))*100

x0 : an initial guess of the root

'''
import numpy as np
import sympy as sp
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from matplotlib.pyplot import *


# Define the function whose roots are required
def f(x):
    return sp.sqrt(x) - sp.cos(x)

'''X = sp.Symbol('x')
print(sp.diff(f(X)))'''

def df(x):
        return 2 * x-np.power(2,x) * np.log(2)


# Input Parameters
N = 50           # Max. number of iterations
eps = 5          # Acceptable Error 
x0 = -0.5

# Input lists
xm_list = [x0]
Epsilon = []
f_list = [f(x0)]


for i in range(1,N):
        xm_list.append(xm_list[i-1] - (f(xm_list[i-1]) / df(xm_list[i-1])))
        f_list.append(f(xm_list[i]))
       
        #Estimated Relative Error
        Epsilon.append((abs( (xm_list[i] - xm_list[i-1]) / xm_list[i]) * 100)) 

        if Epsilon[i-1] < eps:
                break

print(Epsilon)
#Table
columns = ["Iteration", "xm", "Epsilon%", "f(xm)"]
  
Table = PrettyTable()
  
# Add Columns
Table.add_column(columns[0], range(1,i+1))
Table.add_column(columns[1], [round(num, 4) for num in xm_list][:i])
Table.add_column(columns[2], [round(num, 4) for num in Epsilon][:i])
Table.add_column(columns[3], [round(num, 8) for num in f_list][:i])

print(Table)
print('Root found : '+str(xm_list[i]))


#Plot
fig = figure(figsize=(8, 8), dpi=75)

plt.subplot(2,1,1)
x = np.arange(xm_list[i-1]-0.5,xm_list[i]+0.5,0.00001)
y = f(x)
font1 = {'color':'blue','size':15}

plt.annotate('Root ≈ '+str(np.round(xm_list[i],5)), xy=(xm_list[i], f(xm_list[i])),xytext=(xm_list[i]+0.1, f(xm_list[i])+0.05), arrowprops=dict(facecolor='blue', shrink=0.05))
plt.plot(x, y, 'b-', linewidth=3)
plt.scatter(xm_list[i],f(xm_list[i]), c='purple', s=100,alpha=0.5)
plt.xlabel('X', fontsize=12)
plt.ylabel('Function', fontsize=12)
plt.title('y = f(x)', fontdict=font1, loc='left')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

plt.subplot(2,1,2)
x = np.arange(1,i+1)
y = Epsilon
font2 = {'color':'red','size':15}
text = plt.text((i+1)/2, Epsilon[0]/2, 'Epsilon% = '+str(np.round(Epsilon[i-1],5))+'\n\nRoot ≈'+str(np.round(xm_list[i],7))+'\n\nf(xm) ='+str(np.round(f(xm_list[i]),10)), fontsize=16,horizontalalignment='center',verticalalignment='center')
text.set_bbox(dict(facecolor='papayawhip', alpha=0.6, edgecolor='papayawhip'))
plt.plot(x, y, 'r-', linewidth=3)
plt.xlabel('Iteration', fontsize=12)
plt.ylabel('Error(%)', fontsize=12)
plt.title('Convergence Diagram', fontdict=font2, loc='left')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()

