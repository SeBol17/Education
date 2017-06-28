A = int(input())
B = int(input())
N = int(input())
totalCost = (A * 100 + B) * N
totalRub = totalCost // 100
totalCop = totalCost % 100
print(totalRub, totalCop)
