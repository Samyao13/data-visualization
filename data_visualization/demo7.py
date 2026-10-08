import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(前15).xlsx"
df = pd.read_excel(path, sheet_name='7 蝴蝶图', header=1)
df = df.iloc[:, 1:4].dropna(subset=['区域'])
df.columns = ['区域', '2022年', '2021年']

fig, ax = plt.subplots(figsize=(12, 6.8))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

n = len(df)
y = np.arange(n)[::-1]

bar_left_end    = 0.42
bar_left_max    = 0.30      # 最长蓝条长度

name_x          = 0.50

bar_right_start = 0.58
bar_right_max   = 0.30      # 最长红条长度

seg_scale = 0.45            # 参照值 45%
SEG_W  = 0.012              # 单根条纹宽度（固定）
SEG_GAP = 0.004             # 条纹间隙（固定）
HEIGHT = 0.30

def draw_striped_barh(ax, ypos, value, x_start, length, color):
    """固定条纹宽度，条纹数量随长度自适应"""
    seg_w = SEG_W + SEG_GAP
    n_seg = max(1, int(length // seg_w))
    for k in range(n_seg):
        rect = plt.Rectangle((x_start + k * seg_w, ypos - HEIGHT/2),
                             SEG_W, HEIGHT,
                             facecolor=color, edgecolor='none')
        ax.add_patch(rect)

for i, (_, row) in enumerate(df.iterrows()):
    ypos = y[i]
    v22 = row['2022年']
    v21 = row['2021年']

    len22 = bar_left_max * (v22 / seg_scale)
    len21 = bar_right_max * (v21 / seg_scale)

    ax.text(bar_left_end - len22 - 0.012, ypos, f"{v22:.0%}",
            ha='right', va='center', fontsize=12, color='white')
    draw_striped_barh(ax, ypos, v22, bar_left_end - len22, len22, '#2E75B6')

    draw_striped_barh(ax, ypos, v21, bar_right_start, len21, '#C00000')
    ax.text(bar_right_start + len21 + 0.012, ypos, f"{v21:.0%}",
            ha='left', va='center', fontsize=12, color='white')

    ax.text(name_x, ypos, row['区域'], ha='center', va='center',
            fontsize=12, color='white')

ax.text(0.02, 1.06, '2022年第一季度销售目标完成情况',
        transform=ax.transAxes, fontsize=20, fontweight='bold',
        color='white', va='bottom')
ax.text(0.02, 1.00, '华东区域完成率最高达到36%，但是相比去年的42%有所下降',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE', va='bottom')

ax.text(0.02, -0.14, '*注：数据来源于公司销售系统，统计日期截至2022.03.31',
        transform=ax.transAxes, fontsize=9, color='#8899AA', va='top')

ax.set_xlim(0, 1)
ax.set_ylim(-0.5, n - 0.5)
ax.set_yticks([])
ax.set_xticks([])
for s in ax.spines.values():
    s.set_visible(False)
plt.subplots_adjust(top=0.86, bottom=0.14, left=0.02, right=0.98)
plt.show()