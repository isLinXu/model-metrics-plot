import re
from graphviz import Digraph

def extract_structure_info(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.startswith(('├─', '│'))]

def plot_structure_graph(structure_info, file_name):
    g = Digraph('G', format='png')
    pattern = re.compile(r'├─(.+):(.+)')
    parent_layer_name = None
    for info in structure_info:
        match = pattern.match(info)
        if match:
            layer_type, layer_name = match.groups()
            layer_name = layer_name.strip()
            g.node(layer_name, label=f"{layer_type}\n{layer_name}")
            if parent_layer_name:
                g.edge(parent_layer_name, layer_name)
            parent_layer_name = layer_name

    g.render(f"{file_name}_structure_graph", view=True)


if __name__ == "__main__":
    # file_path = input("请输入文件路径: ")  # 通过用户输入获取文件路径
    file_path = "/Users/gatilin/PycharmProjects/onnx-easy-tools/vgg16/vgg16.txt"
    file_name = file_path.split('/')[-1].split('.')[0]
    structure_info = extract_structure_info(file_path)
    if structure_info:  # 只有在提取到结构信息时才绘制图形
        plot_structure_graph(structure_info, file_name)