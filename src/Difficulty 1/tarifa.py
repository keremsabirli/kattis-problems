# https://open.kattis.com/problems/tarifa
monthly, loopCount = int(input()), int(input())
result = 0
for x in range(loopCount):
    a = int(input())
    if monthly >= a: result += (monthly - a)
    else: result -= (a - monthly)
result += monthly
print(result)