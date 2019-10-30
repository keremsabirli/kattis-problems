# https://open.kattis.com/problems/lastfactorialdigit
elementCount = int(input())
result = 0
for x in range(elementCount):
    a = int(input())
    if a >= 5: result = 0
    elif a == 0 or a == 1: result = 1
    elif a == 2: result = 2
    elif a == 3: result = 6
    elif a == 4: result = 4
    print(result)