# coding=utf-8
import urlmanager
import htmldownloader
import html_outputer
import html_parser

class SpiderMain():
    def __init__(self):
        self.urls = urlmanager.UrlManager()
        self.downloader = htmldownloader.HtmlDownloader()
        self.outputer = html_outputer.Html_Outputer()
        self.parser = html_parser.HtmlParser()

    def Craw(self,root_url):
        count=1
        # 将入口url添加进url管理器
        self.urls.add_new_url(root_url)
        # 启动爬虫循环
        while self.urls.have_new_url():
            # 获取待爬取的url
            new_url=self.urls.get_new_url()
            print ('craw %d:%s'%(count,new_url))
            # 发送请求，获取返回的HTML文件
            html_cont=self.downloader.download(new_url)

            # 解析返回的HTML文件获取新的url集合和要输出的data
            # print html_cont
            new_urls,new_data=self.parser.parser(new_url,html_cont)

            # 将解析出的url集合添加到待爬取集合中
            self.urls.add_new_urls(new_urls)

            #收集数据
            self.outputer.collect_data(new_data)

            if count==1000:
                break
            count += 1
        self.outputer.output_html()

if __name__=="__main__":
    #爬虫入口url
    root_url="https://baike.baidu.com/item/Python"
    obj_spider=SpiderMain()
    #启动爬虫
    obj_spider.Craw(root_url)