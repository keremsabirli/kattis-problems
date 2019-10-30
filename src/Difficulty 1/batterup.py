# https://open.kattis.com/problems/batterup
elementCount, result = int(input()), 0
numbers = input().split()
for x in numbers:
    if int(x) == -1:
        elementCount -= 1
        continue
    else:
        result += int(x)
print(result / elementCount)