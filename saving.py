import numpy as np
import os
x=np.arange(16).reshape(4,4)
header='c1 c2 c3 c4'
np.savetxt('anu.txt',x,fmt="%d" ,header=header)
print("\n after loading content of the textfile:")
print(np.loadtxt('anu.txt'))