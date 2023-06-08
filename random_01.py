# random是Python内置的随机数模块，提供了各种生成随机数和随机序列的函数。下面列出了random库中常用的一些函数：
# random.random()：生成一个[0,1)之间的随机浮点数。
# random.uniform(a, b)：生成一个区间[a,b]之间的随机浮点数。
# random.randint(a, b)：生成一个区间[a,b]之间的随机整数。
# random.choice(seq)：从序列seq中随机选择一个元素。
# random.shuffle(seq)：将序列seq中的元素随机打乱。
# random.sample(population, k)：从种群population中随机选择k个元素。
import random
random.seed(10)
a = random.random()
random.seed(10)
b = random.random()
print(a)
print(b)

from random import * 
count = 0
for i in range(100000):
    num1 = randint(1,6)
    num2 = randint(1,6)
    if num1+num2 == 7:
        count += 1
print(count/100000)