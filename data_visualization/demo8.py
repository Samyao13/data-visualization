import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(前15).xlsx"
df = pd.read_excel(path, sheet_name='8 数值百分比', header=1)
df = df.iloc[:, 1:6].dropna(subset=['区域'])
df.columns = ['区域', '销量', '占位1', '占位2', '同比去年']

df = df.sort_values('销量', ascending=False).reset_index(drop=True)

fig, ax = plt.subplots(figsize=(12, 6.8))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

n = len(df)
y = np.arange(n)[::-1]

max_val = df['销量'].max()
bar_total = 0.70

for i, (_, row) in enumerate(df.iterrows()):
    ypos = y[i]
    v = row['销量']
    r = row['同比去年']

    w1 = (v / max_val) * bar_total * 0.65
    ax.barh(ypos, w1, height=0.55, left=0.18,
            color='#1F4E79', edgecolor='none')

    w2 = bar_total * 0.65 - w1
    ax.barh(ypos, w2, height=0.55, left=0.18 + w1,
            color='#7FA9D0', edgecolor='none')

    ax.text(0.18 + w1 / 2, ypos, str(int(v)),
            ha='center', va='center', fontsize=11, color='white')

    w3 = bar_total * 0.30
    x3 = 0.18 + bar_total * 0.65
    color = '#7B2A34' if r < 0 else '#2A6E3A'
    ax.barh(ypos, w3, height=0.55, left=x3, color=color, edgecolor='none')
    ax.text(x3 + w3 / 2, ypos, f"{r:.1%}",
            ha='center', va='center', fontsize=11, color='white')

    ax.text(0.14, ypos, row['区域'], ha='right', va='center',
            fontsize=12, color='white')

ax.text(0.02, 1.12, '2021年各区域销量及同比情况',
        transform=ax.transAxes, fontsize=20, fontweight='bold',
        color='white', va='bottom')
ax.text(0.02, 1.04, '各区域商品销量同比去年均有下降，其中华南下降最多，同比下降20.8%',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE', va='bottom')

ax.text(0.02, -0.10, '*注：数据来源于公司销售系统，统计日期截至2022.01.01',
        transform=ax.transAxes, fontsize=9, color='#8899AA', va='top')

ax.set_xlim(0, 1)
ax.set_ylim(-0.6, n - 0.4)
ax.set_yticks([])
ax.set_xticks([])
for s in ax.spines.values():
    s.set_visible(False)
plt.subplots_adjust(top=0.84, bottom=0.12, left=0.02, right=0.98)
plt.show()