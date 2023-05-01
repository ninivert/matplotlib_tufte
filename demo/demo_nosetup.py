from matplotlib_tufte import *
import matplotlib.pyplot as plt

# by default, will use gca
# this is however discouraged
plt.plot([0,1,2],[-2,4,5])
despine()
data_lim()
breathe()
plt.savefig('fig_nosetup.png')