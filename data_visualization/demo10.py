import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r"C:\Users\LENOVO\Desktop\数据可视化\第二章 图表(前15).xlsx"
df = pd.read_excel(path, sheet_name='10 甘特图', header=2)
df = df.iloc[:, 1:7].dropna(subset=['项目名称'])
df.columns = ['项目名称', '开始日期', '项目天数', '完成度', '进行天数', '结束日期']
df['开始日期'] = pd.to_datetime(df['开始日期'])
df['结束日期'] = pd.to_datetime(df['结束日期'])

fig, ax = plt.subplots(figsize=(12, 5.5))
fig.patch.set_facecolor('#1B2A4A')
ax.set_facecolor('#1B2A4A')

n = len(df)
y = np.arange(n)[::-1]

start = pd.Timestamp('2022-03-01')
end   = pd.Timestamp('2022-06-14')
ticks = pd.date_range(start=start, end=end, freq='15D')

for t in ticks:
    ax.axvline(t, color='#B0B8C8', linestyle=(0, (3, 4)),
               linewidth=0.7, alpha=0.55)

DEEP  = '#1F5FB0'   # 深蓝：已完成
LIGHT = '#3FA9F5'   # 浅蓝：未完成

for i, (_, row) in enumerate(df.iterrows()):
    ypos = y[i]
    s = row['开始日期']
    e = row['结束日期']
    done_days = row['进行天数']
    total_days = row['项目天数']
    h = 0.30

    # 交界点：开始日期 + 进行天数
    x_done = s + pd.Timedelta(days=done_days)

    # 深蓝段：开始 -> 完成
    ax.barh(ypos, x_done - s, left=s, height=h,
            color=DEEP, edgecolor='none')
    # 浅蓝段：完成 -> 结束
    ax.barh(ypos, e - x_done, left=x_done, height=h,
            color=LIGHT, edgecolor='none')

    # 百分比放在交界点上
    ax.text(x_done, ypos, f"{row['完成度']:.0%}",
            ha='center', va='center', fontsize=9, color='white')

ax.set_xticks(ticks)
ax.set_xticklabels([f"{t.year}/{t.month}/{t.day}" for t in ticks],
                   fontsize=9, color='white')
ax.xaxis.set_ticks_position('top')
ax.tick_params(axis='x', colors='white', length=0, pad=4)

ax.set_yticks(y)
ax.set_yticklabels(df['项目名称'], fontsize=10, color='white')
ax.tick_params(axis='y', colors='white', length=0, pad=4)

for s_ in ax.spines.values():
    s_.set_visible(False)

ax.set_xlim(start - pd.Timedelta(days=2), end + pd.Timedelta(days=2))
ax.set_ylim(-0.5, n - 0.5)

ax.text(0.0, 1.18, '2022年化妆品类目采购项目进度',
        transform=ax.transAxes, fontsize=17, fontweight='bold',
        color='white', va='bottom', ha='left')

plt.subplots_adjust(top=0.80, bottom=0.05, left=0.10, right=0.985)
plt.show()