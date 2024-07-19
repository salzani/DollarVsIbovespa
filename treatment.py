from Dollar_info import dollarData
from Ibovespa_info import ibovespaData

import matplotlib.pyplot as plt
import mplcyberpunk


plt.style.use("cyberpunk")


fig, ax1 = plt.subplots(figsize=(12, 6))


color = 'tab:red'
ax1.set_xlabel('Mês')
ax1.set_ylabel('USD/BRL', color=color)
ax1.plot(dollarData.index, dollarData['Adj Close'], marker='o', linestyle='-', color=color, label='USD/BRL')
ax1.tick_params(axis='y', labelcolor=color)


ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Ibovespa', color=color)
ax2.plot(ibovespaData.index, ibovespaData['Adj Close'], marker='o', linestyle='-', color=color, label='Ibovespa')
ax2.tick_params(axis='y', labelcolor=color)


plt.title('USD/BRL e Ibovespa Mensal em 2023')
ax1.tick_params(axis='x', rotation=45)


ax1.legend(loc='upper left', bbox_to_anchor=(0.1, 1.1))
ax2.legend(loc='upper right', bbox_to_anchor=(0.1, 1.1))

mplcyberpunk.add_glow_effects(ax1)
mplcyberpunk.add_glow_effects(ax2)


plt.show()
