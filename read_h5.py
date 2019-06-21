import sys
import h5py
import matplotlib.pyplot as plt
import numpy as np

filename = sys.argv[1]

f = h5py.File(filename,'r')


plt.subplot(211)
plt.plot(f['elapsed_t'], f['x'])
plt.ylabel('x')
plt.grid('on')
plt.subplot(212)
plt.plot(f['elapsed_t'], f['y'])
plt.ylabel('y')
plt.xlabel('t')
plt.grid('on')
plt.show()
