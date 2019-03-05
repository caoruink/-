# -*- coding:gbk -*-
import csv


def solve_id(filename, ids, website_name):
    # solve ids of stocks and websites
    for inline in filename:
        lines = inline.split(',')
        website_name.append(lines[0])
        id = int(lines[1].split('\n')[0])
        if id < 10000:
            ids.append('?00' + str(id))
        else:
            ids.append('?' + str(id))


if __name__ == '__main__':
    topic_id = file('topic_id.csv', 'rb')
    topics = file('eastmoney_topics.csv', 'rb')
    other_topics = file('eastmoney_topic3.csv', 'rb')
    features = file('other_features.csv', 'w+')
    identifier = []
    website_names = []
    solve_id(topic_id, identifier, website_names)
    line1 = topics.readline()
    # read titles
    line2 = other_topics.readline()
    # read titles
    index = 0
    # index of identifier and website_names
    features.write('股票代码,网址' + line1)
    line1 = topics.readline()
    line2 = other_topics.readline()
    for each in identifier:
        if line1 != [] or line2 != []:
            if line1.split(',')[0] == website_names[index]:
                content = line1
                line1 = topics.readline()
            else:
                if line2.split(',')[0] == website_names[index]:
                    content = line2
                    line2 = other_topics.readline()
                else:
                    break
        else:
            break
        features.write(identifier[index] + ',' + content.split('\r')[0] + '\n')
        index += 1
    topic_id.close()
    topics.close()
    other_topics.close()
    features.close()

