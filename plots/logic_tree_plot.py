
import matplotlib.pyplot as plt

def draw_tree(tree, root_node, x, y, dx, dy, node_style=None, branch_style=None,debug=False):
    '''
    绘制逻辑树
    Args:
        tree:  dict, 树的结构
        root_node:  str, 根节点
        x: float, 根节点的x坐标
        y: float, 根节点的y坐标
        dx: float, x方向的间距
        dy: float, y方向的间距
        node_style: 节点样式
        branch_style: 分支样式

    Returns:

    '''
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

    if debug:
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