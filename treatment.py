from Dollar_info import dataDollar
from Ibovespa_info import data

import matplotlib.pyplot as plt
import mplcyberpunk

plt.style.use("cyberpunk")

fig, ax1 = plt.subplots(figsize=(12, 6))

color = 'tab:red'

ax1.set_ylabel('USD/BRL',
               color=color,
               labelpad=20)

ax1.plot(dataDollar.index,
         dataDollar, marker='o',
         linestyle='-', color=color,
         label='USD/BRL')

ax1.tick_params(axis='y',
                labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'

ax2.set_ylabel('Ibovespa',
               color=color,
               labelpad=15)

ax2.plot(data.index,
         data, marker='o',
         linestyle='-', color=color,
         label='Ibovespa')

ax2.tick_params(axis='y', labelcolor=color)

plt.title('USD/BRL e Ibovespa nos últimos 10 anos', fontweight='bold')

ax1.tick_params(axis='x', rotation=45)

ax1.legend(loc='upper left', bbox_to_anchor=(0.1, 1.1))
ax2.legend(loc='upper right', bbox_to_anchor=(0.1, 1.1))

plt.grid(False)

mplcyberpunk.add_glow_effects(ax1)
mplcyberpunk.add_glow_effects(ax2)
plt.show()
