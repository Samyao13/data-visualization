import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(前15).xlsx"
df = pd.read_excel(path, sheet_name='9 对比柱形图', header=1)
df = df.iloc[:, 1:5].dropna(subset=['商品'])
df.columns = ['商品', '2021销量', '2022销量', '差值']

fig, ax = plt.subplots(figsize=(12, 6.8))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

x = np.arange(len(df))
w = 0.22
gap = 0.01

x_left  = x - w/2 - gap
x_right = x + w/2 + gap

ax.bar(x_left,  df['2021销量'], w, color='#1F6FBF')
ax.bar(x_right, df['2022销量'], w, color='#7FA9D0')

for xi, v in zip(x_left, df['2021销量']):
    ax.text(xi, v + 80, str(int(v)), ha='center', va='bottom',
            fontsize=10, color='white')
for xi, v in zip(x_right, df['2022销量']):
    ax.text(xi, v - 80, str(int(v)), ha='center', va='top',
            fontsize=10, color='white')

for i in range(len(df)):
    y1 = df['2021销量'].iloc[i]
    y2 = df['2022销量'].iloc[i]
    yhigh = max(y1, y2)
    ylow  = min(y1, y2)

    xa = x_right[i]

    # 箭头尖端 = 高柱顶上那条深蓝短横线的高度，不超出
    ax.annotate('', xy=(xa, yhigh), xytext=(xa, ylow),
                arrowprops=dict(arrowstyle='-|>', color='white',
                                lw=1.2, mutation_scale=16))

    # 高柱顶深蓝短横线：从左柱顶向右延伸到箭头竖线正上方
    ax.plot([x_left[i], xa], [yhigh, yhigh],
            color='#1F6FBF', linewidth=2.0)

    ax.text(xa + 0.05, (y1 + y2) / 2, str(int(df['差值'].iloc[i])),
            ha='left', va='center', fontsize=10, color='white')

ax.axhline(0, color='white', linewidth=0.6, alpha=0.5)

ax.set_xticks(x)
ax.set_xticklabels(df['商品'], fontsize=11, color='white')
ax.set_yticks([])
ax.tick_params(axis='x', colors='white', length=0, pad=8)
for s in ax.spines.values():
    s.set_visible(False)

ax.add_patch(Rectangle((0.02, 0.88), 0.012, 0.025, transform=ax.transAxes,
                       facecolor='#1F6FBF', edgecolor='none'))
ax.text(0.04, 0.89, '2021销量', transform=ax.transAxes,
        fontsize=9, color='white', va='center')
ax.add_patch(Rectangle((0.10, 0.88), 0.012, 0.025, transform=ax.transAxes,
                       facecolor='#7FA9D0', edgecolor='none'))
ax.text(0.12, 0.89, '2022销量', transform=ax.transAxes,
        fontsize=9, color='white', va='center')

ax.text(0.0, 1.18, '2022年商品对比去年销售情况',
        transform=ax.transAxes, fontsize=20, fontweight='bold',
        color='white', va='bottom')
ax.text(0.0, 1.10, '商品整体比去年销量有所下降，其中隔离下降最多，下降33%',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE', va='bottom')

ax.text(0.0, -0.18, '*注：数据来源于公司销售系统，统计日期截至2022.01.01',
        transform=ax.transAxes, fontsize=9, color='#8899AA', va='top')

plt.subplots_adjust(top=0.82, bottom=0.16, left=0.03, right=0.97)
plt.show()