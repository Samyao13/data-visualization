import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Wedge

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(前15).xlsx"
df = pd.read_excel(path, sheet_name='14 单值圆环图', header=1)
df = df.iloc[:, 1:3].dropna()
df.columns = ['完成率', '占位']
val = float(df['完成率'].iloc[0])

fig, ax = plt.subplots(figsize=(12, 6.8))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

cx, cy = 0.5, 0.5
r = 0.28
width = 0.075

# 圆环起点在 12 点钟方向，顺时针
# 已完成段：从 90° 顺时针 val*360°，即从 90° 到 90 - 360*val
# 剩余段：从 90 - 360*val 到 -270

# 紫 -> 粉 渐变
cmap = mcolors.LinearSegmentedColormap.from_list(
    'purple_pink', ['#8E44D0', '#E8447E'])

# 剩余段（深灰蓝）
theta_remain_start = 90 - 360 * val
ax.add_patch(Wedge((cx, cy), r, 90 - 360, theta_remain_start,
                   width=width, facecolor='#2E3B56', edgecolor='none'))

# 已完成段：拆成很多小块做渐变
n_seg = 240
for k in range(n_seg):
    a0 = 90 - 360 * val * (k / n_seg)
    a1 = 90 - 360 * val * ((k + 1) / n_seg)
    color = cmap(k / (n_seg - 1))
    ax.add_patch(Wedge((cx, cy), r, a1, a0, width=width,
                       facecolor=color, edgecolor='none'))

# 中间文字
ax.text(cx, cy + 0.02, f"{val:.0%}", ha='center', va='center',
        fontsize=44, color='white', fontweight='bold')
ax.text(cx, cy - 0.09, '目标完成率', ha='center', va='center',
        fontsize=14, color='#B0C4DE')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# 标题（左上）
ax.text(0.02, 0.96, '2022年上半年目标完成率',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='left', va='top')
ax.text(0.02, 0.88, '截至6月30日销售目标总体完成率达到85%',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='left', va='top')

# 底部数据来源
ax.text(0.02, 0.02, '*注：数据来源于公司销售系统',
        transform=ax.transAxes, fontsize=10, color='#8899AA',
        ha='left', va='bottom')

plt.subplots_adjust(top=0.96, bottom=0.04, left=0.02, right=0.98)
plt.show()