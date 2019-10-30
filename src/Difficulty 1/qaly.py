# https://open.kattis.com/problems/qaly
elementCount = int(input())
qaly = 0.000
for i in range(elementCount):
    period = input().split()
    qaly += (float(period[0]) * float(period[1]))
print(qaly)