for m in range(1,4+1):
    for i in range(1,m+1):
        print("*",end='')
    print()
for m in range(1,4+1):
    for i in range(1,5-m+1):
        print("*",end='')
    print()

# num = int(input("请输入菱形边长(奇数): "))
# for i in range(num//2+1):
#     for j in range(num//2-i):
#         print(" ", end="")
#     for k in range(2*i+1):
#         print("*", end="")
#     print()
# # 打印下半部分
# for i in range(num//2):
#     for j in range(i+1):
#         print(" ", end="")
#     for k in range(num-2*i-2):
#         print("*", end="")
#     print()