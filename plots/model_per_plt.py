import matplotlib.pyplot as plt

def extract_data_from_txt(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    start_flag = '===========================【operators】==========================='
    end_flag = '===========================【inputs】=============================='

    start_index = None
    end_index = None

    for i, line in enumerate(lines):
        if line.startswith(start_flag):
            start_index = i + 1
        elif line.startswith(end_flag):
            end_index = i - 1
            break

    if start_index is None or end_index is None:
        raise ValueError('Operators section not found in the file.')

    operators_data = []
    for line in lines[start_index:end_index + 1]:
        if line.startswith('|'):
            operator, count_percentage = line.split(':')
            operator = operator.strip('| ')
            count, percentage = count_percentage.split(', ')
            percentage = float(percentage.strip('percentage='))
            operators_data.append((operator, percentage))

    return operators_data


def plot_pie_chart(operators_data, file_name, top_n=10):
    print(operators_data)
    labels = [operator for operator, _ in operators_data]
    sizes = [percentage for _, percentage in operators_data]

    if len(labels) > top_n:
        labels = labels[:top_n]
        sizes = sizes[:top_n]
        labels.append('others')
        sizes.append(100 - sum(sizes))
    # Set the size of the figure using figsize parameter
    fig, ax = plt.subplots(figsize=(12, 8))
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    # Add legend with fontsize parameter to set the font size
    plt.title(f"Operators Percentage for {file_name}", y=1.05)
    plt.legend(wedges, labels, loc="lower right", bbox_to_anchor=(1, 0), fontsize=10)
    plt.savefig(f'{file_name}_operators_percentage_pie_chart.png')  # save the figure to file
    plt.show()

if __name__ == "__main__":
    # file_path = "/Users/gatilin/PycharmProjects/house-of-model-cards1/model_cards/timm/vgg/vgg11/vgg11.txt"
    # file_path = "/Users/gatilin/PycharmProjects/onnx-easy-tools/alexnet/alexnet.txt"
    # file_path = '/Users/gatilin/PycharmProjects/onnx-easy-tools/infos/mmyolo/yolov5_l-p6-v62_syncbn_fast_8xb16-300e_coco/yolov5_l-p6-v62_syncbn_fast_8xb16-300e_coco.txt'
    # file_path = '/Users/gatilin/PycharmProjects/onnx-easy-tools/infos/mmyolo/yolov5_l-p6-v62_syncbn_fast_8xb16-300e_coco/yolov5_l-p6-v62_syncbn_fast_8xb16-300e_coco.txt'
    # file_path = '/Users/gatilin/PycharmProjects/onnx-easy-tools/infos/detectron2/Cityscapes/mask_rcnn_R_50_FPN/mask_rcnn_R_50_FPN.txt'
    # file_path = '/Users/gatilin/PycharmProjects/onnx-easy-tools/infos/detectron2/COCO-Detection/rpn_R_50_C4_1x/rpn_R_50_C4_1x.txt'
    file_path = '/Users/gatilin/PycharmProjects/onnx-easy-tools/vgg16/vgg16.txt'
    file_name = file_path.split('/')[-1].split('.')[0]
    operators_data = extract_data_from_txt(file_path)
    plot_pie_chart(operators_data, file_name)