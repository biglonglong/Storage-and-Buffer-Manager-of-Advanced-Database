import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 示例数据
data = [
    ['lru', 'io number', 1, 552817],
    ['lru', 'hit rate(%)', 1, 33.914],
    ['lru', 'time(s)', 1, 2.683],
    ['lru', 'io number', 2, 475998],
    ['lru', 'hit rate(%)', 2, 42.592],
    ['lru', 'time(s)', 2, 5.371],
    ['lru', 'io number', 4, 337274],
    ['lru', 'hit rate(%)', 4, 57.055],
    ['lru', 'time(s)', 4, 5.418],
    ['lru', 'io number', 8, 366635],
    ['lru', 'hit rate(%)', 8, 54.994],
    ['lru', 'time(s)', 8, 5.149],
    ['lru', 'io number', 16, 373354],
    ['lru', 'hit rate(%)', 16, 54.573],
    ['lru', 'time(s)', 16, 5.105],
]

# 将数据转换为DataFrame
df = pd.DataFrame(data, columns=['Algorithm', 'Metric', 'Threads', 'Value'])

# 过滤使用lru算法的数据
df_lru = df[df['Algorithm'] == 'lru']

# 设置Seaborn样式
sns.set(style="whitegrid")

# 创建图形
fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制io number的折线图，使用左边的坐标轴
sns.lineplot(
    data=df_lru[df_lru['Metric'] == 'io number'], x="Threads", y="Value", marker="o", ax=ax1, label="IO Number"
)
ax1.set_ylabel('IO Number', fontsize=12)
ax1.tick_params(axis='y', labelsize=10)

# 绘制其他性能指标的折线图，使用右边的坐标轴
ax2 = ax1.twinx()
sns.lineplot(
    data=df_lru[df_lru['Metric'] == 'hit rate(%)'], x="Threads", y="Value", marker="s", ax=ax2, label="Hit Rate (%)", color="g"
)
sns.lineplot(
    data=df_lru[df_lru['Metric'] == 'time(s)'], x="Threads", y="Value", marker="D", ax=ax2, label="Time (s)", color="r"
)
ax2.set_ylabel('Hit Rate (%) / Time (s)', fontsize=12)
ax2.tick_params(axis='y', labelsize=10)

# 移除多余的网格线
ax1.grid(False)
ax2.grid(False)

# 添加标题
plt.title("Performance Comparison using LRU Algorithm", fontsize=16)

# 在图中标识不同数据的值
for line in ax1.lines:
    for x, y in zip(line.get_xdata(), line.get_ydata()):
        ax1.annotate(f'{y:.0f}', xy=(x, y), textcoords='offset points', xytext=(0, 5), ha='center')

for line in ax2.lines:
    for x, y in zip(line.get_xdata(), line.get_ydata()):
        ax2.annotate(f'{y:.3f}', xy=(x, y), textcoords='offset points', xytext=(0, 5), ha='center')

# 调整图例
lines_labels = [ax.get_legend_handles_labels() for ax in [ax1, ax2]]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
ax2.legend(lines, labels, loc='center right', title='Metric', fontsize=12, title_fontsize=12)

# 显示图形
plt.tight_layout()
plt.show()