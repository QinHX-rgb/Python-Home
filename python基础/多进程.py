import multiprocessing

def work(process_id):
    for i in range(100):
        print(f"当前进程：{process_id},{i}")

#主函数（必须）
if __name__ == "__main__":
    for i in range(1,6):
        p = multiprocessing.Process(target=work,args=(i,))
        p.start()