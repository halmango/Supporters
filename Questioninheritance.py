class Calculator:
    def __init__ (self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        num3 = num2 + 2
        print(f"{num1} + {num2} + {num3} = {num1 + num2 + num3}")
Calculator(int(input("숫자 1을 입력해주세요: ")), int(input("숫자 2을 입력해주세요: ")))