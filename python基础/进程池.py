#打开num.txt 读取所有行的数，对每个数求平方并输出
import multiprocessing
# "r" 读取 read
# "w" 读取 write
# f = open("num.txt","r")
# print(f.read())
# f.close

# 上下文管理器（作用下代码执行完自动关闭）
with open("class/num.txt","r") as f:
    txt = f.read()
nums = txt.split("\n")      # 以换行符为界读取每个数据并加入列表里
# print(nums)

def work(num):
    num = int(num)      # 将列表强行转换成数字
    out_num = num * num
    print(out_num)

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=10)
    pool.map(work,nums)