import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(后15).xlsx"
df = pd.read_excel(path, sheet_name='19 南丁格尔圆饼图', header=None,
                   skiprows=2, nrows=6, usecols=[1, 2])
df.columns = ['部门', '占比']
df['占比'] = df['占比'].astype(float)
if df['占比'].max() <= 1.5:
    df['占比'] = df['占比'] * 100

fig, ax = plt.subplots(figsize=(12, 6.8))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

cx, cy = 0.62, 0.50
r = 0.30
line_len = 0.09    # 引线长度（统一）

vals = df['占比'].values
colors = ['#F0406E', '#F5B324', '#29B8B0', '#2E7FC4',
          '#4FA8E8', '#7B5BD6']

total = vals.sum()
start_deg = 90.0

for i, (v, c) in enumerate(zip(vals, colors)):
    span = v / total * 360
    theta2 = start_deg
    theta1 = start_deg - span
    ax.add_patch(Wedge((cx, cy), r, theta1, theta2,
                       facecolor=c, edgecolor='#1B2A4A', linewidth=1.2))

    # 引线：从扇形中角位置沿半径方向直出
    mid = np.radians((theta1 + theta2) / 2)
    x1 = cx + r * np.cos(mid)
    y1 = cy + r * np.sin(mid)
    x2 = cx + (r + line_len) * np.cos(mid)
    y2 = cy + (r + line_len) * np.sin(mid)
    ax.plot([x1, x2], [y1, y2], color=c, linewidth=1.2)

    start_deg -= span

# 标题
ax.text(0.02, 0.96, '2021年各部门人数分布',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='left', va='top')
ax.text(0.02, 0.88, '公司总人数1664，销售部人数最多451，占比29.2%',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='left', va='top')

# 底部来源
ax.text(0.02, 0.02,
        '*注：数据来源于公司人力资源系统，统计日期截至2022.01.01',
        transform=ax.transAxes, fontsize=10, color='#8899AA',
        ha='left', va='bottom')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.subplots_adjust(top=0.96, bottom=0.04, left=0.02, right=0.98)
plt.show()