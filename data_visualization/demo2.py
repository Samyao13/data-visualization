import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. 字体设置
# ==========================================
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ==========================================
# 2. 读取数据（包含新增的 D 列）
# ==========================================
file_path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(前15).xlsx"

# 只读 B、C 列（区域、销售量）；如果你想读均值，改成 usecols="B:D"
df = pd.read_excel(file_path, header=1, usecols="B:C")
df.columns = df.columns.str.strip()

categories = df['区域'].tolist()
values = df['销售量'].tolist()

# ✅ 计算平均值（对应 Excel 的 D3 公式）
avg_value = sum(values) / len(values)   # 2656.166...
avg_value_int = int(round(avg_value))   # 显示为 2656

print("分类：", categories)
print("数值：", values)
print("平均值：", avg_value_int)

# ==========================================
# 3. 绘图
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6))

bg_color = '#0e1a3c'
fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

bars = ax.bar(categories, values, color='#0099ff', width=0.35, zorder=3)

# 数据标签（柱子上方数字）
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 50,
            f'{int(height)}',
            ha='center', va='bottom',
            color='white', fontsize=11, fontweight='bold')

# 标题
ax.text(0.5, 1.15, "3月各区域销量分布",
        transform=ax.transAxes, ha='center', va='bottom',
        fontsize=24, color='white', fontweight='bold')

ax.text(0.5, 1.08, "东北销量最多占总销量的22%，华南销量最低",
        transform=ax.transAxes, ha='center', va='bottom',
        fontsize=14, color='#d0d0d0')

# ✅ 新增：黄色平均值水平线
ax.axhline(y=avg_value, color='#FFD700', linewidth=2, zorder=4, label='平均值')

# ✅ 新增：右侧"平均值：2656"标签
ax.text(len(categories) - 0.3, avg_value + 60,
        f'平均值：{avg_value_int}',
        color='#FFD700', fontsize=11, fontweight='bold',
        ha='right', va='bottom', zorder=5)

# 坐标轴美化
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('white')
ax.spines['bottom'].set_color('white')

ax.tick_params(axis='x', colors='white', labelsize=12)
ax.tick_params(axis='y', colors='white', labelsize=10)

# Y 轴范围与刻度
ax.set_ylim(0, 4000)
ax.set_yticks([0, 1000, 2000, 3000, 4000])

# 网格线
ax.yaxis.grid(True, linestyle='--', alpha=0.3, color='gray', zorder=0)

# 底部注释
plt.figtext(0.13, 0.005,
            "*注：数据来源于公司销售系统，统计日期截至2022.03.31",
            ha='left', fontsize=9, color='#d0d0d0')

plt.tight_layout()
plt.subplots_adjust(bottom=0.12)
plt.show()