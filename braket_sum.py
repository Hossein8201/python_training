# https://quera.org/problemset/221454?tab=description
import math
from decimal import Decimal as d
turn = int(input())
list = []
for i in range(turn):
    number= int(input())
    begin = float(input())
    sum = d(math.floor(begin) * number)
    begin -= math.ceil(begin)
    begin *=-1
    diff = d(begin) * d(number)
    diff = math.ceil(diff)
    amount = number - diff
    if amount>=0:
        sum += amount
    list += [sum]
for i in list:
    print(i)