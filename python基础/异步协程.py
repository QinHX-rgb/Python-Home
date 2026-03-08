import asyncio
# 延时

async def work1():  # 异步函数
    await asyncio.sleep(10)     # 延时10秒钟
    print("服务员，我要点青椒肉丝")

async def work2():  # 异步函数
    print("服务员，我要点土豆肉丝")

async def main():
    works = [work1(),work2()]
    await asyncio.gather(*works)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()