# a, b, c = int(input()), int(input()), int(input())

a = input()
b = input()

if a == 'красный' and b == 'синий' or b == 'красный' and a == 'синий':
    print('фиолетовый')
elif a == 'красный' and b == 'желтый' or b == 'красный' and a == 'желтый':
    print('оранжевый')
elif a == 'синий' and b == 'желтый' or b == 'синий' and a == 'желтый':
    print('зеленый')
elif a == b and (a == 'красный' or a == 'синий' or a == 'желтый') and (b == 'красный' or b == 'синий' or b == 'желтый'):
    print(a)
elif (a != 'красный' and a != 'желтый' and a != 'синий') or (b != 'красный' and b != 'желтый' and b != 'синий'):
    print('ошибка цвета')
