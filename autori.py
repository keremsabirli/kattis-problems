# https://open.kattis.com/problems/autori
x = input()
x = x.split("-")
result = ""
for a in x:
    result += a[0]
print(result)