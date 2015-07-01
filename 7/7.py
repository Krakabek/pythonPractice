__author__ = 'Danil Radkovsky'

import random
import math

i = 0
i6 = 0.0
p = 2/6.0
while 1:
    i += 1
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    if num1 == 6:
        i6 += 1
    if num2 == 6:
        i6 += 1
    pe = i6/i
    if math.fabs(p-pe) < 0.0001:
        break

print(i)