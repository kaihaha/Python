class Phine2013:
    Number = "123456"
    Producer = "HONOR"
    def fourG(self):
        print("4G通信")
    def tianqi(self):
        print("天气晴")
class Phine2023(Phine2013):
    color = "blue"
    Number = "456789"
    Producer = "OPPO"
    def fourG(self):
        print("5G通信")

class Phine2014:
    Number = "123456"
    Producer = "HONOR"
    def fourG(self):
        print("4G通信")
    def tianqi(self):
        print("天气晴")

class Phine2024(Phine2014,Phine2023):
    color = "white"
    Number = "147258"
    Producer = "Voio"
    def fourG(self):
        Phine2023.fourG(self)
        Phine2014.fourG(self)

# phone = Phine2023()
phone = Phine2024()
print(phone.color)
print(phone.Number)
print(phone.Producer)
phone.fourG()