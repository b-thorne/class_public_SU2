import sys
import numpy as np
import matplotlib.pyplot as plt

fname = str(sys.argv[1])

cls = np.loadtxt(fname, unpack = True)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.loglog(np.abs(cls[sys.argv[2]]))
plt.show()
