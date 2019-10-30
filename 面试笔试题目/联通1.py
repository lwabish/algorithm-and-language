
import sys


def cal_tax(income):
    tax = 0
    if 3000 < income <= 5000:
        tax = (income-3000)*0.05
    elif 5000 < income <= 20000:
        tax = (income - 5000)*0.1+2000*0.05
    elif income > 20000:
        tax = (income - 20000)*0.15+2000*0.05+15000*0.1
    return '{:.2f}'.format(tax)


for line in sys.stdin:
    a = line.split()[0]
    print(cal_tax(float(a)))
