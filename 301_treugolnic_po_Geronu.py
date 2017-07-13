a = float(input())
b = float(input())
c = float(input())
p = int((a + b + c) / 2)
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print('{}'.format(s))
