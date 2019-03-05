# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import pdb


class Spider:
    def __init__(self, web_name):
        self.siteURL = web_name

    def getPage(self):
        url = self.siteURL
        print url
        status = urllib.urlopen(url).code
        request = urllib2.Request(url)
        if status == 200:
            response = urllib2.urlopen(request)
            return response.read().decode("utf-8").encode('utf-8')
        else:
            return 'wrong'

    def getContents(self):
        page = self.getPage()
        # pdb.set_trace()
        if page != 'wrong':
            '''
            pattern = re.compile('申购状况.*?<td>网上发行中签率.*?&nbsp;(.*?)</td>            <td>网下配售中签率',re.S)
            item = re.findall(pattern, page)
            print item'''
            pattern1 = re.compile('<td>网上发行中签率.*?</td>            <td>&nbsp;(.*?)</td>.*?'
                                  '网下配售中签率.*?</td>            <td>(.*?)</td>', re.S)
            item1 = re.findall(pattern1, page)
            if item1 != []:
                for each in item1:
                    for one in each:
                        if one != []:
                            out.write(str(one) + ',')
                        else:
                            out.write('error,')
            else:
                out.write('error,error,')
            pattern2 = re.compile('<td>发行前每股净资产（元）</td>            <td>(.*?)</td>.*?'
                                  '<td>首日换手率.*?</td>            <td>(.*?)</td>.*?首日最高涨幅', re.S)
            item2 = re.findall(pattern2, page)
            if item2 != []:
                for each in item2:
                    for one in each:
                        if one != []:
                            out.write(str(one) + ',')
                        else:
                            out.write('error,')
            else:
                out.write('error,error,')
            pattern3 = re.compile('<td colspan="2">投资金额总计</td>            <td>(.*?)</td>', re.S)
            item3 = re.findall(pattern3, page)
            if item3 != []:
                out.write(str(item3[0]) + ',')
            else:
                out.write('error,')
            '''
            pattern4 = re.compile('总资产（亿元）.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?'
                                  '</tr>.*?'
                                  '净资产（亿元）.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?<td>.*?'
                                  '</td>.*?</tr>.*?少数股东权益（万元）.*?'
                                  '营业收入（亿元）.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?'
                                  '</tr>.*?'
                                  '净利润（亿元）.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?'
                                  '</tr>.*?'
                                  '资本公积（万元）.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?'
                                  '</tr>.*?'
                                  '未分配利润（亿元）.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?<td>.*?</td>'
                                  '.*?</tr>.*?'
                                  '基本每股收益（元）.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?'
                                  '<td>.*?</td>.*?</tr>.*?稀释每股收益（元）.*?每股现金流.*?'
                                  '净资产收益率.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?'
                                  '/tr>', re.S)'''
            pattern4 = re.compile('总资产（亿元）.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?</tr>.*?<tr>.*?'
                                  '净资产（亿元）.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?</tr>.*?<tr>.*?'
                                  '营业收入（亿元）.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?/td>.*?</tr>.*?<tr>.*?'
                                  '净利润（亿元）.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?</tr>.*?<tr>.*?'
                                  '资本公积.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?</tr>.*?<tr>.*?'
                                  '未分配利润.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?</tr>.*?<tr>.*?'
                                  '基本每股收益.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?</tr>.*?<tr>.*?'
                                  '净资产收益率.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?</tr>', re.S)
            item4 = re.findall(pattern4, page)
            if item4 != []:
                for each in item4:
                    for one in each:
                        if one != []:
                            out.write(str(one) + ',')
                        else:
                            out.write('error,')
                out.write('\n')
            else:
                out.write('error,error,error,error,error,error,error,error\n')
            # print item

        else:
            out.write(self.siteURL + 'error' + ',' + 'error' + ',' + 'error' + ',' + 'error' + '\n')

if __name__ == "__main__":
    topics = file('topic3.csv', 'rb')
    websites = []
    for inline in topics:
        websites.append(inline.split('\r')[0])
    out = file('eastmoney_topic3.csv', 'w+')
    out.write('网上发行中签率,网下配售中签率,发行前每股净资产,首日换手率,投资金额总计,总资产,净资产,营业收入,'
              '净利润,资本公积,未分配利润,基本每股收益,净资产收益率\n')

    for eachone in websites:
        spider = Spider(eachone)
        spider.getContents()
    # spider = Spider('http://topic.eastmoney.com/hnsw/')
    # spider.getContents()
    out.close()
