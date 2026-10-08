import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(后15).xlsx"
df = pd.read_excel(path, sheet_name='24 目标柱形图', header=None,
                   skiprows=2, nrows=6, usecols=[1, 2, 3])
df.columns = ['商品', '实际销量', '目标销量']
df['实际销量'] = df['实际销量'].astype(float)
df['目标销量'] = df['目标销量'].astype(float)

fig, ax = plt.subplots(figsize=(12, 7.0))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

x = np.arange(len(df))
w_bg = 0.36
w_fg = 0.20

# 目标柱：空心白框（无填充）
ax.bar(x, df['目标销量'], width=w_bg,
       facecolor='none', edgecolor='white', linewidth=1.0, zorder=2)

# 实际柱：深蓝
ax.bar(x, df['实际销量'], width=w_fg,
       color='#1F6FBF', edgecolor='none', zorder=3)

# 实际柱顶白色数值
for xi, v in zip(x, df['实际销量']):
    ax.text(xi, v + 15, str(int(v)), ha='center', va='bottom',
            fontsize=11, color='white', zorder=4)

# x 轴
ax.set_xticks(x)
ax.set_xticklabels(df['商品'], fontsize=11, color='white')
ax.tick_params(axis='x', colors='white', length=0, pad=8)
ax.set_yticks([])

ax.axhline(0, color='#5A6B8C', linewidth=0.8, alpha=0.6)

for s in ax.spines.values():
    s.set_visible(False)

# 图例（小方块 + 文字）
ax.add_patch(Rectangle((0.34, 0.80), 0.012, 0.022,
                       transform=ax.transAxes,
                       facecolor='none', edgecolor='white'))
ax.text(0.36, 0.81, '目标销量', transform=ax.transAxes,
        fontsize=10, color='white', va='center')
ax.add_patch(Rectangle((0.46, 0.80), 0.012, 0.022,
                       transform=ax.transAxes,
                       facecolor='#1F6FBF', edgecolor='none'))
ax.text(0.48, 0.81, '实际销量', transform=ax.transAxes,
        fontsize=10, color='white', va='center')

# 标题
ax.text(0.5, 0.96, '2022年上半年各商品销量完成情况',
        transform=ax.transAxes, fontsize=22, fontweight='bold',
        color='white', ha='center', va='top')
ax.text(0.5, 0.88, '防晒整体销量最好，达到856，面霜远超目标，超额完成30%',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='center', va='top')

# 底部注释：放到整张画布最底端，避免和柱子重叠
fig.text(0.04, 0.03,
         '*注：数据来源于公司销售系统，统计日期截至2022.06.30',
         fontsize=10, color='#8899AA', va='bottom')

ax.set_ylim(0, df['目标销量'].max() * 1.25)

plt.subplots_adjust(top=0.84, bottom=0.14, left=0.04, right=0.96)
plt.show()