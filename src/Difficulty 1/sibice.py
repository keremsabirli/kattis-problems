# https://open.kattis.com/problems/sibice
import math
inp = list(map(int,input().split()))
elementCount, w, h = inp[0], inp[1], inp[2]
space = math.sqrt(w*w + h*h)
for i in range(elementCount):
    if space >= int(input()):
        print("DA")
    else:
        print("NE")