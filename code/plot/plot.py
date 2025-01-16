import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 示例数据
data = [
    ['lru', 'io number', 1, 552817],
    ['lru', 'hit rate(%)', 1, 33.914],
    ['lru', 'time(s)', 1, 2.683],
    ['clock', 'io number', 1, 561828],
    ['clock', 'hit rate(%)', 1, 32.883],
    ['clock', 'time(s)', 1, 2.810],
    ['2Q', 'io number', 1, 470364],
    ['2Q', 'hit rate(%)', 1, 43.501],
    ['2Q', 'time(s)', 1, 2.184],
]

# 将数据转换为DataFrame
df = pd.DataFrame(data, columns=['Algorithm', 'Metric', 'Threads', 'Value'])

# 过滤线程为1的数据
df_thread_1 = df[df['Threads'] == 1]

# 设置Seaborn样式
sns.set(style="whitegrid")

# 创建图形
fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制io number的柱状图，使用左边的坐标轴
sns.barplot(
    data=df_thread_1[df_thread_1['Metric'] == 'io number'], x="Metric", y="Value", hue="Algorithm", palette="muted", ax=ax1
)
ax1.set_ylabel('IO Number', fontsize=12)
ax1.tick_params(axis='y', labelsize=10)

# 绘制其他性能指标的柱状图，使用右边的坐标轴
ax2 = ax1.twinx()
sns.barplot(
    data=df_thread_1[df_thread_1['Metric'] != 'io number'], x="Metric", y="Value", hue="Algorithm", palette="muted", ax=ax2
)
ax2.set_ylabel('Hit Rate (%) / Time (s)', fontsize=12)
ax2.tick_params(axis='y', labelsize=10)

# 移除多余的网格线
ax1.grid(False)
ax2.grid(False)

# 添加标题
plt.title("Performance Comparison at Thread=1", fontsize=16)

# 在图中标识不同数据的值
for p in ax1.patches:
    ax1.annotate(format(p.get_height(), '.0f'),  # 显示为整数
                 (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='center',
                 xytext=(0, 9), textcoords='offset points')

for p in ax2.patches:
    ax2.annotate(format(p.get_height(), '.3f'),
                 (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='center',
                 xytext=(0, 9), textcoords='offset points')



# 调整图例
ax1.legend_.remove()
ax2.legend(title='Algorithm', fontsize=12, title_fontsize=12)

# 显示图形
plt.tight_layout()
plt.show()