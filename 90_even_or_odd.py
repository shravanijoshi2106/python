class Number:
    def __init__(self, num):
        self.num = num

    def check(self):
        if self.num % 2 == 0:
            print(self.num, "is Even")
        else:
            print(self.num, "is Odd")

n1 = Number(10)

n1.check()