import json
import scrapy
import datetime
from scrapy.http import HtmlResponse
from bs4 import BeautifulSoup
from scrapy.cmdline import execute
class ProductSpider(scrapy.Spider):
    name = 'index'
    handle_httpstatus_list = [404]#用于接收404报错
    def start_requests(self):
        start = 245162
        chunk = 100
        print(start + chunk + 1)
        for i in range(start, start + chunk + 1):
            yield scrapy.Request(url='https://ask.csdn.net/questions/'+str(i), method="GET", meta={"qx_id": i})

    def parse(self, response: HtmlResponse):
        try:
            jo = {}
            qxid = response.meta['qx_id']
            jo['qx_id'] = qxid
            if response.text.find('页面找不到了') == -1:
                soup = BeautifulSoup(response.text, 'html.parser')
                jo['money'] = '0'
                if response.text.find('taglist') != -1:
                    taglist = soup.find_all('ul', class_='taglist')[0]
                    mon = taglist.find_all('li', class_='money')
                    if (len(mon) >= 1):
                        jo['money'] = mon[0].find_all('span')[0].text.replace("¥", "")

                jo['num'] = soup.find_all('div', class_='wap-right')[0].find_all('span', class_='issur-time')[0].text.replace(" ", "").replace("\n", "").replace("浏览", "")

                jo['reply'] = '0'
                emn = soup.find_all('em', class_='em1')
                if (len(emn) >= 1):
                    jo['reply'] = emn[0].text  # 评论数

                jo['community'] = '首页'
                lxy = soup.find_all('span', class_='el-breadcrumb__inner')
                if (len(lxy) >= 2):
                    jo['community'] = lxy[1].find_all('a')[0].text.replace(" ", "").replace("\n", "")


                jo['title'] = soup.find_all('h1')[0].text
                jo['name'] = soup.find_all('a', class_='name')[1].text
                jo['renq'] = soup.find_all('span', class_='issur-time')[0].text  # 日期
                jo['blogDetail2'] = soup.find_all('div', class_='md')[0].text  # 内容
            else:
                print(qxid, ' 没有')
            yield jo
        except:
            yield scrapy.Request(url='https://ask.csdn.net/questions/' + str(response.meta['qx_id'])+'?qxno=1', method="GET", meta={"qx_id": response.meta['qx_id']})

# 这个是main函数也是整个程序入口的惯用写法
if __name__ == '__main__':
    execute(['scrapy', 'crawl', 'index'])