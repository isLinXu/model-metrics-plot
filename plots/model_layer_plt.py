import re
from graphviz import Digraph

def extract_structure_info(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    structure_info = []
    for line in lines:
        if line.startswith('├─') or line.startswith('│'):
            structure_info.append(line.strip())

    return structure_info

def plot_structure_graph(structure_info, file_name):
    g = Digraph('G', format='png')

    for i, info in enumerate(structure_info):
        if info.startswith('├─'):
            layer_type, layer_name = info.strip('├─').split(':', 1)
            layer_name = layer_name.strip()
            g.node(layer_name, label=f"{layer_type}\n{layer_name}")
            if i > 0:
                parent_layer_name = structure_info[i - 1].strip('├─').split(':', 1)[1].strip()
                g.edge(parent_layer_name, layer_name)

    g.render(f"{file_name}_structure_graph", view=True)

if __name__ == "__main__":
    file_path = "/Users/gatilin/PycharmProjects/onnx-easy-tools/vgg16/vgg16.txt"
    # extract file name from file path
    file_name = file_path.split('/')[-1].split('.')[0]
    structure_info = extract_structure_info(file_path)
    plot_structure_graph(structure_info, file_name)