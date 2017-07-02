n = int(input())
h = n % 3600 // 60
m = n % 60
print(h, m)