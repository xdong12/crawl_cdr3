# -*- coding: utf-8 -*-
import os
from fake_useragent import UserAgent
ua = UserAgent()

####################配置信息################
# 可配置对应的请求头
#TODO
HEADERS = {
    "User-Agent": ua.random,
}




######################################
# 由于win和linux系统对于路径搜索不一致, 需要对split进行修改： Win: \\  Linux: /
BOT_NAME = str(os.path.abspath(__file__).split('/')[-2])

SPIDER_MODULES = ['employment.spiders']
NEWSPIDER_MODULE = 'employment.spiders'

# COMMANDS_MODULE = "commands"

# 输出格式 可手动选择输出格式
ITEM_PIPELINES = {
    # BOT_NAME + '.pipelines.PipelineCsv': 320,
    # BOT_NAME + '.pipelines.PipelineExcel': 340,
    # BOT_NAME + '.pipelines.PipelineMysql': 360,
    BOT_NAME + '.pipelines.PipelineMongodb': 380,
}

DOWNLOADER_MIDDLEWARES = {
    BOT_NAME + '.middlewares.EmploymentDownloaderMiddleware': 550,
}

# 下载超时:
DOWNLOAD_TIMEOUT = 10
# 自动节流器
AUTOTHROTTLE_ENABLED = True
# 延迟下载 防止被ban
DOWNLOAD_DELAY = 0.2

AUTOTHROTTLE_TARGET_CONCURRENCY = 16
# 并发数
CONCURRENT_REQUESTS = 32

# 起始值
AUTOTHROTTLE_START_DELAY = 1
# 上限
AUTOTHROTTLE_MAX_DELAY = 5
# 禁止重试
RETRY_ENABLED = True

# #TODO
# # 禁止cookies:
# COOKIES_ENABLED = False
#
# MEDIA_ALLOW_REDIRECTS = True

# 查看限速参数
AUTOTHROTTLE_DEBUG = True

ROBOTSTXT_OBEY = False

# 是否显示重复请求
DUPEFILTER_DEBUG = True

# 代理ip
# PROXY_IP = "http://http-dyn.abuyun.com:9020"
PROXY_IP = 'http://192.168.1.50:35555/random'
# PROXY_IP = 'http://api.ip.data5u.com/dynamic/get.html?order=364b34f504a96d09d677bed1b3bc6d8a&json=1&random=1&sep=3'


# 阿布云代理隧道验证信息
PROXY_USER = "HU76I061ZS89394D"
PROXY_PASS = "832AF14CA6EA0C82"

# 代理列表
PROXY_LIST = [
]

# ---------- mysql ----------
MYSQL_CONFIG = {
    'host': '192.168.1.50',
    'port': 3306,
    'user': 'root',
    'password': 'zwasljin',
    'database': 'data_collection',
    'charset': 'utf8mb4',
}

# ---------- mongodb ----------
MONGODB_CONFIG = {
    'host': '192.168.1.50', # 192.168.1.50
    'port': 27016 # 27016
}
MONGODB_DB = 'crawlab_test'


# 1(必须). 使用了scrapy_redis的去重组件，在redis数据库里做去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

#  2(必须). 使用了scrapy_redis的调度器，在redis里分配请求
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 3(可选). 在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复，也就是不清理redis queues
SCHEDULER_PERSIST = True

# 4(必须). 通过配置RedisPipeline将item写入key为 spider.name : items 的redis的list中，供后面的分布式处理item 这个已经由 scrapy-redis 实现，不需要我们写代码，直接使用即可
# ITEM_PIPELINES = {
# 　　 'scrapy_redis.pipelines.RedisPipeline': 100 ,
# }
# 5(必须). 指定redis数据库的连接参数
REDIS_HOST = '192.168.1.50'
REDIS_PORT = 26379

# ---------- 斐斐打码 ----------
CODE_CONFIG = {
    "pd_id": "121873",  # 用户中心页可以查询到pd信息
    "pd_key": "J5zpit4Xv+77jpCaL1ilaJfgu64Qpt4L",
    "app_id": "321873",  # 开发者分成用的账号，在开发者中心可以查询到
    "app_key": "jI8tTxXaM7ue+dZqGauiTGLGJI7Ugk2r",
    "pred_type": "30500"  # 识别类型，具体类型可以查看官方网站的价格页选择具体的类型，不清楚类型的，可以咨询客服
}

# 禁止请求重定向
# REDIRECT_ENABLED = False

