import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(后15).xlsx"
df = pd.read_excel(path, sheet_name='23 柱形折线图', header=None,
                   skiprows=2, nrows=6, usecols=[1, 2, 3])
df.columns = ['年份', '销售量', '同比']
df['销售量'] = df['销售量'].astype(float)
df['同比'] = df['同比'].astype(float)
if df['同比'].max() <= 1.5:
    df['同比'] = df['同比'] * 100

fig, ax = plt.subplots(figsize=(12, 7.0))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

x = np.arange(len(df))
vals = df['销售量'].values
rates = df['同比'].values

# 柱形
ax.bar(x, vals, width=0.42, color='#1F6FBF', edgecolor='none')
for xi, v in zip(x, vals):
    ax.text(xi, v + 60, str(int(v)), ha='center', va='bottom',
            fontsize=10, color='white')

# 折线
ax2 = ax.twinx()
ax2.plot(x, rates, color='#F0406E', marker='o', markersize=8,
         linewidth=2.0, markerfacecolor='#F0406E',
         markeredgecolor='#F0406E', zorder=10)
for xi, r in zip(x, rates):
    ax2.text(xi, r + 1.5, f"{int(r)}%", ha='center', va='bottom',
             fontsize=10, color='white')

# 轴范围：让折线整体更高、柱形更低
ax.set_ylim(0, 10000)        # 柱形只占下方
ax2.set_ylim(-35, 60)        # 折线数据 5~35 -> 落在约 6400~8500，全在柱顶之上

ax.set_xticks(x)
ax.set_xticklabels(df['年份'].astype(int), fontsize=11, color='white')
ax.tick_params(axis='x', colors='white', length=0, pad=8)
ax.set_yticks([])
ax2.set_yticks([])

for s in ax.spines.values():
    s.set_visible(False)
for s in ax2.spines.values():
    s.set_visible(False)

legend_elements = [
    Rectangle((0, 0), 1, 1, facecolor='#1F6FBF', edgecolor='none'),
    Line2D([0], [0], color='#F0406E', marker='o',
           markersize=6, linewidth=2),
]
ax.legend(legend_elements, ['销售量', '同比'],
          loc='upper right', bbox_to_anchor=(0.98, 0.97),
          frameon=False, fontsize=11, labelcolor='white',
          handlelength=1.6)

ax.text(0.02, 0.96, '近六年销售量及增长率',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='left', va='top')
ax.text(0.02, 0.90, '平台销量近6年持续增长，但近两年增长率有所放缓',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='left', va='top')

# 底部注释放整张图最底端，不跟柱子重叠
fig.text(0.04, 0.03, '*注：数据来源于公司销售系统',
         fontsize=10, color='#8899AA', va='bottom')

plt.subplots_adjust(top=0.86, bottom=0.12, left=0.04, right=0.96)
plt.show()