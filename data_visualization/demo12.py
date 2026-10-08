import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(前15).xlsx"
df = pd.read_excel(path, sheet_name='12 菱形走势图', header=1)
df = df.iloc[:, 1:3].dropna()
df.columns = ['月份', '完成率']

fig, ax = plt.subplots(figsize=(12, 6.8))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

x = np.arange(len(df))
vals = df['完成率'].values * 100

# 细红竖线 + 顶部菱形
for i, v in enumerate(vals):
    ax.vlines(x[i], 0, v, color='#E03030', linewidth=1.0)
    ax.plot(x[i], v, marker='D', markersize=8,
            markerfacecolor='#1B2A4A', markeredgecolor='#E03030',
            markeredgewidth=1.6)
    ax.text(x[i], v + 1.6, f"{v:.2f}%",
            ha='center', va='bottom', fontsize=11, color='white')

# 底部横线（x 轴基线）
ax.axhline(0, color='white', linewidth=0.8, alpha=0.8)

# x 轴月份
ax.set_xticks(x)
ax.set_xticklabels(df['月份'], fontsize=11, color='white')
ax.tick_params(axis='x', colors='white', length=0, pad=8)

# 去掉 y 轴刻度
ax.set_yticks([])
for s in ax.spines.values():
    s.set_visible(False)

# y 轴范围
ax.set_ylim(0, 90)
ax.set_xlim(-0.6, len(df) - 0.4)

# 标题（居中）
ax.text(0.5, 1.18, '2022年1-8月公司计划完成率',
        transform=ax.transAxes, fontsize=20, fontweight='bold',
        color='white', ha='center', va='bottom')
ax.text(0.5, 1.10, '公司整体完成率55%，4月和8月超过70%，2月和6月较低未过半',
        transform=ax.transAxes, fontsize=12, color='#B0C4DE',
        ha='center', va='bottom')

# 底部数据来源
ax.text(0.0, -0.16, '*注：数据来源于公司销售系统，统计日期截至2022.08.31',
        transform=ax.transAxes, fontsize=10, color='#8899AA', va='top')

plt.subplots_adjust(top=0.82, bottom=0.14, left=0.06, right=0.94)
plt.show()