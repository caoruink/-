import time
import datetime
import csv
import os
from os.path import join


def create_time_series(start_time, end_time, interval):
    # 生成要提取的数据的时间
    start_time = time.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    time_series = []
    time_series.append(start_time)
    while start_time <= end_time:
        start_time = (starttime + datetime.timedelta(minutes=interval))
        time_series.append(start_time)
    return time_series


def choose_data(data_raw, attr_array, time_series):
    lines_num = len(data_raw)
    line_index = 0
    attr_number = len(attr_array)
    attr_index = 0
    while line_index < lines_num:
        if data_raw[line_index, 0] == "time" and data_raw[line_index + 1, 0] == attr_array[attr_index]:
            start_col_index = 1
            col_number = len(data_raw[line_index, ])
            time_series_index = 0
            while start_col_index < col_number and :
                tmp_time = time.strptime(data_raw[line_index, col_number])
                if tmp_time < 


def solve_file(floder, attr_array, time_series):
    outfile_name = floder + 'disk_net.csv'
    outfile = open(outfile_name, 'wb')
    root_dir = floder
    # 遍历的文件夹
    for parent, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            infile = file(file_path, "rb")
            reader = csv.reader(infile)
            choose_data(reader, attr_array, time_series)
            csv.close(infile)