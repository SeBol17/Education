n = int(input())
n = n % 10000
a1 = n % 10
a2 = (n / 10) % 10
a3 = (n / 100) % 10
a4 = n / 1000
print((a1 * 10 + a2) - (a4 * 10 + a3) + 1)

# Дано четырехзначное число. Определите, является ли
# его десятичная запись симметричной. Если число симметричное, то выведите 1, иначе выведите любое другое целое число.
# Число может иметь меньше четырех знаков, тогда нужно считать, что его десятичная запись дополняется слева
# незначащими нулями.

# Формат ввода
# Вводится единственное число.
# Формат вывода
# Примеры
# Тест
# 1
# Входные данные:
# 2002
# Вывод
# программы:
# 1
