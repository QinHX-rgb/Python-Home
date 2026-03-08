import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 SLBrowser/9.0.7.12231 SLBChan/112 SLBVPV/64-bit',
    # 'Accept-Encoding': 'gzip, deflate', 
    # 'Accept': '*/*', 
    # 'Connection': 'keep-alive'
    # ''
    'cookie': """bid=bEJ-YMZhruA; ap_v=0,6.0; _pk_id.100001.4cf6=7a4ee62a90b5bd22.1768484442.; _pk_ses.100001.4cf6=1; __utma=30149280.698324542.1768484442.1768484442.1768484442.1; __utmb=30149280.0.10.1768484442; __utmc=30149280; __utmz=30149280.1768484442.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1350235977.1768484442.1768484442.1768484442.1; __utmb=223695111.0.10.1768484442; __utmc=223695111; __utmz=223695111.1768484442.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"""
}

# type=19&interval_id=100%3A90&action=&start=0&limit=20

params = {
    'type': '19',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20'
}

res = requests.get("https://movie.douban.com/j/chart/top_list?",headers=headers,params=params)

rj = res.json()
all_actors = []
for j in rj:
    all_actors += j['actors']   
print(all_actors)