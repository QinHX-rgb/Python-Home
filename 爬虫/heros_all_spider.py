# -*- coding: utf-8 -*-
"""
Created on 2026-01-18 19:38:46
---------
@summary:
---------
@author: 34716
"""

import feapder


class HerosAllSpider(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://spidertools.cn")

    def parse(self, request, response):
        # 提取网站title
        print(response.xpath("//title/text()").extract_first())
        # 提取网站描述
        print(response.xpath("//meta[@name='description']/@content").extract_first())
        print("网站地址: ", response.url)


if __name__ == "__main__":
    HerosAllSpider().start()