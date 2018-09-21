# coding=utf-8
from util.constant import Constant
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests,traceback
from urllib import request

class DownLoad(object):

    def __init__(self,settings,type=Constant.DOWNLOAD_REQUEST_TYPE):
        self.url = settings["url"]
        self.proxy = settings["proxy"]
        self.headers = settings["headers"]
        self.cookies = settings["cookies"]
        self.timeout = settings["timeout"]
        self.type = type





    def request_download(self):
        """
        requests方式下载页面
        :return:
        """
        try:
            resp = requests.get(self.url, headers=self.headers, cookies=self.cookies, timeout=self.timeout, proxies=self.proxy)
            return resp
        except Exception as a:
            print(traceback.format_exc())
            print("下载失败：{}".format(self.url))
            return None

        # try:
        #     response=request.urlopen(self.url)
        #     page = response.read()
        #     page = page.decode('utf-8')
        #     return page
        # except:
        #     return None


    def selenium_download(self):
        """
        动态渲染方式下载页面
        :return:
        """
        try:
            # dcap = dict(DesiredCapabilities.PHANTOMJS)  #设置userAgent
            # dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
            # driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe',desired_capabilities=dcap) #加载网址
            driver = webdriver.Chrome(r'C:\Users\Ramboo\Downloads\chromedriver\chromedriver.exe')
            driver.get(self.url)
            return driver.page_source
        except Exception as a:
            print(traceback.format_exc())
        finally:
            driver.quit()


    def download(self):
        if self.type == Constant.DOWNLOAD_REQUEST_TYPE:
            return self.request_download()
        else:
            return self.selenium_download()


if __name__=="__main__":
    settings = {}
    settings["url"] = "http://www.runoob.com/python/python-dictionary.html"
    settings["timeout"]=10
    settings["headers"]=None
    settings["cookies"]=None
    settings["proxy"]=None
    down = DownLoad(settings)


