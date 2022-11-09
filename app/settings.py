BOT_NAME = 'index'

SPIDER_MODULES = ['app.code']
NEWSPIDER_MODULE = 'app.code'
# 爬取的默认User-Agent，除非被覆盖。
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'

# 是否遵循robots协议，一般不要遵循设为False即可，robots.txt
ROBOTSTXT_OBEY = False


# 下载器最大并发数，默认16个
CONCURRENT_REQUESTS = 300

#每个域名最大并发，默认8
CONCURRENT_REQUESTS_PER_DOMAIN = 300

#每个IP的并发量设置为1，避免同一个IP并发请求网站
#CONCURRENT_REQUESTS_PER_IP = 1


#每个IP的请求间隔，设置为3秒，这个间隔要自己测一下，有些网站，比如百度，是30秒
#DOWNLOAD_DELAY = 3








DOWNLOADER_MIDDLEWARES = {
   'app.middlewares.process_request': 541
}

# 设置管道优先级
ITEM_PIPELINES = {
   'app.pipelines.Pipeline': 300,
}
HTTPERROR_ALLOWED_CODES = [403]

#最大重试次数
RETRY_TIMES = 3000000





""" 启用限速设置 """
DOWNLOADER_MIDDLEWARES = {
    #'app.middlewares.DemoDownloaderMiddleware': 543,
    'app.middlewares.RandomProxyMiddleware': 542
}

#下载延迟
#实际是一个范围随机值： 0.5倍-1.5倍 单位秒DOWNLOAD_DELAY = 3
#若不设置随机值，设置如下：RANDOMIZE_DOWNLOAD_DELAY = False
#DOWNLOAD_DELAY = 3



# 每个域名最大并发数，默认8个
#CONCURRENT_REQUESTS_PER_DOMAIN = 100


#每个ip的最大并发数，默认0，代表没有限制
#CONCURRENT_REQUESTS_PER_IP = 100



# 是否禁用cookies
# 禁用后速度会快些，但可能会反爬，视情况而定COOKIES_ENABLED = False #禁用cookies
#COOKIES_ENABLED = False



# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

#默认请求头
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
}




# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xmeta.middlewares.XmetaSpiderMiddleware': 543,
#}


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'