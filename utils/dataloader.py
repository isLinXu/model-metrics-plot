import math


def fps_to_ms(fps: int) -> int:
    '''
    Convert FPS to a millisecond interval.
    Args:
        fps: Input FPS as integer.
    Returns:
        Interval in milliseconds as integer number.
    '''
    return math.floor((1 / fps) * 1000)


def csv_to_dict(csv):
    d_list = []
    with open(csv, 'r') as f:
        lines = f.read().splitlines()
    d = {}  # dict
    title = lines[0].split(',')
    data = []
    for i in range(1, len(lines)):
        line = lines[i].split(',')
        # print('line:', line)
        data.append(line)
        # for j in range(len(title)):
        # d[title[j]] = line[j]

        # d_list.append(d)

    for j in range(len(data)):
        m_data = data[j]
        print('m_data:', m_data)
        for i in range(len(m_data)):
            d[title[i]] = m_data[i]
            print('d:', d)
            #             d[title[i]] = data[i]
            # for line in lines:
            #     if line:
            #         data = line.split(',')
            #         print('data:', data)
            #         for i in range(len(data)):
            #             d[title[i]] = data[i]
            #             print('d:', d)
            d_list.append(d)
    return d_list


def csv_dict_list(csv_path):
    from csv import DictReader
    with open(csv_path, 'r') as read_obj:
        dict_reader = DictReader(read_obj)
        print(read_obj)
        list_of_dict = list(dict_reader)
        print(list_of_dict)
        for k, v in list_of_dict.items():
            print(k, v)


import csv

import pandas
def pd_read_csv(csv_path):

    df = pandas.read_csv(csv_path)
    # print(df)
    return df

if __name__ == '__main__':
    # csv_path = '/home/linxu/PycharmProjects/model-metrics-plot/data/test.csv'
    csv_path = '/data/model_data.csv'
    # csv_dict = csv_to_dict(csv_path)
    # print('csv_dict:', csv_dict)
    # for m_data in csv_dict:
    #     print('i_data:', m_data)
    # csv_dict_list(csv_path)
    # csv_read_pandas(csv_path)
    df = pd_read_csv(csv_path)

    print(df.shape)  # 返回df的行数和列数
    print(df.shape[0])  # 返回df的行数
    print(df.shape[1])  # 返回df的列数

