import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# ==========================================
# 1. 设置中文字体 (防止中文乱码)
# ==========================================
# Windows 系统通常使用 SimHei (黑体) 或 Microsoft YaHei (微软雅黑)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# ==========================================
# 2. 读取数据
# ==========================================
file_path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(前15).xlsx"

# 读取 Excel 文件
# 注意：根据截图，数据可能在第一个 Sheet，且表头在第一行
try:
    df = pd.read_excel(file_path, header=1, usecols="B:C")

    # 打印前几行检查数据是否正确读取
    print("数据读取成功，前5行如下：")
    print(df.head())

    # 确保列名没有多余空格
    df.columns = df.columns.str.strip()

    # 假设 Excel 中的列名分别为 "区域" 和 "销售量"
    # 如果列名不同，请在这里修改
    categories = df['区域'].tolist()
    values = df['销售量'].tolist()

except Exception as e:
    print(f"读取文件出错: {e}")
    # 如果文件读取失败，为了演示代码效果，我这里手动创建一个数据副本
    # 实际运行时请确保路径正确
    data = {
        '区域': ['华北', '华南', '东北', '西北', '西南', '华东'],
        '销售量': [2354, 1902, 3524, 2698, 2896, 2563]
    }
    df = pd.DataFrame(data)
    categories = df['区域'].tolist()
    values = df['销售量'].tolist()

# ==========================================
# 3. 绘图设置
# ==========================================
# 设置画布大小 (宽, 高)
fig, ax = plt.subplots(figsize=(10, 6))

# 设置背景颜色 (深蓝色)
bg_color = '#0e1a3c'  # 根据图片吸取的颜色
fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

# 绘制柱状图
# color: 柱子的颜色 (亮蓝色)
# width: 柱子的宽度
bars = ax.bar(categories, values, color='#0099ff', width=0.35, zorder=3)

# ==========================================
# 4. 添加数据标签 (柱子上方的数字)
# ==========================================
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 50,
            f'{int(height)}',
            ha='center', va='bottom',
            color='white', fontsize=11, fontweight='bold')

# ==========================================
# 5. 图表美化 (坐标轴、网格、标题)
# ==========================================

# --- 标题设置 ---
# 主标题 (使用 ax.text 以便更灵活地控制位置)
ax.text(0.5, 1.15, "3月各区域销量分布",
        transform=ax.transAxes,
        ha='center', va='bottom',
        fontsize=24, color='white', fontweight='bold')

# 副标题
ax.text(0.5, 1.08, "东北销量最多占总销量的22%，华南销量最低",
        transform=ax.transAxes,
        ha='center', va='bottom',
        fontsize=14, color='#d0d0d0')

# --- 坐标轴设置 ---
# 隐藏上边框和右边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# 左边框和下边框设为白色
ax.spines['left'].set_color('white')
ax.spines['bottom'].set_color('white')

# 设置刻度标签颜色为白色
ax.tick_params(axis='x', colors='white', labelsize=12)
ax.tick_params(axis='y', colors='white', labelsize=10)

# --- 网格线设置 ---
# 只显示 Y 轴网格，虚线，颜色淡灰
ax.yaxis.grid(True, linestyle='--', alpha=0.3, color='gray', zorder=0)

# ==========================================
# 在 ax.yaxis.grid(...) 之后，添加以下内容
# ==========================================

# 1. 设置 Y 轴刻度范围与间隔
ax.set_ylim(0, 4000)                    # Y 轴范围 0 ~ 4000
ax.set_yticks([0, 1000, 2000, 3000, 4000])   # 刻度只显示这几个

# ==========================================
# 2. 修改底部注释的位置
# 原来：plt.figtext(0.15, 0.02, ...)  → 位置太靠上，被柱子挡住
# 修改为：放到画布最底部
plt.figtext(0.13, 0.005,
            "*注：数据来源于公司销售系统，统计日期截至2022.03.31",
            ha='left', fontsize=9, color='#d0d0d0')

# ==========================================
# 6. 显示图表
# ==========================================
plt.tight_layout()
plt.subplots_adjust(bottom=0.12)   # 底部留出更多空间
plt.show()