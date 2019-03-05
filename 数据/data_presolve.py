# -*- coding: utf-8 -*-
from sklearn import preprocessing
import random


def max_min():
    basefile = file('base_inc.csv', 'rb')
    outfile = file('all_inc.csv', 'w+')
    basefile.seek(0)
    line = basefile.readline()
    linenum = 0
    text = []
    identifier = []
    while line != '':
        linetext = []
        temptext = []
        linetext = line.split(',')
        identifier.append(linetext[0])
        i = 1
        while i < len(linetext):
            temptext.append(float(linetext[i]))
            i += 1
        text.append(temptext)
        linenum += 1
        line = basefile.readline()
    min_max_scaler = preprocessing.MinMaxScaler()
    text_minmax = min_max_scaler.fit_transform(text)
    i = 0
    while i < len(identifier):
        outfile.write(identifier[i] + ',')
        for each in text_minmax[i]:
            outfile.write(str(each)+',')
        outfile.write('\n')
        i += 1
    basefile.close()
    outfile.close()


def data_alloc():
    train = file('train_inc.csv', 'w+')
    test = file('test_inc.csv', 'w+')
    data_all = file('all_inc.csv', 'rb')
    increasing = file('increasing.txt', 'w+')
    data_all.seek(0)
    line = data_all.readline()
    i = 0
    linenum = 0
    randomnum = []
    while i < 50:
        randomnum.append(random.randint(1, 280))
        i += 1
    randomnum = list(set(randomnum))
    print len(randomnum)
    randomnum.sort()
    i = 0
    '''
    randomnum = [16, 22, 25, 26, 32, 48, 53, 65, 72, 73, 85, 88, 91, 95, 99, 103, 113, 114, 116, 117,
                 120, 127, 147, 149, 158, 160, 166, 175, 181, 185, 205, 215, 217, 223, 247, 250, 255, 257, 260, 269,
                 276, 278, 280]'''
    print len(randomnum)
    print randomnum
    index_sample = file('index_sample.txt', 'w+')
    for each in randomnum:
        index_sample.write(str(each) + '\n')
        each -= 1
    index_sample.close()
    while line != '':
        if i < len(randomnum) and linenum != randomnum[i]:
            train.write(line.split('\r')[0]+'\n')
            linenum += 1
        else:
            if i == len(randomnum):
                train.write(line.split('\r')[0] + '\n')
                linenum += 1
            else:
                test.write(line.split('\r')[0]+'\n')
                increasing.write(line.split(',')[-1])
                linenum += 1
                i += 1
        line = data_all.readline()

    train.close()
    test.close()
    data_all.close()

# max_min()
data_alloc()
print 'end!'
