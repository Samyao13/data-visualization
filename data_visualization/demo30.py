import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(后15).xlsx"
df = pd.read_excel(path, sheet_name='30 对比滑珠图', header=None,
                   skiprows=3, nrows=5, usecols=[1, 2, 3])
df.columns = ['区域', '2022完成率', '2021完成率']
df['2022完成率'] = df['2022完成率'].astype(float)
df['2021完成率'] = df['2021完成率'].astype(float)
if df['2022完成率'].max() <= 1.5:
    df['2022完成率'] = df['2022完成率'] * 100
if df['2021完成率'].max() <= 1.5:
    df['2021完成率'] = df['2021完成率'] * 100

fig, ax = plt.subplots(figsize=(12, 7.0))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

n = len(df)
y = np.arange(n)[::-1]

x0 = 0.22
bar_max = 0.68
bar_h = 0.16

# 圆球尺寸（数据坐标 -> pt^2）
fig_w, fig_h = fig.get_size_inches()
ax_pos = ax.get_position()
ax_h_in = fig_h * (ax_pos.y1 - ax_pos.y0)
ylim = (-0.6, n - 0.4)
units_per_inch_y = (ylim[1] - ylim[0]) / ax_h_in
r_y = bar_h / 2
d_in = 2 * r_y / units_per_inch_y
s = (d_in * 72) ** 2

for i, (_, row) in enumerate(df.iterrows()):
    ypos = y[i]
    v22 = row['2022完成率']
    v21 = row['2021完成率']

    # 灰底：长方形，两端微圆（圆角很小）
    ax.add_patch(FancyBboxPatch((x0, ypos - bar_h/2),
                                bar_max, bar_h,
                                boxstyle="round,pad=0,rounding_size=0.02",
                                facecolor='#8A9BB2', edgecolor='none'))

    # 蓝条：右端到 2022 蓝点圆心
    w22 = bar_max * (v22 / 100)
    ax.add_patch(FancyBboxPatch((x0, ypos - bar_h/2),
                                w22, bar_h,
                                boxstyle="round,pad=0,rounding_size=0.02",
                                facecolor='#1F8FE0', edgecolor='none'))

    # 2021 灰点（白边）
    cx21 = x0 + bar_max * (v21 / 100)
    ax.scatter(cx21, ypos, s=s,
               facecolor='#8A9BB2', edgecolor='white',
               linewidth=1.5, zorder=5)

    # 2022 蓝点（白边，放在灰点之上）
    cx22 = x0 + w22
    ax.scatter(cx22, ypos, s=s,
               facecolor='#1F8FE0', edgecolor='white',
               linewidth=1.5, zorder=6)

    # 百分比：行上方居中
    ax.text(cx22, ypos + bar_h/2 + 0.10, f"{int(v22)}%",
            ha='center', va='bottom', fontsize=11, color='white')

    # 区域名
    ax.text(x0 - 0.02, ypos, row['区域'],
            ha='right', va='center', fontsize=11, color='white')

ax.set_xlim(0, 1)
ax.set_ylim(*ylim)
ax.axis('off')

# 图例：横排在上方
ax.scatter(0.06, n - 0.55, s=s*1.3,
           facecolor='#1F8FE0', edgecolor='white', linewidth=1.5)
ax.text(0.075, n - 0.55, '2022完成率', fontsize=11, color='white',
        va='center')
ax.scatter(0.20, n - 0.55, s=s*1.3,
           facecolor='#8A9BB2', edgecolor='white', linewidth=1.5)
ax.text(0.215, n - 0.55, '2021完成率', fontsize=11, color='white',
        va='center')

# 标题/副标题：拉开间距
ax.text(0.02, 1.22, '2022年上半年销量目标达成率同比去年情况',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='left', va='bottom')
ax.text(0.02, 1.12, '华南完成率最高达到86%，华东最低35%，其中华南和华东不及2021年',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='left', va='bottom')

# 底部来源
ax.text(0.02, 0.02,
        '*注：数据来源于公司销售系统，统计日期截至2022.06.30',
        transform=ax.transAxes, fontsize=10, color='#8899AA',
        ha='left', va='bottom')

plt.subplots_adjust(top=0.72, bottom=0.08, left=0.02, right=0.98)
plt.show()