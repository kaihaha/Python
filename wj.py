f = open('文件.txt','x')
f1 = open('文件.txt','r')
f2 = open('文件.txt','w')
f2.close()

f3 = open('文件.txt','rb')
print(type(f))
print(type(f3))

print(f.name)
print(f.mode)
print(f.encoding)
print(f.read())
f.write('dfsdfsdfsdfsdfsdfsd')
print(f.readlines())
print(f.tell())
f.rename('','')# 文件重命名
f.remove('')# 文件删除
f.close()

