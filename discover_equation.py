# https://quera.org/problemset/602
import math as m
from decimal import Decimal as d

def function1(x,y):
    yr = d(x) - d(m.floor(x))
    if abs(d(yr)-d(y))<= 0.2:
        return 1
    return 0

def function2(x,y):
    yr = d(x)**2 + d(x)
    if abs(d(yr)-d(y))<= 0.2:
        return 1
    return 0

def function3(x,y):
    yr = abs(d(1) - d(x)**3) + d(x)**3
    if abs(d(yr)-d(y))<= 0.2:
        return 1
    return 0

number = int(input())
answer_list = []
for i in range(number):
    list = input().split()
    if(float(list[0]))
    if function1(x,y):
        answer_list += [1]
    if function2(x,y):
        answer_list += [2]
    if function3(x,y):
        answer_list += [3]
for i in range(1,4):
    if answer_list.count(i) == number:
        print(i)
        exit()
print('No ones')