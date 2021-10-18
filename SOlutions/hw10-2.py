import matplotlib.pyplot as plt


import pandas as pd

df=pd.read_csv('cities.csv')

import numpy as np
x = df['longd']
y = df['latd']

colors=np.log10(df['population_total'])

sizes = df['area_total_sq_mi']

plt.scatter(x, y, 
            c=colors, s=sizes,
            alpha=0.5,
            cmap='jet')
            
plt.xlabel('longitude')
plt.ylabel('latitude')

plt.title('Cities: Area and Population')
#show color bar
cb = plt.colorbar()
#Label for color bar
cb.set_label('log 10(population)') 
plt.clim(3,7)

plt.show()