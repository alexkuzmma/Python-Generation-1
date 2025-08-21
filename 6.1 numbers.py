# num_1 = int(input())
# # a = num_1 // 10
# # b = num_1 % 10
# #
# # print(a, b)
# # #print(a + b)
#
# # 3х-зн.
# # a = num_1 // 100
# # b = num_1 % 100 // 10
# # c = num_1 % 10
# # print(f'сумма цифр {a}, {b}, {c} =', a + b + c)
#
# # 4х-зн.
# a = num_1 // 1000
# b = num_1 % 1000 // 100
# c = num_1 % 100 // 10
# d = num_1 % 10
# sum = a + b + c + d
# print(a + b + c + d)
#
# # print(f'сумма цифр {a}, {b}, {c}, {d} =', a + b + c + d)
# found = False
#
# if sum % a == 0:
#     print(f'Сумма цифр {num_1} делится на {a}')
#     found = True
# if sum % b == 0:
#     print(f'Сумма цифр {num_1} делится на {b}')
#     found = True
# if sum % c == 0:
#     print(f'Сумма цифр {num_1} делится на {c}')
#     found = True
# if sum % d == 0:
#     print(f'Сумма цифр {num_1} делится на {d}')
#     found = True
#
# if not found:
#     print(f'Сумма цифр {num_1} не делится на свои цифры.')

# a, b, c = int(input()), int(input()), int(input())
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print('YES')
# else:
#     print('NO')

# a = float(input())
# b = float(input())
# S = a * b / 2
# print(S)

# S = float(input())
# V1 = float(input())
# V2 = float(input())
#
# T = (S / (V1 + V2))
# print(T)

# 3
# a = float(input())
# if a != 0:
#     print(a ** -1)
# else:
#     print('Обратного числа не существует')

# 4
# far = float(input())
#
# cel = 5 / 9 * (far - 32)
# print(cel)

# 5
# n = int(input())
#
# a1 = 10.5
# a2 = 4
#
# if n == 1:
#     print(a1)
# if n == 2:
#     print(a1 * 2)
# if n > 2:
#     ostatok = n - 2
#     res = a1 * 2 + ostatok * a2
#     print(res)

# 6
# a = float(input())
#
# res1 = a * 10
# print(res1)
#
# res2 = res1 % 10
# print(res2)
#
# print(input(res2))

# 7
# a = float(input())
#
# res = a - int(a)
# print(res)

# 8 Наибольшее и наименьшее
# a1, a2, a3, a4, a5 = int(input()), int(input()), int(input()), int(input()), int(input())
#
# minimum = min(a1, a2, a3, a4, a5)
# maximum = max(a1, a2, a3, a4, a5)
#
# print(f'Наименьшее число = {minimum}')
# print(f'Наибольшее число = {maximum}')

# 9 Сортировка трёх
# a1, a2, a3 = int(input()), int(input()), int(input())
#
# min1 = min(a1, a2, a3)
# max1 = max(a1, a2, a3)
# sred = a1 + a2 + a3 - min1 - max1
#
# print(max1)
# print(sred)
# print(min1)

# 10 Интересное число
# a = int(input())
#
# x1 = a // 100
# x2 = a // 10 - x1 * 10
# x3 = a // 1 - x1 * 100 - x2 * 10
#
# min1 = min(x1, x2, x3)
# max1 = max(x1, x2, x3)
# sred = x1 + x2 + x3 - min1 - max1
#
# if max1 - min1 == sred:
#     print('Число интересное')
# else:
#     print('Число неинтересное')

# 11 Абсолютная сумма
# a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())
#
# res = abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5)
# print(res)

# 12 Манхэттенское расстояние
# p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
#
# res = abs(p1 - q1) + abs(p2 - q2)
# print(res)

# End