"""
===================
Basic Functionality
===================

Basic usage of the codetopackage package.
"""
		
###############################################################
# This is just an example of what you can do with the 
# documentation generated automatically by codetopacakge.
   
import codetopackage
import matplotlib.pyplot as plt
import numpy as np

print('Hello World!')
x=np.linspace(0,2*np.pi,1000)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)