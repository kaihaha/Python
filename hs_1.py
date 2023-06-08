a = 9
b = 6
def add(a, b):
    return a + b

def sub(a, b):
    if b < 0:
        raise ValueError("不能有负数！")
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("不能被零除！")
    return a / b
print(add(a, b))  # 输出 8
print(sub(a, b))  # 输出 2
print(multi(a, b))  # 输出 15
print(div(a, b))  # 输出 1.6666666666666667