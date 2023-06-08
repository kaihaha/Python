class Student():
    # name = None
    # nl = None
    # xb = None
    # zy = None
    def __init__(self,name,nl,xb,zy):
        self.name = name
        self.nl = nl
        self.xb = xb
        self.zy = zy

    def say_hi(self):
        print(f"大家好，我是{self.name}，今年{self.nl},性别{self.xb},我的专业{self.zy}")
ust = Student("zhangwenkai",21,"nan","JY")
# ust.name = "zhangwenkai"
# ust.nl = 21
# ust.xb = "nan"
# ust.zy = "JY"
ust.say_hi()
del ust
# print(ust.name)
# print(ust.nl)
# print(ust.xb)
