import matplotlib.pyplot as plt


def extract_data_from_txt(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    operators_data = []
    for line in lines:
        if line.startswith('| Conv') or line.startswith('| Relu') or line.startswith('| MaxPool') or line.startswith(
                '| GlobalAveragePool') or line.startswith('| Flatten') or line.startswith('| Gemm'):
            operator, count_percentage = line.split(':')
            operator = operator.strip('| ')
            count, percentage = count_percentage.split(', ')
            percentage = float(percentage.strip('percentage='))
            operators_data.append((operator, percentage))
    return operators_data

def plot_pie_chart(operators_data, file_name):
    labels = [operator for operator, _ in operators_data]
    sizes = [percentage for _, percentage in operators_data]

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
    file_path = "/Users/gatilin/PycharmProjects/house-of-model-cards1/model_cards/timm/vgg/vgg11/vgg11.txt"
    operators_data = extract_data_from_txt(file_path)
    plot_pie_chart(operators_data, 'vgg11')