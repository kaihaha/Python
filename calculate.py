def calculator():
    num1 = float(input("输入第一个数字："))
    num2 = float(input("输入第二个数字："))
    operation = input("输入运算符 (+、-、*、/): ")
    if operation == '+':
        print(num1 + num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        if num2 == 0:
            print("错误：除数为零")
        else:
            print(num1 / num2)
    elif operation == '-':
        if num1 < num2:
            print("错误：负结果")
        else:
            print(num1 - num2)
    else:
        print("无效的运算符")
    continue_calculation = input("是否继续计算？ (y/n): ")
    if continue_calculation.lower() == 'y':
        calculator()
calculator()