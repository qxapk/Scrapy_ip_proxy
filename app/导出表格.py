import json
import xlsxwriter
import datetime
def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True
def kw_zhuan(a):
    if a.find('k') != -1:
        a = str(float(a.replace("k", ""))*1000)
        return a
    if a.find('w') != -1:
        a = str(float(a.replace("w", ""))*10000)
        return a
    return a

if __name__ == '__main__':
    qxtime = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    btou = ['id', '赏金','文章阅览量', '文章评论数', '社区名', '文章标题', '文章作者名', '文章发布时间', '文章内容']  # 表头
    k = xlsxwriter.Workbook(r'C:\Users\aabb\Desktop\csdn_问答1_' + qxtime + '.xlsx', {'strings_to_urls': False, 'constant_memory': True})
    # 为显式钱的单元格添加数字格式
    format_money = k.add_format({'num_format': '#,##0'}).set_num_format('0.00')  # 格式化数据格式为小数点后两位
    # 添加 Excel 日期格式
    format_date = k.add_format({'num_format': 'yyyy-mm-dd hh:mm:ss'})


    b = k.add_worksheet("表格")  # 创建工作表
    f = 0  # 表头
    b.write(f, 0, btou[0])
    b.write(f, 1, btou[1])
    b.write(f, 2, btou[2])
    b.write(f, 3, btou[3])
    b.write(f, 4, btou[4])
    b.write(f, 5, btou[5])
    b.write(f, 6, btou[6])
    b.write(f, 7, btou[7])
    b.write(f, 8, btou[8])

    fx = open("shuju.txt", 'r', encoding='utf-8')  # 返回一个文件对象
    a = fx.readline()
    while a:
        if (is_json(a) == True):
            obj = json.loads(a)
            if 'money' in obj:#json_判断key存在则
                qx_id = obj['qx_id']
                money = obj['money']
                num = obj['num']
                num = kw_zhuan(num)

                reply = obj['reply']
                community = obj['community']
                title = obj['title']
                name = obj['name']
                renq = obj['renq']
                blogDetail2 = obj['blogDetail2']


                f = f + 1
                b.write(f, 0, qx_id)
                b.write_number(f, 1, float(money), format_money)
                b.write_number(f, 2, float(num), format_money)
                b.write_number(f, 3, float(reply), format_money)
                b.write(f, 4, community)
                b.write(f, 5, title)
                b.write(f, 6, name)
                b.write(f, 7, renq)
                b.write_datetime(f, 7, datetime.datetime.strptime(renq, "%Y-%m-%d %H:%M"), format_date)
                b.write(f, 8, blogDetail2)
        else:
            print('不是json：',a)

        a = fx.readline()
    fx.close()
    print('开始close()')
    k.close()
    print('结束k.close()')