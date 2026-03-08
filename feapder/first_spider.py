# -*- coding: utf-8 -*-
"""
Created on 2026-01-17 19:42:00
---------
@summary:
---------
@author: 34716
"""

import feapder


class FirstSpider(feapder.AirSpider):
    def start_requests(self):
        # 发送请求
        for i in range(5):
            start = i * 25 # 每页25条数据
            url = f"https://www.douban.com/group/117205/discussion?start={start}&type=new"
            yield feapder.Request(url)

    def download_midware(self, request):
        # 下载中间件，可以在这里添加请求头、代理等
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "priority": "u=0, i",
            "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 SLBrowser/9.0.7.12231 SLBChan/112 SLBVPV/64-bit"
            }
        cookies = {
            "bid": "bEJ-YMZhruA",
            "__utmz": "30149280.1768484442.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
            "ap_v": "0,6.0",
            "_pk_id.100001.8cb4": "7fac8f11bf4d7b22.1768551492.",
            "_pk_ses.100001.8cb4": "1",
            "ct": "y",
            "__utma": "30149280.698324542.1768484442.1768484442.1768551493.2",
            "__utmt": "1",
            "dbcl2": "\"293188927:nXbyCwG9vqQ\"",
            "push_noty_num": "0",
            "push_doumail_num": "0",
            "__utmv": "30149280.29318",
            "__yadk_uid": "94xOKuWWuSFQquDrILCiv6BVnAx9zc2w",
            "ck": "ACYg",
            "__utmc": "30149280",
            "__utmb": "30149280.35.2.1768551809742"
        }
        request.headers = headers
        request.cookies = cookies
        return request

    def parse(self, request, response):
        # 解析响应
        # 提取网站title
        print(response)
        soup = response.bs4()
        olt = soup.find("table",class_="olt")
        trs = olt.find_all("tr")
        del trs[0]  # 删除表头
        for tr in trs:
            tds = tr.find_all("td")
            info = {
                "内容": tds[0].text.strip(),
                "作者": tds[1].text.strip(),
                "回复/查看": tds[2].text,
                "最后回复时间": tds[3].text,
            }
            print(info)

        # # 提取网站描述
        # print(response.xpath("//meta[@name='description']/@content").extract_first())
        # print("网站地址: ", response.url)


if __name__ == "__main__":
    FirstSpider().start()