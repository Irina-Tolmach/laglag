import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

t = pd.read_csv('trees.csv')

g = t.sort_values('Girth')
x = np.arange(len(t['ID']))
plt.title('Girth')
plt.plot(x, g['Girth'])
plt.show()
plt.bar(x, g['Girth'])
plt.show()

h = t.sort_values('Height')
x = np.arange(len(t['ID']))
plt.title('Height')
plt.plot(x, h['Height'])
plt.show()
plt.bar(x, h['Height'])
plt.show()

v = t.sort_values('Volume')
x = np.arange(len(t['ID']))
plt.title('Volume')
plt.plot(x, v['Volume'])
plt.show()
plt.bar(x, v['Volume'])
plt.show()
