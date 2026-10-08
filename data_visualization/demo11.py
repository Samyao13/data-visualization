import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator
from matplotlib.patches import FancyBboxPatch

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(前15).xlsx"
df = pd.read_excel(path, sheet_name='11 平滑折线图', header=1)
df = df.iloc[:, 1:4].dropna()
df.columns = ['年份', '月份', '销量']

x = np.arange(len(df))
vals = df['销量'].values
labels = df['月份'].tolist()

fig, ax = plt.subplots(figsize=(12, 7.0))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

xs = np.linspace(x.min(), x.max(), 500)
ys = PchipInterpolator(x, vals)(xs)
ax.plot(xs, ys, color='#F26C22', linewidth=2.0)

ax.set_yticks([0, 1000, 2000, 3000, 4000])
ax.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000'],
                   fontsize=10, color='white')
ax.tick_params(axis='y', colors='white', length=0)
ax.spines['left'].set_color('white')
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=10, color='white')
ax.tick_params(axis='x', colors='white', length=0, pad=8)

idx_max = int(np.argmax(vals))
ax.vlines(x[idx_max], 0, vals[idx_max],
          color='#F26C22', linestyle=(0, (4, 4)), linewidth=1.2)
ax.text(x[idx_max], vals[idx_max] + 120, f"{int(vals[idx_max])}",
        ha='center', va='bottom', fontsize=11, color='white')

# ============ 第一行：2021 / 2022 色带 ============
bar_y = -0.20
bar_h = 0.10
x2021_s, x2021_e = x[0] - 0.4, x[8] - 0.4
x2022_s, x2022_e = x[8] - 0.4, x[-1] + 0.4

box1 = FancyBboxPatch((x2021_s, bar_y - bar_h/2),
                      x2021_e - x2021_s, bar_h,
                      boxstyle="round,pad=0,rounding_size=0.01",
                      transform=ax.get_xaxis_transform(),
                      clip_on=False, facecolor='#41B8E8',
                      edgecolor='white', linewidth=1.2)
box2 = FancyBboxPatch((x2022_s, bar_y - bar_h/2),
                      x2022_e - x2022_s, bar_h,
                      boxstyle="round,pad=0,rounding_size=0.01",
                      transform=ax.get_xaxis_transform(),
                      clip_on=False, facecolor='#F0B429',
                      edgecolor='white', linewidth=1.2)
ax.add_patch(box1)
ax.add_patch(box2)

ax.text((x2021_s + x2021_e)/2, bar_y, '2021',
        ha='center', va='center', fontsize=11, color='white',
        transform=ax.get_xaxis_transform())
ax.text((x2022_s + x2022_e)/2, bar_y, '2022',
        ha='center', va='center', fontsize=11, color='white',
        transform=ax.get_xaxis_transform())

# ============ 标题 ============
ax.text(0.0, 1.16, '化妆品品类月度销量走势',
        transform=ax.transAxes, fontsize=20, fontweight='bold',
        color='white', va='bottom')
ax.text(0.0, 1.08, '2022年销量迅速增加，1月最高，销量达到3782',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE', va='bottom')

# ============ 第二行：底部注释（在整张图最底端） ============
fig.text(0.05, 0.03,
         '*注：数据来源于公司销售系统，统计日期截至2022.03.31',
         fontsize=10, color='#8899AA', va='bottom')

ax.set_ylim(0, 4200)
plt.subplots_adjust(top=0.84, bottom=0.22, left=0.08, right=0.97)
plt.show()