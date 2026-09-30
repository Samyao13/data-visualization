import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# ==========================================
# 1. 字体设置
# ==========================================
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ==========================================
# 2. 精准读取数据
# ==========================================
file_path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(前15).xlsx"

try:
    sheet_name = '5 层叠柱形图'
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=1)
    df.columns = df.columns.astype(str).str.strip()
    df = df.dropna(how='all')

    categories = df['季度'].tolist()
    sales = df['销售额'].tolist()
    profit = df['利润额'].tolist()

except Exception as e:
    print(f"读取文件出错: {e}")
    exit()

# ==========================================
# 3. 绘图全局样式
# ==========================================
bg_color = '#1B1D36'  # 背景深蓝色
text_color = '#FFFFFF'  # 文字白色
grid_color = '#3A4060'  # 网格线暗蓝色
sales_color = '#1E88E5'  # 销售额蓝色
profit_color = '#E94B5F'  # 利润额红色

fig, ax = plt.subplots(figsize=(10, 6), facecolor=bg_color)
ax.set_facecolor(bg_color)

# ==========================================
# 4. 绘制重叠柱状图 (关键：左蓝右红，局部重叠)
# ==========================================
x = np.arange(len(categories))  # X轴位置

# 蓝色柱子（销售额）：宽，靠左
width_sales = 0.35
bars1 = ax.bar(x - 0.1, sales, width_sales, label='销售额', color=sales_color, zorder=3)

# 红色柱子（利润额）：窄，向右偏移，插入蓝色柱子内部
width_profit = 0.3
# 关键偏移量：让红色柱子的左侧刚好在蓝色柱子的右半边
# 蓝色柱子在 x-0.1 位置，宽度0.35，右边缘是 x-0.1+0.35 = x+0.25
# 红色柱子放在 x+0.05 位置，宽度0.2，左边缘是 x+0.05，正好与蓝色柱子重叠
bars2 = ax.bar(x + 0.05, profit, width_profit, label='利润额', color=profit_color, zorder=4)

# ==========================================
# 5. 添加数据标签 (纯文本，无背景框)
# ==========================================
# 蓝色柱子的数字标签（居中于蓝色柱子）
for bar in bars1:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 50, str(int(height)),
            color=text_color, ha='center', va='bottom', fontsize=10, zorder=7)

# 红色柱子的数字标签（居中于红色柱子）
for bar in bars2:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 50, str(int(height)),
            color=text_color, ha='center', va='bottom', fontsize=10, zorder=7)

# ==========================================
# 6. 坐标轴和网格线
# ==========================================
ax.set_ylim(0, 6000)
ax.set_yticks(np.arange(0, 6001, 1000))
ax.set_yticklabels([])  # 隐藏Y轴刻度数字

ax.yaxis.grid(True, color=grid_color, linestyle='--', linewidth=1, zorder=0)

for spine in ax.spines.values():
    spine.set_visible(False)

# X轴刻度位置需要稍微调整，因为柱子整体向右偏移了
ax.set_xticks(x)
ax.set_xticklabels(categories, color=text_color, fontsize=11)

ax.tick_params(axis='x', length=0, pad=12)
ax.tick_params(axis='y', length=0)

# ==========================================
# 7. 添加图例 (右侧，带彩色边框)
# ==========================================
legend_elements = [
    Patch(facecolor='none', edgecolor=sales_color, label='销售额', linewidth=1.5),
    Patch(facecolor='none', edgecolor=profit_color, label='利润额', linewidth=1.5)
]

ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(0.98, 0.4),
          frameon=False, labelcolor=text_color, fontsize=10, handlelength=2)

# ==========================================
# 8. 添加标题、副标题和脚注
# ==========================================
fig.text(0.08, 0.92, '2021年至今季度销售额(万)和利润额(万)', color=text_color,
         fontsize=22, fontweight='bold', ha='left')
fig.text(0.08, 0.86, '2022年第二季度销售额首次出现下降，降幅达到15%', color=text_color,
         fontsize=13, ha='left')
fig.text(0.08, 0.02, '*注：数据来源于公司销售系统，统计日期截至2022.06.30',
         color='#A0B0D0', fontsize=9, ha='left')

plt.subplots_adjust(left=0.08, right=0.88, top=0.80, bottom=0.15)

# ==========================================
# 9. 显示图表
# ==========================================
plt.show()