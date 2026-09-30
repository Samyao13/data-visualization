import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. 字体设置
# ==========================================
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ==========================================
# 2. 读取数据（需确认 Sheet 名和范围）
# ==========================================
file_path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(前15).xlsx"
sheet_name = "8 数值百分比"    # ⚠️ 请根据扫描结果改成实际 Sheet 名

df = pd.read_excel(file_path, sheet_name=sheet_name, header=1, usecols="B:D")
df.columns = df.columns.astype(str).str.strip()

print(df)

regions  = df['区域'].tolist()
val_2022 = df['2022年'].astype(str).str.rstrip('%').astype(float).tolist()
val_2021 = df['2021年'].astype(str).str.rstrip('%').astype(float).tolist()

# ==========================================
# 3. 绘图
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6))

bg_color = '#0e1a3c'
fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

y = np.arange(len(regions))
bar_height = 0.35

# --- 左侧蓝条（负值，向左延伸）---
bars_left = ax.barh(y, [-v for v in val_2022],
                    height=bar_height, color='#0099ff',
                    edgecolor='none', linewidth=0, zorder=3)

# --- 右侧粉条（正值，向右延伸）---
bars_right = ax.barh(y, val_2021,
                     height=bar_height, color='#ff5577',
                     edgecolor='none', linewidth=0, zorder=3)

# ==========================================
# 4. 数值标签（显示在柱外两端）
# ==========================================
# 左侧蓝条数值：显示在柱子左端外侧
for bar, val in zip(bars_left, val_2022):
    ax.text(-val - 1, bar.get_y() + bar.get_height()/2,
            f'{int(val)}%',
            ha='right', va='center',
            color='white', fontsize=10, fontweight='bold', zorder=5)

# 右侧粉条数值：显示在柱子右端外侧
for bar, val in zip(bars_right, val_2021):
    ax.text(val + 1, bar.get_y() + bar.get_height()/2,
            f'{int(val)}%',
            ha='left', va='center',
            color='white', fontsize=10, fontweight='bold', zorder=5)

# ==========================================
# 5. 中心区域名
# ==========================================
for i, region in enumerate(regions):
    ax.text(0, i, region, ha='center', va='center',
            color='white', fontsize=12, fontweight='bold', zorder=6)

# ==========================================
# 6. 标题与副标题
# ==========================================
ax.text(0.5, 1.12, "2022年第一季度销售目标完成情况",
        transform=ax.transAxes, ha='center', va='bottom',
        fontsize=20, color='white', fontweight='bold')

ax.text(0.5, 1.05, "华东区域完成率最高达到36%，但是相比去年的42%有所下降",
        transform=ax.transAxes, ha='center', va='bottom',
        fontsize=12, color='#d0d0d0')

# ==========================================
# 7. 隐藏坐标轴
# ==========================================
ax.set_yticks([])
ax.set_xticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

max_val = max(max(val_2021), max(val_2022))
ax.set_xlim(-max_val * 1.3, max_val * 1.3)
ax.set_ylim(-0.6, len(regions) - 0.2)

# ==========================================
# 8. 底部注释
# ==========================================
plt.figtext(0.10, 0.02,
            "*注：数据来源于公司销售系统，统计日期截至2022.03.31",
            ha='left', fontsize=9, color='#d0d0d0')

plt.tight_layout()
plt.subplots_adjust(bottom=0.10)
plt.show()