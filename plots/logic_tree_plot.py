# import matplotlib.pyplot as plt
#
# tree = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': ['H', 'I'],
#     'E': [],
#     'F': [],
#     'G': [],
#     'H': [],
#     'I': []
# }
# def plot_tree(node, tree, x, y, dx, dy, ax):
#     ax.text(x, y, node, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))
#     children = tree[node]
#     if len(children) == 0:
#         return
#     dx = dx / len(children)
#     x_left = x - dx * (len(children) - 1) / 2
#     for child in children:
#         ax.plot([x, x_left], [y, y-dy], '-k')
#         plot_tree(child, tree, x_left, y-dy, dx, dy, ax)
#         x_left += dx
#
# # 创建画布和子图
# fig, ax = plt.subplots()
# # 设置坐标轴范围
# ax.set_xlim(0, 10)
# ax.set_ylim(0, 10)
# # 调用绘制函数
# plot_tree('A', tree, 5, 10, 8, 2, ax)
# # 隐藏坐标轴
# ax.axis('off')
# # 显示图形
# plt.show()

import matplotlib.pyplot as plt

def draw_tree(tree, root_node, x, y, dx, dy, node_style=None, branch_style=None):
    def plot_node(node, x, y, dx, dy, ax):
        ax.text(x, y, node, ha='center', va='center', bbox=node_style)

    def plot_branch(node, children, x, y, dx, dy, ax):
        if len(children) == 0:
            return
        dx_child = dx / len(children)
        x_left = x - dx_child * (len(children) - 1) / 2
        for child in children:
            ax.plot([x, x_left], [y, y - dy], **branch_style)
            plot_node(child, x_left, y - dy, dx, dy, ax)
            plot_branch(child, tree[child], x_left, y - dy, dx_child, dy, ax)
            x_left += dx_child

    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    plot_node(root_node, x, y, dx, dy, ax)
    plot_branch(root_node, tree[root_node], x, y, dx, dy, ax)

    ax.axis('off')
    plt.show()

if __name__ == '__main__':
    # 定义分支树
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
    # 定义节点样式和分支样式
    node_style = dict(facecolor='white', edgecolor='black', boxstyle='circle')
    branch_style = dict(color='black', linestyle='-')

    # 调用 draw_tree 函数绘制分支树
    draw_tree(tree, 'A', 5, 10, 8, 2, node_style, branch_style)