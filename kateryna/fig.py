import pandas as pd
import matplotlib.pyplot as plt
pt = pd.read_csv("/Users/maxwellcorbin/Periodic-table/Periodic-table/periodic_table.csv")

fig, ax = plt.subplots(nrows=2, ncols=1)
fig.set_size_inches(10, 10)
ax[0].set_facecolor('red')
ax[0].plot(pt.AtomicMass, pt.AtomicNumber)
ax[1].plot(pt.AtomicMass, pt.AtomicNumber, markersize=1)
fig.savefig("./my_fig3.png")

