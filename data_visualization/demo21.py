import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(后15).xlsx"
df = pd.read_excel(path, sheet_name='20 南丁格尔（PPT）', header=None,
                   skiprows=2, nrows=6, usecols=[1, 2])
df.columns = ['部门', '占比']
df['占比'] = df['占比'].astype(float)
if df['占比'].max() <= 1.5:
    df['占比'] = df['占比'] * 100

fig, ax = plt.subplots(figsize=(13, 7.0))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

cx, cy = 0.60, 0.50
r_min = 0.10              # 最小半径
r_max = 0.34              # 最大半径

vals = df['占比'].values
colors = ['#F0406E', '#F5B324', '#29B8B0', '#4FA8E8',
          '#2E7FC4', '#7B5BD6']

max_val = vals.max()
total = vals.sum()

# 6 个扇形，从 12 点顺时针
start_deg = 90.0
mid_angles = []
for v, c in zip(vals, colors):
    span = v / total * 360
    r_this = r_min + (r_max - r_min) * (v / max_val)
    theta2 = start_deg
    theta1 = start_deg - span
    ax.add_patch(Wedge((cx, cy), r_this, theta1, theta2,
                       facecolor=c, edgecolor='#1B2A4A', linewidth=1.2))
    mid_angles.append((theta1 + theta2) / 2)
    start_deg -= span

# 每个扇形一条折线引线 + 末端小圆点
for i, (mid_deg, c) in enumerate(zip(mid_angles, colors)):
    mid = np.radians(mid_deg)
    r_this = r_min + (r_max - r_min) * (vals[i] / max_val)

    x1 = cx + (r_this + 0.005) * np.cos(mid)
    y1 = cy + (r_this + 0.005) * np.sin(mid)
    # 折点（沿半径方向再往一点）
    x2 = cx + (r_this + 0.07) * np.cos(mid)
    y2 = cy + (r_this + 0.07) * np.sin(mid)

    # 水平方向：朝远离圆心方向
    if np.cos(mid) >= 0:
        x3 = x2 + 0.13
        ha = 'left'
    else:
        x3 = x2 - 0.13
        ha = 'right'

    ax.plot([x1, x2, x3], [y1, y2, y2], color=c, linewidth=1.2)
    ax.scatter([x2], [y2], s=30, color=c, zorder=5)

# 标题
ax.text(0.02, 0.96, '2021年各部门人数分布',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='left', va='top')
ax.text(0.02, 0.88, '公司总人数1664，销售部人数最多451，占比29.2%',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='left', va='top')

ax.text(0.02, 0.02,
        '*注：数据来源于公司人力资源系统，统计日期截至2022.01.01',
        transform=ax.transAxes, fontsize=10, color='#8899AA',
        ha='left', va='bottom')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.subplots_adjust(top=0.96, bottom=0.04, left=0.02, right=0.98)
plt.show()