import requests
import jsonpath
from fake_useragent import UserAgent
import time
import random

# ====================== 【需要你手动修改的3个配置项】 ======================
item_id = "699999999999"  # 替换成你要爬取的商品ID
cookie_str = "你的淘宝cookie内容粘贴到这里"  # 替换成你复制的cookie
page_num = 5  # 要爬取的评论页数，建议先爬1-5页测试，不要爬太多！
# ==========================================================================

# 随机请求头，模拟真实浏览器，降低反爬概率
ua = UserAgent()
headers = {
    "user-agent": ua.random,
    "cookie": cookie_str,
    "referer": f"https://item.taobao.com/item.htm?id={item_id}",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"
}

# 存储所有评论
all_comments = []

def crawl_taobao_comment():
    """爬取淘宝商品评论核心函数"""
    for page in range(1, page_num + 1):
        # 淘宝评论的真实请求接口（亲测有效）
        url = f"https://rate.taobao.com/feedRateList.htm?" \
              f"auctionNumId={item_id}" \
              f"&currentPageNum={page}" \
              f"&pageSize=20" \
              f"&rateType=0" \
              f"&orderType=sort_weight" \
              f"&hasSku=false" \
              f"&folded=0"

        try:
            # 发送请求，禁止重定向
            response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
            # 处理响应：淘宝返回的是jsonp格式，需要去掉前后的回调函数，转成纯json
            json_data = response.text.replace('jsonp_tbcrate_reviews_list(', '').replace(');', '')
            data = eval(json_data)  # 转为字典

            # 解析评论数据
            comments = jsonpath.jsonpath(data, '$..comments')
            if not comments or len(comments[0]) == 0:
                print(f"第{page}页：无评论数据，爬取结束")
                break

            # 提取每条评论的核心信息
            for comment in comments[0]:
                comment_info = {
                    "用户昵称": comment.get("nick", "匿名用户"),
                    "评论内容": comment.get("content", "无内容"),
                    "购买商品规格": comment.get("auctionSku", "未填写规格"),
                    "评论时间": comment.get("date", "未知时间"),
                    "点赞数": comment.get("usefulVoteCount", 0)
                }
                all_comments.append(comment_info)

            print(f"第{page}页评论爬取成功，共获取{len(comments[0])}条评论")

            # 核心防封：随机休眠2-5秒，模拟人类操作，切勿删除！
            time.sleep(random.uniform(2, 5))

        except Exception as e:
            print(f"第{page}页爬取失败，错误信息：{str(e)}")
            # 失败后休眠更长时间，避免被风控
            time.sleep(random.uniform(5, 8))
            continue

    # 爬取完成后，打印所有评论
    print("\n===== 爬取结果汇总 =====")
    print(f"共爬取到 {len(all_comments)} 条有效评论")
    for idx, com in enumerate(all_comments, 1):
        print(f"\n【{idx}】{com}")

if __name__ == '__main__':
    print("开始爬取淘宝商品评论...")
    crawl_taobao_comment()