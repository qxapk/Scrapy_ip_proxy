import logging

import requests
import sqlite3
import os.path
import random
import datetime
import time
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
# 连接数据库
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "ip.db")
#print('db_path：',db_path)
conn = sqlite3.connect(db_path)  # 打开数据库
conn.row_factory = dict_factory
cour = conn.cursor()  # 创建游标
cour.execute('delete from proxy_ip')
conn.commit()


# 爬取西刺网站上的代理ip

def crawler_ips():
    print('刷新了')
    while True:
        payload = {
            'token': '5bc9c411fab73c06447a1f6b104b52e3',
            'num': 200,
            'protocol': 'HTTP',
            'time_avail': 1,
            'result_format': 'JSON',
            'ip_dedup': 1
        }
        r = requests.get('http://api.sgxz.cn:12080/getip', params=payload, timeout=(10, 15))
        if r.text.find('port') != -1 and r.text.find('success') != -1:
            data = r.json()
            if data['state'] == 0:
                for i, f in enumerate(data['data']):
                    cour.execute(r"insert INTO `proxy_ip` (`ip`,`port`) VALUES('"+str(f['ip'])+"','"+str(f['port'])+"')")
                    conn.commit()# 提交数
                r.close()
                break
            else:
                r.close()
                raise Exception('qx_error[crawler_ips]' + r.text)
crawler_ips()
f5 = datetime.datetime.now() + datetime.timedelta(minutes=3)
class Get_ip(object):
    def get_random_ip(self):
        now = datetime.datetime.now()
        global f5
        if str(f5 - now).find('day') != -1:
            print('3分钟了，刷新ip')
            f5 = datetime.datetime.now() + datetime.timedelta(minutes=3)
            cour.execute('delete from proxy_ip')#清空
            conn.commit()
            crawler_ips()

        cour.execute(r'SELECT ip,port from proxy_ip')
        user_cha = cour.fetchall()  # 查
        if (len(user_cha) != 0):
            s = user_cha[random.randint(0, len(user_cha) - 1)]
            return 'http://{0}:{1}'.format(s['ip'], s['port'])
        else:
            crawler_ips()
            return self.get_random_ip()


if __name__ == '__main__':
    crawler_ips()
    get_ip = Get_ip()
    a = get_ip.get_random_ip()