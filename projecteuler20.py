#https://projecteuler.net/problem=20
from functions import factorial

fac = str(factorial(100))

def sumDigitsInStr(n):
    top = 0
    for digit in n:
        top += int(digit)
    return top

print(sumDigitsInStr(fac)) #648

