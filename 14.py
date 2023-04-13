# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите N: "))
i = 0
# result = 0
# while (result <= n):
#     result = 2**i
#     if (result <= n):
#         print(result)
#         i += 1

while (2**i <= n):
    print(2**i)
    i += 1
