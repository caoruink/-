# -*- coding: cp936 -*-
import numpy
import csv


def data_choose(data_spliting, colarray):
    # pdb.set_trace()
    data_choosing = []  # 以数组形式记录各个股票的参数
    m = 0
    while m < len(data_spliting):
        t = []  # 记录一个股票的参数
        for j in colarray:
            t.append(float(data_spliting[m][j]))
        m += 1
        data_choosing.append(t)
    return data_choosing


def gbrt_predict(train, test, n, depth, filename):
    # from sklearn.metrics import mean_squared_error
    from sklearn.ensemble import GradientBoostingRegressor

    x1 = []  # 训练数据输入
    y1 = []  # 训练数据输出

    for line in train:
        x1.append(line[0:len(line) - 1])
        y1.append(float(line[len(line) - 1]))

    clf = GradientBoostingRegressor(n_estimators=n, learning_rate=0.3, max_depth=depth, random_state=0, loss='ls')
    clf = clf.fit(x1, y1)

    x2 = []  # 预测数据输入
    y2 = []  # 预测数据输出
    for line in test:
        x2.append(line[0:len(line) - 1])
        y2.append(float(line[len(line) - 1]))
    out = clf.predict(x2)

    outfile = open(filename, 'w+')
    for i in out:
        outfile.write("%s\n" % (i))

    feature_importance = clf.feature_importances_
    # print feature_importance
    feature_importance = 100.0 * (feature_importance / feature_importance.max())
    feature_importance_order = []
    feature_importance_ordered = []
    for each in feature_importance:
        feature_importance_ordered.append(each)
        feature_importance_order.append(each)
    feature_importance_order.sort(reverse=True)
    for each in feature_importance_ordered:
        print feature_importance_order.index(each) + 1
    print feature_importance
    outfile.write('\n')
    for eachone in feature_importance_order:
        outfile.write(str(eachone) + '\n')
    outfile.close()


def data_split(file):
    file.seek(0)
    line = file.readline()
    data_spliting = []
    while line != '':
        line = line.split(",")  # csv文件以‘,’分隔
        t = []  # 记录一个股票的参数
        j = 1
        while j <= num_attr:
            t.append(line[j])
            j += 1
        line = file.readline()
        data_spliting.append(t)
    return data_spliting


def data_solve():
    increasing = file('数据/increasing.txt', 'rb')
    predict1 = file('predict_gbrt/predict1.txt', 'rb')
    predict2 = file('predict_gbrt/predict2.txt', 'rb')
    predict3 = file('predict_gbrt/predict3.txt', 'rb')
    predict4 = file('predict_gbrt/predict4.txt', 'rb')
    predict5 = file('predict_gbrt/predict5.txt', 'rb')
    outfile = file('predict_gbrt/deal_data_result.csv', 'w+')

    line = increasing.readline()
    line1 = predict1.readline()
    line2 = predict2.readline()
    line3 = predict3.readline()
    line4 = predict4.readline()
    line5 = predict5.readline()

    newline = []
    another_line = []
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    while line != '':
        line = float(line.split('\n')[0])
        line1 = float(line1.split('\r')[0])
        line2 = float(line2.split('\r')[0])
        line3 = float(line3.split('\r')[0])
        line4 = float(line4.split('\r')[0])
        line5 = float(line5.split('\r')[0])
        t = []
        t.append(line)
        t.append(line1)
        t.append(line2)
        t.append(line3)
        t.append(line4)
        t.append(line5)
        t.append(abs(line1 - line)/t[0])
        t.append(abs(line2 - line)/t[0])
        t.append(abs(line3 - line)/t[0])
        t.append(abs(line4 - line)/t[0])
        t.append(abs(line5 - line)/t[0])
        print t[0], t[1], t[2], t[3], t[4], t[5]

        num1 += t[6]
        num2 += t[7]
        num3 += t[8]
        num4 += t[9]
        num5 += t[10]

        newline.append(t)
        i = 0
        while i < len(t) - 1:
            outfile.write(str(t[i]) + ',')
            i += 1
        outfile.write(str(t[i]) + '\n')
        line = increasing.readline()
        line1 = predict1.readline()
        line2 = predict2.readline()
        line3 = predict3.readline()
        line4 = predict4.readline()
        line5 = predict5.readline()

    outfile.write('\n' + ',' + str(num1 / len(newline)) + ',' + str(num2 / len(newline)) + ',' + str(
        num3 / len(newline)) + ',' + str(num4 / len(newline)) + ',' + str(num5 / len(newline)) + '\n')
    print str(num1 / len(newline)) + ',' + str(num2 / len(newline)) + ',' + str(
        num3 / len(newline)) + ',' + str(num4 / len(newline)) + ',' + str(num5 / len(newline))
    print str(1 - num1 / len(newline)) + ',' + str(1 - num2 / len(newline)) + ',' + str(
        1 - num3 / len(newline)) + ',' + str(1 - num4 / len(newline)) + ',' + str(1 - num5 / len(newline))

    increasing.close()
    predict1.close()
    predict2.close()
    predict3.close()
    predict4.close()
    predict5.close()
    outfile.close()
    print 'end!'


train = file('数据/train.csv', 'rb')
test = file('数据/test.csv', 'rb')
num_attr = 30
train_data = data_split(train)
test_data = data_split(test)
n_estimators = 600
max_depth = 4
i = 0
colarray1 = []
# 所有数据 0--19
colarray2 = []
# 原始数据+all百度指数  1.2.3.6-19
colarray3 = []
# 原始数据+募资 4-19
colarray4 = []
# 原始数据 6-19
colarray5 = []
# 行业百度指数+所有数据 1.6-19

while i < num_attr:
    colarray1.append(i)
    if i != 7:
        colarray2.append(i)
    '''
    if i != 8:
        colarray2.append(i)
    '''
    # if i != 0 and i != 18:
    if i != 8:
        colarray3.append(i)
    if i != 10:
        colarray4.append(i)
    # if i != 8 and i != 9:
    if i <= 16 or i == 29:
        colarray5.append(i)
    i += 1

gbrt_predict(data_choose(train_data, colarray1), data_choose(test_data, colarray1), n_estimators, max_depth,
             'predict_gbrt/predict1.txt')
gbrt_predict(data_choose(train_data, colarray2), data_choose(test_data, colarray2), n_estimators, max_depth,
             'predict_gbrt/predict2.txt')
gbrt_predict(data_choose(train_data, colarray3), data_choose(test_data, colarray3), n_estimators, max_depth,
             'predict_gbrt/predict3.txt')
gbrt_predict(data_choose(train_data, colarray4), data_choose(test_data, colarray4), n_estimators, max_depth,
             'predict_gbrt/predict4.txt')
gbrt_predict(data_choose(train_data, colarray5), data_choose(test_data, colarray5), n_estimators, max_depth,
             'predict_gbrt/predict5.txt')
data_solve()

train.close()
test.close()
print 'end!'
