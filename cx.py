class Parent01:
    def myMethod(self):
        print('调用父类方法')
class Parent02:
    def myMethod(self):
        print('调用父类方法')
class Child(Parent01,Parent02):
    def myMethod(self):
        print('调用子类方法')
c = Child()
c.myMethod()
super(Child,c).myMethod()