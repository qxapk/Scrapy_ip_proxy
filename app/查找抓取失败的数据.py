f = open('代理shuju.txt', 'r', encoding='utf-8')
text = str(f.readlines())

start = 245162
chunk = 1000
print(start + chunk + 1)
for i in range(start, start + chunk + 1):
    if text.find(str(i)) == -1:
        print('没找到：',str(i))