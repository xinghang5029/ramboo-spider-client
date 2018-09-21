# coding=utf-8
from scrapy import cmdline

class SpiderProcess(object):

    def start(self):
        cmdline.execute(r'scrapy crawl ramboo -a start_url=http://shuidi.cn/b-search?key=%E8%8C%B6%E5%8F%B6'.split())

if __name__ == '__main__':

    cmdline.execute(r'scrapy crawl ramboo -a start_url=http://shuidi.cn/b-search?key=%E8%8C%B6%E5%8F%B6'.split())