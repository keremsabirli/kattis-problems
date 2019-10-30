domdict = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 20,
    "T": 10,
    "9": 14,
    "8": 0,
    "7": 0
}
nondomdict = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 2,
    "T": 10,
    "9": 0,
    "8": 0,
    "7": 0
}
def points(suit,li):
    score = 0
    for i in li:
        if(i[1] == suit):
            score += domdict.get(str(i[0]))
        else:
            score += nondomdict.get(str(i[0]))
    return score

inp = input().split()
numberOfHands, suit = int(inp[0]), inp[1]
hands = []
for i in range(numberOfHands*4):
    hands.append(input())

print(points(suit, hands))