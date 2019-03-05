# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import pdb


class Spider:
    def __init__(self, page):
        self.siteURL = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=NS&sty=NSST&st=%2012&sr=-1&p='\
                       + str(page) + '&ps=100&stat=1&rt=47532300'

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
            pattern = re.compile('".*?"', re.S)
            item = re.findall(pattern, page)
            # print item
            if item != []:
                for each in item:
                    each = each.split('"')[1]
                    out.write(str(each) + '\n')
            else:
                out.write('error\n')
        else:
            out.write('error' + ',' + 'error' + ',' + 'error' + ',' + 'error' + '\n')

if __name__ == "__main__":
    pages = [1, 2, 3, 4, 5, 6]
    out = file('eastmoney.csv', 'w+')
    for each in pages:
        spider = Spider(each)
        spider.getContents()
    out.close()
