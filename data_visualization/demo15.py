import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(前15).xlsx"
df = pd.read_excel(path, sheet_name='15 水球图', header=1)
df = df.iloc[:, 1:3].dropna()
df.columns = ['完成率', '辅助']
val = float(df['完成率'].iloc[0])

fig, ax = plt.subplots(figsize=(12, 6.8))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

cx, cy = 0.5, 0.45

# ---- 外层圆环 ----
r1 = 0.28
r2 = 0.268
ax.add_patch(Circle((cx, cy), r1, facecolor='none',
                    edgecolor='#2E8FD0', linewidth=1.3))
ax.add_patch(Circle((cx, cy), r2, facecolor='none',
                    edgecolor='#2E8FD0', linewidth=1.3))

# ---- 内层水球：直接贴到内圈 ----
r_inner = r2   # 与内圈半径一致，无缝隙
clip_circle = Circle((cx, cy), r_inner, transform=ax.transData)

# 内圆底色
ax.add_patch(Circle((cx, cy), r_inner, facecolor='#1B2A4A',
                    edgecolor='none'))

# 水位以下蓝色（矩形被圆裁切）
water_top = cy - r_inner + 2 * r_inner * val
rect = Rectangle((cx - r_inner, cy - r_inner), 2 * r_inner,
                 water_top - (cy - r_inner),
                 facecolor='#1F8FE0', edgecolor='none')
rect.set_clip_path(clip_circle)
ax.add_patch(rect)

# 中央文字
ax.text(cx, cy, f"{val:.0%}", ha='center', va='center',
        fontsize=44, color='white', fontweight='bold')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

ax.text(0.02, 0.96, '2022年上半年目标完成率',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='left', va='top')
ax.text(0.02, 0.88, '截至6月30日销售目标总体完成率达到65%',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='left', va='top')

ax.text(0.02, 0.02, '*注：数据来源于公司销售系统',
        transform=ax.transAxes, fontsize=10, color='#8899AA',
        ha='left', va='bottom')

plt.subplots_adjust(top=0.96, bottom=0.04, left=0.02, right=0.98)
plt.show()