import matplotlib.pyplot as plt

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}
def plot_tree(node, tree, x, y, dx, dy, ax):
    ax.text(x, y, node, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))
    children = tree[node]
    if len(children) == 0:
        return
    dx = dx / len(children)
    x_left = x - dx * (len(children) - 1) / 2
    for child in children:
        ax.plot([x, x_left], [y, y-dy], '-k')
        plot_tree(child, tree, x_left, y-dy, dx, dy, ax)
        x_left += dx

# 创建画布和子图
fig, ax = plt.subplots()
# 设置坐标轴范围
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
# 调用绘制函数
plot_tree('A', tree, 5, 10, 8, 2, ax)
# 隐藏坐标轴
ax.axis('off')
# 显示图形
plt.show()