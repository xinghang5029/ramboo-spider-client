# coding=utf-8
from spider_process.processor import Processor,FieldProcess
from spider_process.download import DownLoad
class Spider(object):



    def __init__(self,download,rule):
        self.download =  download
        self.processor = Processor()
        self.detail_processor = FieldProcess()
        self.rule = rule



    def start(self):
        content = self.download.download()
        if content is not None:
            self.processor.process(content,self.rule)


    def detail_start(self):
        content = self.download.download()
        if content is not None:
            self.detail_processor.process(content,self.rule)


if __name__=="__main__":
    settings = {}
    settings["url"] = "http://www.runoob.com/python/python-dictionary.html"
    settings["timeout"] = 10
    settings["headers"] = None
    settings["cookies"] = None
    settings["proxy"] = None
    download = DownLoad(settings)
    spider = Spider(download,None)
    spider.start()


