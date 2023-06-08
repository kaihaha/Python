class Phine:
    Number = "123456"
    Producer = "HONOR"
    __current_voltage = 0.3

    def tianqi(self):
        print("天气晴")

    def weather(self):
        if self.__current_voltage<0.5:
            print("不能使用")
        else:
            print("天气晴")

User = Phine()
print(User.Number)
User.weather()
User.tianqi()