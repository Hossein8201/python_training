# https://quera.org/problemset/304?tab=description
from decimal import Decimal as d
import math

def mypow(base,exp):
    if(exp==0):
        return d(1)
    else:
        return d(base)*mypow(base,exp-1)

base = d(float(input()))
exp = d(int(input()))
#print("%.3f" % d(mypow(base,exp)))
print("%.3f" % d(pow(base,exp)))