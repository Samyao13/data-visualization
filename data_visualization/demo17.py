import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(后15).xlsx"
df = pd.read_excel(path, sheet_name='17 玉玦图', header=None,
                   skiprows=2, nrows=4, usecols=[1, 2, 3])
df.columns = ['年龄', '占比', '占位']
df['占位'] = df['占位'].astype(float)
if df['占位'].max() <= 1.5:
    df['占位'] = df['占位'] * 100

fig, ax = plt.subplots(figsize=(12, 6.8))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

cx, cy = 0.52, 0.50
r_outer = 0.34
ring_w = 0.075
gap = 0.008

df = df.sort_values('占位', ascending=False).reset_index(drop=True)
vals = df['占位'].values          # 37.5, 29.2, 20.8, 12.5
labels = ['[20,30)', '[30,40)', '[40,50)', '>=50']
colors = ['#F0406E', '#F5B324', '#29B8B0', '#2E9BD6']

max_val = vals.max()
max_span = 250

radii = []
for i, (v, c) in enumerate(zip(vals, colors)):
    r_out = r_outer - i * (ring_w + gap)
    radii.append(r_out)
    span = v / max_val * max_span
    ax.add_patch(Wedge((cx, cy), r_out, 90 - span, 90,
                       width=ring_w, facecolor=c, edgecolor='none'))

# 年龄标签：贴各环起点(12点)左侧
for i, lab in enumerate(labels):
    r_out = radii[i]
    r_in = r_out - ring_w
    r_mid = (r_out + r_in) / 2
    ax.text(cx - 0.01, cy + r_mid, lab, fontsize=11, color='white',
            ha='right', va='center')

# 百分比标签：贴"该环自己的"缺口末端，半径用该环中线
for i, v in enumerate(vals):
    r_out = radii[i]
    r_in = r_out - ring_w
    r_mid = (r_out + r_in) / 2
    span = v / max_val * max_span
    end_ang = np.radians(90 - span)      # 该环缺口末端角度

    # 沿该环中线，稍微向圆心方向偏一点点，让标签落在环上
    x = cx + r_mid * np.cos(end_ang)
    y = cy + r_mid * np.sin(end_ang)

    # 根据象限选对齐
    if end_ang > np.pi / 2:
        ha, va = 'right', 'bottom'
    elif end_ang > 0:
        ha, va = 'left', 'bottom'
    elif end_ang > -np.pi / 2:
        ha, va = 'left', 'top'
    else:
        ha, va = 'right', 'top'

    ax.text(x, y, f"{v:.1f}%", fontsize=11, color='white',
            ha=ha, va=va)

ax.text(0.02, 0.96, '2022年上半年年龄分布',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='left', va='top')
ax.text(0.02, 0.88, '公司平均年龄32.5，23-30员工比例最高',
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