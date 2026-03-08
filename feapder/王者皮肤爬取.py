import requests
from bs4 import BeautifulSoup

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
    "RK": "h93RwWsf8m",
    "ptcz": "ee4fe9a0da4db6989bbb6a63bc20793a15579ce43dcb6f9c35c65117580b6c52",
    "pac_uid": "0_0kkmXssEWbmAr",
    "_qimei_uuid42": "1940700081a100b3c843ac3c8b22694fd3b0d01295",
    "_qimei_fingerprint": "4c836a2489a1a3078bd8ea87e4c29ea8",
    "_qimei_h38": "2db80e8cc843ac3c8b22694f02000007d19407",
    "_qimei_q32": "a73475431d2f2b86c2c80df95c3a8469",
    "_qimei_q36": "29705f94d49789cf01b8500830001f418819",
    "isHostDate": "20470",
    "PTTuserFirstTime": "1768608000000",
    "isOsSysDate": "20470",
    "PTTosSysFirstTime": "1768608000000",
    "isOsDate": "20470",
    "PTTosFirstTime": "1768608000000",
    "pgv_info": "ssid=s5246083056",
    "ts_last": "pvp.qq.com/web201605/herolist.shtml",
    "pgv_pvid": "1865499090",
    "ts_uid": "8357119240",
    "weekloop": "0-0-0-3",
    "eas_sid": "k1H7C6y8B6M572T331T777L0D5",
    "pvpqqcomrouteLine": "herolist_herolist",
    "PTTDate": "1768652407794"
}
url = "https://pvp.qq.com/web201605/herolist.shtml"
response = requests.get(url, headers=headers, cookies=cookies)

soup = BeautifulSoup(response.content.decode("gbk"),'html.parser')
ul = soup.find("ul",class_="herolist")
lis = ul.find_all("li")
for li in lis:
    name = li.text
    abs_url = "http:" + li.a.img['src']
    img_res = requests.get(abs_url, headers=headers, cookies=cookies)
    with open(f"{name}.png","wb") as f:
        f.write(img_res.content)    
        