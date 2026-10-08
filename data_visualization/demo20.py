import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(后15).xlsx"
df = pd.read_excel(path, sheet_name='20 南丁格尔圆环图', header=None,
                   skiprows=2, nrows=4, usecols=[1, 2])
df.columns = ['年龄', '占比']
df['占比'] = df['占比'].astype(float)
if df['占比'].max() <= 1.5:
    df['占比'] = df['占比'] * 100

fig, ax = plt.subplots(figsize=(13, 7.0))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

cx, cy = 0.50, 0.50
r_out = 0.30          # 外半径
ring_w = 0.10         # 每段环厚度

vals = df['占比'].values
labels = ['[20,30)', '[30,40)', '[40,50)', '>=50']
colors = ['#5B3BD6', '#F5B324', '#29B8B0', '#4FA8E8']

total = vals.sum()

# 画 4 个环段（统一厚度），从 12 点顺时针
segs = []
start_deg = 90.0
for v, c in zip(vals, colors):
    span = v / total * 360
    mid_deg = start_deg - span / 2
    ax.add_patch(Wedge((cx, cy), r_out, start_deg - span, start_deg,
                       width=ring_w, facecolor=c, edgecolor='none'))
    segs.append({'mid': mid_deg, 'c': c})
    start_deg -= span

# 每段一条引线，末端两行：区间 / 百分比
r_mid = r_out - ring_w / 2
for i, s in enumerate(segs):
    mid = np.radians(s['mid'])
    c = s['c']

    x1 = cx + (r_out + 0.005) * np.cos(mid)
    y1 = cy + (r_out + 0.005) * np.sin(mid)

    if np.cos(mid) >= 0:              # 右半
        x2 = x1 + 0.16
        ha = 'left'
    else:                              # 左半
        x2 = x1 - 0.16
        ha = 'right'

    ax.plot([x1, x2], [y1, y1], color=c, linewidth=1.2)
    ax.scatter([x1], [y1], s=18, color=c, zorder=5)

    # 两行文字紧贴引线末端，上一行区间、下一行百分比
    ax.text(x2, y1 + 0.022, labels[i], fontsize=11, color=c,
            ha=ha, va='bottom')
    ax.text(x2, y1 - 0.022, f"{vals[i]:.1f}%", fontsize=11, color=c,
            ha=ha, va='top')

# 标题
ax.text(0.02, 0.96, '2022年上半年各年龄段人数分布',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='left', va='top')
ax.text(0.02, 0.88, '公司平均年龄32.5，20-30员工比例最高占比37.5%',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='left', va='top')

ax.text(0.02, 0.02,
        '*注：数据来源于公司人力资源系统，统计日期截至2022.06.30',
        transform=ax.transAxes, fontsize=10, color='#8899AA',
        ha='left', va='bottom')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.subplots_adjust(top=0.96, bottom=0.04, left=0.02, right=0.98)
plt.show()