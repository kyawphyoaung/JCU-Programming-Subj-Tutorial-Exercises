import random

pickCount = int(input("How many quick picks? "))

for i in range(pickCount):
    lottery_num1 = random.randint(1, 10) + random.randint(1, 7)
    lottery_num2 = lottery_num1 + random.randint(1, 7)
    lottery_num3 = lottery_num2 + random.randint(1, 7)
    lottery_num4 = lottery_num3 + random.randint(1, 7)
    lottery_num5 = lottery_num4 + random.randint(1, 7)
    lottery_num6 = lottery_num5 + random.randint(1, 7)
    print("{:3}{:3}{:3}{:3}{:3}{:3}".format(lottery_num1, lottery_num2, lottery_num3, lottery_num4, lottery_num5, lottery_num6))