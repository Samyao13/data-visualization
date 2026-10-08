import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. 字体设置
# ==========================================
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ==========================================
# 2. 精准读取数据 (切换到工作表 '4 标注柱形图')
# ==========================================
file_path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(前15).xlsx"

try:
    sheet_name = '4 标注柱形图'  # 修改为第4个工作表
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=1)
    df.columns = df.columns.astype(str).str.strip()
    df = df.dropna(how='all')

    # 提取所有有效数据（不再限制6个）
    categories = df['月份'].tolist()
    values = df['销量'].tolist()

    print(f"✅ 成功提取数据: {list(zip(categories, values))}")

except Exception as e:
    print(f"读取文件出错: {e}")
    exit()

# ==========================================
# 3. 每个商品的专属颜色 (从原图取色)
# ==========================================
# 顺序：口红、面膜、隔离、防晒、精华、面霜、眼影、气垫
bar_colors = [
    '#5B9BD5',  # 口红 - 浅蓝
    '#4B9B8E',  # 面膜 - 青绿
    '#E26B4A',  # 隔离 - 橘红
    '#F2C63D',  # 防晒 - 黄色
    '#2E9BD6',  # 精华 - 亮蓝
    '#1F6FB2',  # 面霜 - 深蓝
    '#4C5FD5',  # 眼影 - 蓝紫
    '#6A5ACD',  # 气垫 - 紫罗兰
]

# 数据标签背景色（比柱子色稍深，带透明度）
label_colors = [
    '#4A7FB5', '#3D8074', '#B85A3D', '#C9A230',
    '#2378A8', '#1A588F', '#3E4EAB', '#564AA6'
]

# ==========================================
# 4. 绘图全局样式
# ==========================================
bg_color = '#1B1D36'  # 背景深蓝色
text_color = '#FFFFFF'  # 文字白色
grid_color = '#3A4060'  # 网格线暗蓝色

fig, ax = plt.subplots(figsize=(10, 6), facecolor=bg_color)
ax.set_facecolor(bg_color)

# ==========================================
# 5. 绘制纯色柱状图 (不再是渐变)
# ==========================================
bars = ax.bar(categories, values, width=0.5, color=bar_colors, zorder=3)

# ==========================================
# 6. 添加数据标签 (紧贴柱顶，背景色=柱子色加深)
# ==========================================
for i, (val, color) in enumerate(zip(values, label_colors)):
    # 偏移量很小，让标签紧贴柱顶
    offset = max(values) * 0.02
    ax.text(i, val + offset, str(val), color=text_color, ha='center', va='bottom',
            fontsize=11, zorder=7,
            bbox=dict(boxstyle="round,pad=0.3", fc=color, ec='none', alpha=0.85))

# ==========================================
# 7. 坐标轴和网格线
# ==========================================
ax.set_ylim(0, 10000)
ax.set_yticks(np.arange(0, 10001, 2000))  # 0, 2000, 4000, 6000, 8000, 10000

ax.yaxis.grid(True, color=grid_color, linestyle='--', linewidth=1, zorder=0)

for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis='x', colors=text_color, length=0, pad=12, labelsize=12)
ax.tick_params(axis='y', colors=text_color, length=0, pad=12, labelsize=11)

# ==========================================
# 8. 添加标题、副标题和脚注
# ==========================================
fig.text(0.08, 0.92, '2021年商品销量情况', color=text_color, fontsize=24, fontweight='bold', ha='left')
fig.text(0.08, 0.86, '口红销量最好达9221，是眼影最低值2645近3.5倍', color=text_color, fontsize=13, ha='left')
fig.text(0.08, 0.02, '*注：数据来源于公司销售系统，统计日期截至2022.08.31', color='#A0B0D0', fontsize=9, ha='left')

plt.subplots_adjust(left=0.08, right=0.95, top=0.80, bottom=0.15)

# ==========================================
# 9. 显示图表
# ==========================================
plt.show()