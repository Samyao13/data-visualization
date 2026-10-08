import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(后15).xlsx"
df = pd.read_excel(path, sheet_name='27 簇状柱形折线图', header=None,
                   skiprows=2, nrows=6, usecols=[1, 2, 3, 4])
df.columns = ['区域', '2022销量', '2021销量', '同比去年']
for c in ['2022销量', '2021销量', '同比去年']:
    df[c] = df[c].astype(float)
if df['同比去年'].max() <= 1.5:
    df['同比去年'] = df['同比去年'] * 100

fig, ax = plt.subplots(figsize=(12, 7.0))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

x = np.arange(len(df))
w = 0.28
vals22 = df['2022销量'].values
vals21 = df['2021销量'].values
rates = df['同比去年'].values

ax.bar(x - w/2 - 0.01, vals22, width=w, color='#2E8FE0',
       edgecolor='none', zorder=2)
ax.bar(x + w/2 + 0.01, vals21, width=w, color='#F04A6E',
       edgecolor='none', zorder=2)

for xi, v in zip(x - w/2 - 0.01, vals22):
    ax.text(xi, v + 30, str(int(v)), ha='center', va='bottom',
            fontsize=10, color='white')
for xi, v in zip(x + w/2 + 0.01, vals21):
    ax.text(xi, v + 30, str(int(v)), ha='center', va='bottom',
            fontsize=10, color='white')

ax2 = ax.twinx()
ax2.plot(x, rates, color='#F5C518', marker='o', markersize=6,
         linewidth=1.8, markerfacecolor='#F5C518',
         markeredgecolor='#F5C518', zorder=10)
for xi, r in zip(x, rates):
    ax2.text(xi, r + 1.0, f"{int(r)}%", ha='center', va='bottom',
             fontsize=10, color='white')

# 关键参数：柱形更高、折线上移
ax.set_ylim(0, 9000)          # 柱形更长
ax2.set_ylim(-80, 60)         # 折线上移

ax.set_xticks(x)
ax.set_xticklabels(df['区域'], fontsize=11, color='white')
ax.tick_params(axis='x', colors='white', length=0, pad=8)
ax.set_yticks([])
ax2.set_yticks([])

ax.axhline(0, color='#5A6B8C', linewidth=0.8, alpha=0.6)
for s in ax.spines.values():
    s.set_visible(False)
for s in ax2.spines.values():
    s.set_visible(False)

# 图例：下移，露出 2361
x_last = x[-1] + w/2 + 0.01
y_top = vals21[-1]           # 2361 的柱顶
ax.add_patch(Rectangle((x_last - 0.15, y_top - 700), 0.30, 420,
                       facecolor='#1B2A4A',
                       edgecolor='#2E8FE0', linewidth=1.5, zorder=8))
ax.text(x_last, y_top - 490, '2022', ha='center', va='center',
        fontsize=10, color='white', zorder=9)
ax.add_patch(Rectangle((x_last - 0.15, y_top - 1180), 0.30, 420,
                       facecolor='#1B2A4A',
                       edgecolor='#F04A6E', linewidth=1.5, zorder=8))
ax.text(x_last, y_top - 970, '2021', ha='center', va='center',
        fontsize=10, color='white', zorder=9)

ax.text(0.5, 1.16, '上半年各月商品销量同比去年情况',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='center', va='bottom')
ax.text(0.5, 1.08, '2022年相比于2021年销量都有提升，半年整体提升17%',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='center', va='bottom')

fig.text(0.04, 0.03,
         '*注：数据来源于公司销售系统，统计日期截至2022.06.30',
         fontsize=10, color='#8899AA', va='bottom')

plt.subplots_adjust(top=0.80, bottom=0.14, left=0.04, right=0.96)
plt.show()