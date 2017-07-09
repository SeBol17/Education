year = int(input())
if year // 4 == 0 and 0 != year % 100 and year % 400 == 0:
    print("YES")
else:
    print("NO")
