def hanio(n,a, b, c):
    if n == 1:
        print(f"Move disk 1 from {a} to {c}")
        return
    hanio(n-1, a, c, b)
    print(f"Move disk {n} from {a} to {c}")
    hanio(n-1, b, a, c)

hanio(7, 'A', 'B', 'C')  # 汉诺塔问题的递归解决方案
