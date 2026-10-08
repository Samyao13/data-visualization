import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(前15).xlsx"
df = pd.read_excel(path, sheet_name='13 对比折线图', header=1)
df = df.iloc[:, 1:4].dropna()
df.columns = ['月份', '2021年', '2022年']

fig, ax = plt.subplots(figsize=(12, 6.8))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

x = np.arange(len(df))
y21 = df['2021年'].values
y22 = df['2022年'].values

ax.plot(x, y21, marker='o', markersize=6, linewidth=2.0,
        color='#FF4A6E', markerfacecolor='#FF4A6E',
        markeredgecolor='#FF4A6E', label='2021年')
ax.plot(x, y22, marker='o', markersize=6, linewidth=2.0,
        color='#2EA9E0', markerfacecolor='#2EA9E0',
        markeredgecolor='#2EA9E0', label='2022年')

# 每个点的标签：统一放在该点的上方；若两点重叠，用偏移避让
offset = 100
for i in range(len(df)):
    v21 = y21[i]
    v22 = y22[i]
    # 2021 标签
    if abs(v21 - v22) < 200 and v21 < v22:
        # 2021 在下，标签也放上方(但会比2022低)
        ax.text(x[i] - 0.10, v21 + offset * 0.6, f"{int(v21)}",
                ha='center', va='bottom', fontsize=10, color='white')
    else:
        ax.text(x[i] - 0.10, v21 + offset, f"{int(v21)}",
                ha='center', va='bottom', fontsize=10, color='white')
    # 2022 标签
    if abs(v21 - v22) < 200 and v22 < v21:
        ax.text(x[i] + 0.10, v22 + offset * 0.6, f"{int(v22)}",
                ha='center', va='bottom', fontsize=10, color='white')
    else:
        ax.text(x[i] + 0.10, v22 + offset, f"{int(v22)}",
                ha='center', va='bottom', fontsize=10, color='white')

# 水平虚线网格
for yv in [0, 500, 1000, 1500, 2000, 2500, 3000]:
    ax.axhline(yv, color='#5A6B8C', linestyle=(0, (4, 4)),
               linewidth=0.7, alpha=0.6)

ax.set_yticks([0, 500, 1000, 1500, 2000, 2500, 3000])
ax.set_yticklabels(['0', '500', '1000', '1500', '2000', '2500', '3000'],
                   fontsize=10, color='white')
ax.tick_params(axis='y', colors='white', length=0)

ax.set_xticks(x)
ax.set_xticklabels(df['月份'], fontsize=11, color='white')
ax.tick_params(axis='x', colors='white', length=0, pad=8)

for s in ax.spines.values():
    s.set_visible(False)

leg = ax.legend(loc='upper right', bbox_to_anchor=(0.98, 1.02),
                frameon=False, fontsize=11, labelcolor='white',
                handlelength=1.8, ncol=2)

ax.text(0.5, 1.18, '2022年上半年各月同比去年销量',
        transform=ax.transAxes, fontsize=20, fontweight='bold',
        color='white', ha='center', va='bottom')
ax.text(0.5, 1.10, '上半年同比去年增长明显，5月份同比增长最多，增长近40%',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='center', va='bottom')

ax.text(0.0, -0.16, '*注：数据来源于公司销售系统，统计日期截至2022.06.30',
        transform=ax.transAxes, fontsize=10, color='#8899AA', va='top')

ax.set_ylim(0, 3200)
ax.set_xlim(-0.4, len(df) - 0.6)

plt.subplots_adjust(top=0.82, bottom=0.14, left=0.06, right=0.94)
plt.show()