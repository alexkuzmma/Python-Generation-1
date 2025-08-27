# Тема урока: цикл for

#1. Последовательность чисел 1
# m = int(input())
# n = int(input())
#
# for i in range(m, n + 1):
#     print(i)

#2 Последовательность чисел 2
m = int(input())
n = int(input())

if m < n:
    for i in range(m, n + 1):
        print(i)
if m > n:
    for i in range(m, n - 1, -1):
        print(i)
if m == n:
    print(m)