import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(后15).xlsx"
df = pd.read_excel(path, sheet_name='28 复合柱形图', header=None,
                   skiprows=2, usecols=[1, 2, 3])
df.columns = ['月份', '月度销量', '季度销量']
df = df.dropna().reset_index(drop=True)
df['月度销量'] = df['月度销量'].astype(float)
df['季度销量'] = df['季度销量'].astype(float)

fig, ax = plt.subplots(figsize=(12, 7.0))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

x = np.arange(len(df))
vals = df['月度销量'].values
quarters = df['季度销量'].values

q_colors = ['#2E5FBF', '#E06A0F', '#D89A0F', '#A0407A']
bar_colors = []
for i in range(len(df)):
    bar_colors.append(q_colors[i // 3])

for q in range(4):
    ax.add_patch(Rectangle((q*3 - 0.45, 0), 2.9, quarters[q*3],
                           facecolor=q_colors[q], alpha=0.35,
                           edgecolor='none', zorder=1))

bars = ax.bar(x, vals, width=0.35, color=bar_colors,
              edgecolor='none', zorder=3)
for xi, v in zip(x, vals):
    ax.text(xi, v + 60, str(int(v)), ha='center', va='bottom',
            fontsize=10, color='white', zorder=4)

for q in range(4):
    x_center = q*3 + 1
    ax.text(x_center, quarters[q*3] + 60, str(int(quarters[q*3])),
            ha='center', va='bottom', fontsize=11, color='white', zorder=4)

ax.set_xticks(x)
ax.set_xticklabels(df['月份'], fontsize=10, color='white')
ax.tick_params(axis='x', colors='white', length=0, pad=8)
ax.set_yticks([])

for s in ax.spines.values():
    s.set_visible(False)

ax.axhline(0, color='#5A6B8C', linewidth=0.8, alpha=0.6)

# 标题/副标题抬到图外，彼此间距拉开
ax.text(0.5, 1.18, '2021年各月化妆品销量走势',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='center', va='bottom')
ax.text(0.5, 1.08, '2021年第三季度销量最多9673，9月单月销量最大3621',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='center', va='bottom')

# 注释放画布最底端
fig.text(0.04, 0.03,
         '*注：数据来源于公司销售系统，统计日期截至2021.12.31',
         fontsize=10, color='#8899AA', va='bottom')

ax.set_ylim(0, max(quarters) * 1.2)

plt.subplots_adjust(top=0.78, bottom=0.14, left=0.04, right=0.96)
plt.show()