import threading

def work(t_id):
    for i in range(100):
        print(f"当前线程：{t_id},{i}")


if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=work,args=(i,))
        t.start()