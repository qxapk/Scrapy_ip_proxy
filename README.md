# Scrapy爬虫框架，代理ip，多线程并发，极简demo中文案例

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badge/) [![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)      

最近研究爬虫框架，各种乱七八糟问题，和爬小项目没必要交互

于是研究了一下Scrapy框架，将其简化，删除对爬小项目无用功能文件

代理ip这方面搞得焦头烂额，费好大劲勉强解决能用。


##  优点
精简版，删除无用功能文件，莫名其妙的交互

项目名均为通用昵称例如（index、main），可反复导入只需修改目录名即可
**app\code\index.py**，是主要代码文件
**pipelines.py**，是写出数据的文件
**ip.db**，存储ip的sql文件
**ip.py**，代理ip的配置文件

以下是代理ip对接文件
middlewares.py-->
  class RandomProxyMiddleware(object):-->
     def process_request(self, request, spider):-->
	    request.meta['proxy'] = asa
		这里就是使用代理IP的代码，如果不想使用代理ip
		将代码改成：
		request.meta['proxy'] = None
		


##  技术特性

- [x] **无需通过cmd创建，直接导入**
- [x] **基础配置已搭建完毕，无需重新配置**
- [x] **中文注解**
- [x] **无需命令行，直接运行：main.py**




## 联系

微信公众号：小千哥

回复：**进群**，可免费入群
公众号时常分享前沿黑科技代码、思路，欢迎关注！