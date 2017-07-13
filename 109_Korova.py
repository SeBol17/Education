n = int(input())
if 5 <= n % 10 <= 9 or n % 10 == 0 or 11 <= n % 100 <= 19:
    print(n, 'korov')
elif 2 <= n % 10 <= 4:
    print(n, 'korovy')
elif n % 10 == 1:
    print(n, "korova")
