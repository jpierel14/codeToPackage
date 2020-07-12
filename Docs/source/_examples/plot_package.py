"""
===================
Basic Functionality
===================

Just a docs implementation example.
"""
		
###############################################################
# This is just an example of what you can do with the 
# documentation generated automatically by codetopacakge. For an
# example of how to actually implement codetopackage, see the 
# :ref:`examples:Creating a Python Package` part of the docs.
   
import matplotlib.pyplot as plt
import numpy as np

print('Hello World!')
x=np.linspace(0,2*np.pi,1000)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)