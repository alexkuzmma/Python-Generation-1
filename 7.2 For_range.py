# Тема урока: цикл for

#1. Последовательность чисел 1
# m = int(input())
# n = int(input())
#
# for i in range(m, n + 1):
#     print(i)

#2 Последовательность чисел 2
# m = int(input())
# n = int(input())
#
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# if m > n:
#     for i in range(m, n - 1, -1):
#         print(i)
# if m == n:
#     print(m)

#3 Последовательность чисел 3
m = int(input())
n = int(input())

if m % 2 == 0:
    if m - 1 == n and m % 2 == 0:
        print(n)
    if m - 1 == n and n % 2 == 0:
        print(m)
if m % 2 == 0 and m - 1 != n:
    for i in range(m - 1, n, -2):
        print(i)
if m % 2 != 0 and n % 2 != 0:
    for i in range(m, n - 1, -2):
        print(i)
if m % 2 != 0 and n % 2 == 0:
    for i in range(m, n, -2):
        print(i)