import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(后15).xlsx"
df = pd.read_excel(path, sheet_name='18 跑道图', header=None,
                   skiprows=2, nrows=6, usecols=[1, 2])
df.columns = ['部门', '人数']
df['人数'] = df['人数'].astype(int)

# 确保按人数降序：销售(451) 在最前
df = df.sort_values('人数', ascending=False).reset_index(drop=True)

fig, ax = plt.subplots(figsize=(12, 6.8))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

cx, cy = 0.52, 0.50
r_outer = 0.34
ring_w = 0.036
gap = 0.006

labels = [f"{d} {n}" for d, n in zip(df['部门'], df['人数'])]
vals = df['人数'].values          # 451, 326, 293, 238, 226, 130
colors = ['#F0406E', '#F5B324', '#63B8E8', '#2E7FC4',
          '#29B8B0', '#7B5BD6']

max_val = vals.max()
max_span = 300

radii = []
for i, (v, c) in enumerate(zip(vals, colors)):
    r_out = r_outer - i * (ring_w + gap)     # 外圈 -> 内圈
    radii.append(r_out)
    span = v / max_val * max_span            # 451->300°, 130->86°
    # 起点 12 点(90°)，顺时针 -> 到 90 - span
    ax.add_patch(Wedge((cx, cy), r_out, 90 - span, 90,
                       width=ring_w, facecolor=c, edgecolor='none'))

# 标签贴各环起点左侧
for i, lab in enumerate(labels):
    r_out = radii[i]
    r_in = r_out - ring_w
    r_mid = (r_out + r_in) / 2
    y = cy + r_mid
    x = cx - 0.01
    ax.text(x, y, lab, fontsize=10, color='white',
            ha='right', va='center')

# 标题
ax.text(0.02, 0.96, '2022年上半年各部门人数',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='left', va='top')
ax.text(0.02, 0.88, '公司总人数1664，销售部人数最多451，占比27%',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='left', va='top')

# 底部来源
ax.text(0.02, 0.02,
        '*注：数据来源于公司人力资源系统，统计日期截至2022.06.30',
        transform=ax.transAxes, fontsize=10, color='#8899AA',
        ha='left', va='bottom')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.subplots_adjust(top=0.96, bottom=0.04, left=0.02, right=0.98)
plt.show()