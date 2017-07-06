a = int(input())
b = int(input())
c = int(input())
if a < b < c:
    print(c)
if b < c < a:
    print(a)
elif a < c < b:
    print(b)
