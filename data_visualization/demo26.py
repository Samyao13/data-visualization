import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(后15).xlsx"
df = pd.read_excel(path, sheet_name='26 柱形圆', header=None,
                   skiprows=2, nrows=6, usecols=[1, 2, 4])
df.columns = ['区域', '销量', '同比去年']
df['销量'] = df['销量'].astype(float)
df['同比去年'] = df['同比去年'].astype(float)
if df['同比去年'].max() <= 1.5:
    df['同比去年'] = df['同比去年'] * 100

fig, ax = plt.subplots(figsize=(12, 7.0))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

x = np.arange(len(df))
vals = df['销量'].values
rates = df['同比去年'].values

bars = ax.bar(x, vals, width=0.32, color='#F04A6E', edgecolor='none')
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width()/2, v + 60, str(int(v)),
            ha='center', va='bottom', fontsize=11, color='white')

bubble_y = max(vals) * 1.22
min_r, max_r = rates.min(), rates.max()
for xi, r in zip(x, rates):
    size = 240 + (r - min_r) / (max_r - min_r) * 1060
    ax.scatter(xi, bubble_y, s=size, color='#2E8FE0',
               edgecolor='none', zorder=5)
    ax.text(xi, bubble_y, f"{int(r)}%", ha='center', va='center',
            fontsize=11, color='white', zorder=6)

ax.set_xticks(x)
ax.set_xticklabels(df['区域'], fontsize=11, color='white')
ax.tick_params(axis='x', colors='white', length=0, pad=8)
ax.set_yticks([])

ax.axhline(0, color='#5A6B8C', linewidth=0.8, alpha=0.6)
for s in ax.spines.values():
    s.set_visible(False)

ax.text(0.02, 1.14, '各区域上半年销量及同比',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='left', va='bottom')
ax.text(0.02, 1.06, '东北区域销量持续保持第一，华东和华南同比去年增长最多',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='left', va='bottom')

fig.text(0.04, 0.03,
         '*注：数据来源于公司销售系统，统计日期截至2022.06.30',
         fontsize=10, color='#8899AA', va='bottom')

ax.set_ylim(0, max(vals) * 1.5)

plt.subplots_adjust(top=0.78, bottom=0.14, left=0.06, right=0.96)
plt.show()