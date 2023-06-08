a=["Hello","Python",1,2,3,'a','b']
a[1]="world"
print("更新后：",a)
print("a[2:4]: ", a[1:4])
print("步长为2",a[::2])
print("检查该列表中是否有数值4: ")
if (4 in a):
    print ("存在")
else:
    print("不存在")
b=["Hello","Python",1,2,3]
b[:2]=[1,2,3],[4,5,6]
print('将第一个和第二个元素更换为列表[1,2,3]和[4,5,6]',b)
b.append(4)
# b.insert(5,4)
print('在列表末尾添加一个元素4:',b)
b.insert(2,[7,8,9])
print('在子列表[4,5,6]后面插入另一个子列表[7,8,9]',b)
b[2][2]=0
print('将子列表[7,8,9]中元素9替换为0',b)