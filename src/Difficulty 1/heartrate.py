# https://open.kattis.com/problems/heartrate
elementCount = int(input())
q = []
for a in range(elementCount):
    q = input().split()
    minimum, estimated, maximum = (float(q[0])-1) * 60.0000 / float(q[1]), float(q[0]) * 60.0000 / float(q[1]), (float(q[0])+1) * 60.0000 / float(q[1])
    print(f"{minimum} {estimated} {maximum}")