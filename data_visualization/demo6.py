import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. 字体设置
# ==========================================
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ==========================================
# 2. 读取数据
# ==========================================
file_path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(前15).xlsx"
xls = pd.ExcelFile(file_path)

target_sheet = None
for name in xls.sheet_names:
    df_test = pd.read_excel(file_path, sheet_name=name, header=None)
    if df_test.astype(str).apply(
        lambda c: c.str.contains('2022年销量').any()
    ).any():
        target_sheet = name
        break

print(f"正在读取 Sheet：{target_sheet}")

df = pd.read_excel(file_path, sheet_name=target_sheet, header=1, usecols="B:F")
df.columns = df.columns.astype(str).str.strip()

regions = df['区域'].tolist()
sales_2022 = df['2022年销量'].astype(int).tolist()
sales_2021 = df['2021年销量'].astype(int).tolist()

# ==========================================
# 3. 绘图
# ==========================================
fig, ax = plt.subplots(figsize=(15, 7))

bg_color = '#0e1a3c'
fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

y = np.arange(len(regions))
bar_height = 0.5

gap = 250

# 左侧蓝柱：从 -val 到 -gap（左对齐）→ 用左边起点、宽度
left_start  = [-v for v in sales_2022]         # 左端
left_width  = [v - gap for v in sales_2022]    # 宽度 = 总长 - gap

bars_left = ax.barh(y, left_width, left=left_start,
                    height=bar_height, color='#0099ff',
                    edgecolor='white', linewidth=0.2, zorder=3)

# 右侧粉柱：从 +gap 到 +val
right_start = [gap for _ in sales_2021]        # 左端从 +gap 开始
right_width = [v - gap for v in sales_2021]    # 宽度 = 总长 - gap

bars_right = ax.barh(y, right_width, left=right_start,
                     height=bar_height, color='#ff5577',
                     edgecolor='white', linewidth=0.2, zorder=3)

# ==========================================
# 4. 数值标签（显示在柱子内部靠外端）
# ==========================================
for bar, val in zip(bars_left, sales_2022):
    ax.text(-val + 30, bar.get_y() + bar.get_height()/2,
            f'{val}',
            ha='left', va='center',
            color='white', fontsize=15, fontweight='bold', zorder=5)

for bar, val in zip(bars_right, sales_2021):
    ax.text(val - 30, bar.get_y() + bar.get_height()/2,
            f'{val}',
            ha='right', va='center',
            color='white', fontsize=15, fontweight='bold', zorder=5)

# ==========================================
# 5. 中心区域名（放在 gap 正中间）
# ==========================================
for i, region in enumerate(regions):
    ax.text(0, i, region, ha='center', va='center',
            color='white', fontsize=18, fontweight='bold', zorder=6)

# ==========================================
# 6. 顶部"2022" / "2021"
# ==========================================
max_val = max(max(sales_2021), max(sales_2022))

ax.text(-max_val * 0.5, len(regions) - 0.5, "2022",
        ha='center', va='bottom',
        color='#0099ff', fontsize=20, fontweight='bold')
ax.text(max_val * 0.5, len(regions) - 0.5, "2021",
        ha='center', va='bottom',
        color='#ff5577', fontsize=20, fontweight='bold')

# ==========================================
# 7. 标题与副标题
# ==========================================
ax.text(0.5, 1.10, "2022年上半年各区域对比去年销量",
        transform=ax.transAxes, ha='center', va='bottom',
        fontsize=22, color='white', fontweight='bold')

ax.text(0.5, 1.04, "2022年整体销量高于2021年，只有东北区域较2021有所下降",
        transform=ax.transAxes, ha='center', va='bottom',
        fontsize=13, color='#d0d0d0')

# ==========================================
# 8. 隐藏坐标轴 + 调整留白
# ==========================================
ax.set_yticks([])
ax.set_xticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_xlim(-max_val * 1.6, max_val * 1.6)
ax.set_ylim(-0.6, len(regions) - 0.2)

# ==========================================
# 9. 底部注释
# ==========================================
plt.figtext(0.10, 0.02,
            "*注：数据来源于公司销售系统，统计日期截至2022.06.30",
            ha='left', fontsize=9, color='#d0d0d0')

plt.tight_layout()
plt.subplots_adjust(bottom=0.10)
plt.show()