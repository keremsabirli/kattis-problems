# https://open.kattis.com/problems/dicecup
def most_accuring(li):
    results = []
    accureCounts = []
    for x in range(int(dices[0])):
        for y in range(int(dices[1])):
            results.append(x + y)
    for i in range(max(results) + 1):
        accureCounts.append(0)
    for i in results:
        accureCounts[int(i)] += 1
    maxValue = 0
    maxIndexes = []
    maxValue = max(accureCounts)
    for i in range(len(accureCounts)):
        if accureCounts[i] == maxValue:
            maxIndexes.append(i + 2)
    return maxIndexes

dices = input().split()
for i in most_accuring(dices):
    print(i)