'''
pip install openpyxl
'''
import pandas as pd

# 读取Excel文件
input_file = "/Users/gatilin/youtu-work/mllm.xlsx"  # 请替换为你的Excel文件路径
output_file = "output.xlsx"  # 输出文件路径
df = pd.read_excel(input_file)

# 获取所有数值列的列名
numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
str_columns = df.select_dtypes(include=['object']).columns.tolist()
print("数值列：", numeric_columns)
print("字符串列：", str_columns)

# 根据每个数值列进行排序，并将排序后的数据存储到新的sheet中
with pd.ExcelWriter(output_file) as writer:
    for col in numeric_columns:
        sorted_df = df.sort_values(by=col)
        sorted_df.to_excel(writer, sheet_name=f'Sorted by {col}', index=False)

print("排序完成，结果已保存到", output_file)