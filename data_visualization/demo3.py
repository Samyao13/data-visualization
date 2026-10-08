import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

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
    sheet_name = '3 渐变圆角柱形图'
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=1)
    df.columns = df.columns.astype(str).str.strip()
    df = df.dropna(how='all')

    categories = df['商品'].tolist()[:6]
    values = df['销量'].tolist()[:6]

    print(f"✅ 成功提取数据: {list(zip(categories, values))}")

except Exception as e:
    print(f"读取文件出错: {e}")
    exit()

# ==========================================
# 3. 绘图全局样式 (精确匹配原图)
# ==========================================
bg_color = '#1B1D36'  # 背景深蓝色
text_color = '#FFFFFF'  # 文字白色
grid_color = '#3A4060'  # 网格线暗蓝色
line_color = '#00B0F0'  # 圆点亮蓝色
bar_bottom_color = '#0066CC'  # 柱子底部亮蓝色
bar_top_color = '#00FFFF'  # 柱子顶部青色
label_bg_color = '#2B5C9B'  # 数据标签背景框颜色

fig, ax = plt.subplots(figsize=(10, 6), facecolor=bg_color)
ax.set_facecolor(bg_color)

# ==========================================
# 4. 绘制渐变柱状图 (关键：柱子变细！)
# ==========================================
cmap = mcolors.LinearSegmentedColormap.from_list("custom_gradient", [bar_bottom_color, bar_top_color])

# 【核心修改】宽度从 0.35 改为 0.15，让柱子变细长
bars = ax.bar(categories, values, width=0.15, zorder=3)

# 为每个柱子内部填充渐变色
for bar in bars:
    height = bar.get_height()
    bottom = bar.get_y()
    grad = np.linspace(0, 1, 100).reshape(-1, 1)
    ax.imshow(grad, extent=[bar.get_x(), bar.get_x() + bar.get_width(), bottom, height],
              aspect='auto', cmap=cmap, zorder=4)

# ==========================================
# 5. 绘制顶点小圆点和数据标签 (无折线！)
# ==========================================
# 只绘制柱顶的小圆点 (s=40 稍微调小)
ax.scatter(categories, values, color=line_color, s=40, zorder=6)

# 添加数据标签 (紧贴圆点上方)
for i, val in enumerate(values):
    # 【核心修改】偏移量减小，让标签更贴近圆点
    offset = max(values) * 0.02
    ax.text(i, val + offset, str(val), color=text_color, ha='center', va='bottom',
            fontsize=10, zorder=7,
            # 圆角矩形背景框，padding 稍微调小
            bbox=dict(boxstyle="round,pad=0.3", fc=label_bg_color, ec='none', alpha=0.8))

# ==========================================
# 6. 坐标轴和网格线
# ==========================================
ax.set_ylim(0, 1200)
ax.set_yticks(np.arange(0, 1201, 200))

ax.yaxis.grid(True, color=grid_color, linestyle='--', linewidth=1, zorder=0)

for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis='x', colors=text_color, length=0, pad=12, labelsize=13)
ax.tick_params(axis='y', colors=text_color, length=0, pad=12, labelsize=12)

# ==========================================
# 7. 添加标题、副标题和脚注
# ==========================================
fig.text(0.08, 0.92, '3月商品销量对比', color=text_color, fontsize=26, fontweight='bold', ha='left')
fig.text(0.08, 0.86, '防晒销量最多，3月销量856；面膜最少，3月销量523', color=text_color, fontsize=14, ha='left')
fig.text(0.08, 0.02, '*注：数据来源于公司销售系统，统计日期截至2022.03.31', color='#A0B0D0', fontsize=9, ha='left')

plt.subplots_adjust(left=0.08, right=0.95, top=0.80, bottom=0.15)

# ==========================================
# 8. 显示图表
# ==========================================
plt.show()