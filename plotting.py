import matplotlib.pyplot as plt
import numpy as np

dat = np.loadtxt('output/explanatory02_cl.dat',unpack=True)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

l = np.copy(dat[0])
#ax.plot(dat[0],dat[4]/(l*(l+1.)),label='EE')
#ax.plot(dat[0],dat[8]/(l*(l+1.)),label='TB',linestyle='--')
#ax.plot(dat[0],dat[9]/(l*(l+1.)),label='EB',linestyle='-.')

for i,d in enumerate(dat[1:]):
    ax.plot(l,d/(l*(l+1.)),label='%d'%i)

ax.legend()
ax.set_yscale('log')
plt.show()
