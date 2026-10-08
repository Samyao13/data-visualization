import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(后15).xlsx"
df = pd.read_excel(path, sheet_name='25 子弹图', header=None,
                   skiprows=3, nrows=6, usecols=[1, 2, 3, 4, 5, 6])
df.columns = ['商品', '实际', '目标', '及格', '良好', '优秀']
for c in ['实际', '目标', '及格', '良好', '优秀']:
    df[c] = df[c].astype(float)

fig, ax = plt.subplots(figsize=(12, 7.0))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

x = np.arange(len(df))
w_bg = 0.42
w_fg = 0.16      # 实际柱宽 = 目标黄条宽

ax.bar(x, df['及格'], width=w_bg, color='#7FA9D0', edgecolor='none', zorder=2)
ax.bar(x, df['良好'], width=w_bg, bottom=df['及格'],
       color='#29B8B0', edgecolor='none', zorder=2)
ax.bar(x, df['优秀'], width=w_bg, bottom=df['及格'] + df['良好'],
       color='#1F6FBF', edgecolor='none', zorder=2)

# 实际柱
ax.bar(x, df['实际'], width=w_fg, color='#2E8FE0',
       edgecolor='none', zorder=4)

# 目标黄条：宽度 = 实际柱宽
for xi, v in zip(x, df['目标']):
    ax.plot([xi - w_fg/2, xi + w_fg/2], [v, v],
            color='#F5B324', linewidth=5,
            solid_capstyle='butt', zorder=5)

ax.set_yticks([0, 200, 400, 600, 800, 1000, 1200])
ax.set_yticklabels(['0', '200', '400', '600', '800', '1000', '1200'],
                   fontsize=10, color='white')
ax.tick_params(axis='y', colors='white', length=0)

ax.set_xticks(x)
ax.set_xticklabels(df['商品'], fontsize=11, color='white')
ax.tick_params(axis='x', colors='white', length=0, pad=8)

ax.axhline(0, color='#5A6B8C', linewidth=0.8, alpha=0.6)
for s in ax.spines.values():
    s.set_visible(False)

legend_elements = [
    Rectangle((0, 0), 1, 1, facecolor='#7FA9D0'),
    Rectangle((0, 0), 1, 1, facecolor='#29B8B0'),
    Rectangle((0, 0), 1, 1, facecolor='#1F6FBF'),
    Rectangle((0, 0), 1, 1, facecolor='#2E8FE0'),
    Line2D([0], [0], color='#F5B324', linewidth=5),
]
ax.legend(legend_elements, ['及格', '良好', '优秀', '实际', '目标'],
          loc='upper center', bbox_to_anchor=(0.5, 1.00),
          frameon=False, fontsize=10, labelcolor='white',
          ncol=5, handlelength=1.3, columnspacing=1.5)

ax.text(0.02, 1.10, '2022年上半年各商品销量完成情况',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='left', va='bottom')
ax.text(0.02, 1.03, '防晒整体销量最好，达到856，面霜远超目标，超额完成30%',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='left', va='bottom')

fig.text(0.04, 0.03,
         '*注：数据来源于公司销售系统，统计日期截至2022.06.30',
         fontsize=10, color='#8899AA', va='bottom')

ax.set_ylim(0, 1250)

plt.subplots_adjust(top=0.78, bottom=0.14, left=0.06, right=0.96)
plt.show()