# Модуль math

# from math import sqrt
#
# n1 = sqrt(25)
# print(n1)

# import math
#
# n2 = math.sqrt(85)
# print(round(n2, 2))

# pi = math.pi
# e = math.e
#
# print(pi)
# print(e)

# 1 Евклидово расстояние
# import math
#
# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
#
# pre = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
# p = math.sqrt(pre)
#
# print(p)

# 2 Площадь и длина
import math

R = float(input())
S = math.pi * R ** 2
C = 2 * math.pi * R

print(S)
print(C)

# 3 Средние значения
# import math
#
# a = float(input())
# b = float(input())
#
# cr_a = (a + b) / 2
# cr_geo = math.sqrt(a * b)
# cr_garm = 2 * a * b / (a + b)
# cr_qvad = math.sqrt((a ** 2 + b ** 2) / 2)
#
# print(cr_a)
# print(cr_geo)
# print(cr_garm)
# print(cr_qvad)

# 4 Тригонометрическое выражение
# import math
#
# x = float(input())
#
# r = math.radians(x)
# tr = math.sin(r) + math.cos(r) + math.tan(r) * math.tan(r)
# print(tr)

# 5 Пол и потолок
# import math
# x = float(input())
#
# p = math.ceil(x) + math.floor(x)
#
# print(p)

# 6 Квадратное уравнение
# import math
#
# a, b, c = float(input()), float(input()), float(input())
#
# D = b ** 2 - 4 * a * c
# print(f'D = {D}')
#
# if D < 0:
#     print('Нет корней')
# if D == 0:
#     x = -(b / (2 * a))
#     print(x)
# if D > 0:
#     x1 = (-b - D ** 0.5) / (2 * a)
#     x2 = (-b + D ** 0.5) / (2 * a)
#     print(min(x1, x2))
#     print(max(x1, x2))

# 7 Правильный многоугольник
# import math
#
# n, a = float(input()), float(input())
#
# S = (n * a ** 2) / (4 * (math.tan(math.pi / n)))
# print(S)

# End