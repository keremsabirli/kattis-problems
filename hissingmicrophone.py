x = input()
memory = False
result = "no hiss"
for a in x:
    if result == "hiss": break
    if a == 's':
        if memory == True:
            result = "hiss"
        if memory == False:
            memory = True
    else:
        memory = False
print(result)