__author__ = 'Danil Radkovsky'

import random
import math

balance = 10
i = 0
i9 = 0.0
while math.fabs(balance) < 1000:
    i += 1
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)
    num4 = random.randint(1, 6)
    if num1 + num2 + num3 + num4 < 9:
        balance += 10
        i9 += 1
    else:
        balance -= 1

print("Your balance is %d" %balance)
if balance >= 100:
    print("Such a nice game")
else:
    print("Your wife will kill you!")

print("Your chances to win were %.4f" % (i9/i))
print("You need to take %.2f as a win reward to get profit" % (i/i9))