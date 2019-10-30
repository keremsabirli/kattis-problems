testCount = int(input())
for i in range(testCount):
    uniqueplaces = []
    placeCount = int(input())
    for j in range(placeCount):
        place = input()
        if place not in uniqueplaces:
            uniqueplaces.append(place)
    print(len(uniqueplaces))