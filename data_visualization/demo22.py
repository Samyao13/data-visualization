import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle, Rectangle

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(后15).xlsx"
raw = pd.read_excel(path, sheet_name='22 仪表盘图', header=None, skiprows=2)
value = None
for i in range(raw.shape[1]):
    if str(raw.iloc[0, i]).strip() == '指针数值':
        value = float(raw.iloc[1, i])
        break
if value is None:
    value = 76.0

fig, ax = plt.subplots(figsize=(12, 7.0))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

# 白色底板
ax.add_patch(Rectangle((0.22, 0.06), 0.56, 0.72,
                       facecolor='white', edgecolor='none'))

cx, cy = 0.50, 0.42

r_center   = 0.145   # 白心半径
r_disk     = 0.185   # 深蓝圆盘半径
r_color_in = r_disk
r_color_out= 0.235
r_light_in = r_color_out
r_light_out= 0.265

# ---- 最外层浅蓝完整圆环 ----
ax.add_patch(Wedge((cx, cy), r_light_out, 0, 360,
                   width=r_light_out - r_light_in,
                   facecolor='#1F6FBF', edgecolor='none'))

# ---- 第 3 层：彩色刻度环 + 缺口为深蓝 ----
start_deg = 200     # 50 位置（左下）
span_deg  = 220     # 顺时针跨度（彩色部分）
ticks = list(range(50, 151, 10))
n = len(ticks) - 1

def seg_color(v):
    if v < 80:
        return '#1F6FBF'   # 蓝
    elif v < 110:
        return '#29B8B0'   # 青绿
    elif v < 130:
        return '#F5B324'   # 黄
    else:
        return '#F0406E'   # 红

# 先画整个深蓝环（缺口处及底色）
ax.add_patch(Wedge((cx, cy), r_color_out, 0, 360,
                   width=r_color_out - r_color_in,
                   facecolor='#1B2A4A', edgecolor='none'))

# 再画彩色段（覆盖刻度范围）
for i in range(n):
    a0 = start_deg - span_deg * (i / n)
    a1 = start_deg - span_deg * ((i + 1) / n)
    c = seg_color(ticks[i])
    ax.add_patch(Wedge((cx, cy), r_color_out, a1, a0,
                       width=r_color_out - r_color_in,
                       facecolor=c, edgecolor='#1B2A4A', linewidth=1.0))

# ---- 第 2 层：深蓝圆盘 ----
ax.add_patch(Circle((cx, cy), r_disk, facecolor='#1B2A4A', edgecolor='none'))

# ---- 第 1 层：中心白圆 ----
ax.add_patch(Circle((cx, cy), r_center, facecolor='white', edgecolor='none'))

# ---- 刻度数字 ----
for i, t in enumerate(ticks):
    a = np.radians(start_deg - span_deg * (i / n))
    r_t = r_color_in + 0.012
    x = cx + r_t * np.cos(a)
    y = cy + r_t * np.sin(a)
    ax.text(x, y, str(t), fontsize=8, color='white',
            ha='center', va='center')

# ---- 指针 ----
needle_deg = start_deg - span_deg * ((value - 50) / 100)
na = np.radians(needle_deg)
nx = cx + (r_center - 0.02) * np.cos(na)
ny = cy + (r_center - 0.02) * np.sin(na)
ax.plot([cx, nx], [cy, ny], color='#B0C4DE', linewidth=1.8)
ax.add_patch(Circle((cx, cy), 0.008, facecolor='#B0C4DE', edgecolor='none'))

# 标题
ax.text(0.5, 0.92, '2022年6月29公司整体运营指数良好',
        transform=ax.transAxes, fontsize=20, fontweight='bold',
        color='white', ha='center', va='top')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.subplots_adjust(top=0.96, bottom=0.04, left=0.02, right=0.98)
plt.show()