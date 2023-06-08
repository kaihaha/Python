# x = float(input("输入一个实验:"))
# y = 1.0
# while y*y != x:
#     y = (y+x/y)/2
#     print(y,y*y)
# print("平方根为：",y)


def sqrt_newton(n):
    """
    使用牛顿迭代法求解平方根
    """
    x = n
    while True:
        y = (x + n / x) / 2
        if abs(y - x) < 1e-6:
            break
        x = y
    return x

if __name__ == '__main__':
    # 读取用户输入的数字
    n = float(input('请输入一个数字: '))
    # 调用牛顿迭代法求解平方根
    sqrt_n = sqrt_newton(n)
    # 输出结果
    print('{0:.6f} 的平方根是 {1:.6f}'.format(n, sqrt_n))