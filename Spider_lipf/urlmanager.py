#coding=utf-8
class UrlManager():
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

# 判断要爬取的url是否在待爬取的url容器中

    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

# 获取待爬取的url并将url从待爬取移到已爬取

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

# 判断是否还有待爬取url
    def have_new_url(self):
        return len(self.new_urls) != 0

# 添加新url到待爬取url集合中
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            if url not in self.new_urls and url not in self.old_urls:
                self.new_urls.add(url)



