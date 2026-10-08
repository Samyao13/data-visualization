import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, PathPatch
from matplotlib.path import Path

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(后15).xlsx"
df = pd.read_excel(path, sheet_name='16 波浪水球图 ', header=2)
df = df.iloc[:, 1:3].dropna()
df.columns = ['完成率', '占位']
val = float(df['完成率'].iloc[0])

fig, ax = plt.subplots(figsize=(12, 6.8))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

cx, cy = 0.5, 0.45

# 外圈蓝环
r_outer = 0.28
ax.add_patch(Circle((cx, cy), r_outer, facecolor='none',
                    edgecolor='#2E8FD0', linewidth=1.5))

# 内层波浪水球（与外圈留空隙）
r_inner = 0.24
water_level = cy - r_inner + 2 * r_inner * val

xs = np.linspace(cx - r_inner, cx + r_inner, 400)
wave_amp = 0.012
wave_period = 0.14
wave = water_level + wave_amp * np.sin((xs - cx) / wave_period * np.pi * 2)

# 波浪上沿 + 圆下半弧
verts = list(zip(xs, wave))
theta = np.linspace(0, -np.pi, 200)
arc_x = cx + r_inner * np.cos(theta)
arc_y = cy + r_inner * np.sin(theta)
verts += list(zip(arc_x, arc_y))
verts.append((xs[0], wave[0]))
codes = [Path.MOVETO] + [Path.LINETO] * (len(verts) - 1)
p = PathPatch(Path(verts, codes), facecolor='#1F8FE0', edgecolor='none')
clip_circle = Circle((cx, cy), r_inner, transform=ax.transData)
p.set_clip_path(clip_circle)
ax.add_patch(p)

# 中央文字
ax.text(cx, cy + 0.02, f"{val:.0%}", ha='center', va='center',
        fontsize=44, color='white', fontweight='bold')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

ax.text(0.02, 0.96, '本科及以上学历员占比',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='left', va='top')
ax.text(0.02, 0.88, '6月30日最新统计数据本科及以上员工占比65%',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='left', va='top')
ax.text(0.02, 0.02, '*注：数据来源于公司人力资源系统',
        transform=ax.transAxes, fontsize=10, color='#8899AA',
        ha='left', va='bottom')

plt.subplots_adjust(top=0.96, bottom=0.04, left=0.02, right=0.98)
plt.show()