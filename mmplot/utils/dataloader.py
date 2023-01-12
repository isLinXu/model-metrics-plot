
import math
import pandas
def pd_read_csv(csv_path):

    df = pandas.read_csv(csv_path)
    # print(df)
    return df

def fps_to_ms(fps: int) -> int:
    '''
    Convert FPS to a millisecond interval.
    Args:
        fps: Input FPS as integer.
    Returns:
        Interval in milliseconds as integer number.
    '''
    return math.floor((1 / fps) * 1000)

if __name__ == '__main__':
    csv_path = '/data/model_data.csv'
    df = pd_read_csv(csv_path)
    print(df.shape)  # 返回df的行数和列数
    print(df.shape[0])  # 返回df的行数
    print(df.shape[1])  # 返回df的列数

