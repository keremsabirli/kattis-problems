whitespaceCount, lowercaseCount, uppercaseCount, symbolCount = 0.0, 0.0, 0.0, 0.0
word = input()
for i in word:
    if i == '_':
        whitespaceCount += 1
    elif str.isupper(i):
        uppercaseCount += 1
    elif str.islower(i):
        lowercaseCount += 1
    else:
        symbolCount += 1
print(whitespaceCount / len(word))
print(lowercaseCount / len(word))
print(uppercaseCount / len(word))
print(symbolCount / len(word))