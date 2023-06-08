for i in range(1, 10):
    for j in range(1, i + 1):
        # 在输出数值时，使用"\t"制表符实现对齐
        print(f"{j}*{i}={i*j}\t", end="")
    print("\n")  # 换行