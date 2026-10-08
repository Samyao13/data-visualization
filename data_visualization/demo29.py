import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(后15).xlsx"
df = pd.read_excel(path, sheet_name='29 滑珠图', header=None,
                   skiprows=2, nrows=5, usecols=[1, 2])
df.columns = ['区域', '完成率']
df['完成率'] = df['完成率'].astype(float)
if df['完成率'].max() <= 1.5:
    df['完成率'] = df['完成率'] * 100

fig, ax = plt.subplots(figsize=(12, 7.0))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

n = len(df)
y = np.arange(n)[::-1]

x0 = 0.20
x_end = x0 + 0.68

# 用 linewidth 来当胶囊高度，单位是 pt
line_w_pt = 26           # 条高（pt），可调

for i, (_, row) in enumerate(df.iterrows()):
    ypos = y[i]
    v = row['完成率']
    cx_dot = x0 + (x_end - x0) * (v / 100)

    # 灰底胶囊
    ax.plot([x0, x_end], [ypos, ypos],
            color='#8A9BB2', linewidth=line_w_pt,
            solid_capstyle='round', zorder=2)

    # 蓝条胶囊
    ax.plot([x0, cx_dot], [ypos, ypos],
            color='#1F8FE0', linewidth=line_w_pt,
            solid_capstyle='round', zorder=3)

    # 滑珠（圆球）：大小与条高一致
    # linewidth(pt) 转成 scatter 的 s
    s_dot = (line_w_pt * 1.05) ** 2
    ax.scatter(cx_dot, ypos, s=s_dot,
               facecolor='#1F8FE0', edgecolor='white',
               linewidth=1.6, zorder=5)

    # 百分比
    ax.text(cx_dot - 0.04, ypos, f"{int(v)}%",
            ha='right', va='center', fontsize=11, color='white',
            zorder=6)

    # 区域名
    ax.text(x0 - 0.02, ypos, row['区域'],
            ha='right', va='center', fontsize=11, color='white')

ax.set_xlim(0, 1)
ax.set_ylim(-0.6, n - 0.4)
ax.axis('off')

ax.text(0.02, 1.14, '2022年上半年产品销量目标达成率情况',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='left', va='bottom')
ax.text(0.02, 1.05, '华南完成率最高达到86%，华东最低35%',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='left', va='bottom')

ax.text(0.02, 0.02,
        '*注：数据来源于公司销售系统，统计日期截至2022.06.30',
        transform=ax.transAxes, fontsize=10, color='#8899AA',
        ha='left', va='bottom')

plt.subplots_adjust(top=0.78, bottom=0.08, left=0.02, right=0.98)
plt.show()