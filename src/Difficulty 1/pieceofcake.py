# https://open.kattis.com/problems/pieceofcake2
def cake(li):
    if li[0]/2 >= li[1]:
        if li[0]/2 >= li[2]:
            return ((li[0]- li[1]) * (li[0] - li[2])) * 4
        else:
            return ((li[0]- li[1]) * li[2]) * 4
    else:
        if li[0]/2 >= li[2]:
            return (li[1] * (li[0] - li[2])) * 4
        else:
            return li[1] * li[2] * 4

a = list(map(int ,input().split()))
print(cake(a))