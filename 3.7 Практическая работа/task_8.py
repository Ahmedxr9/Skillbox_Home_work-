# Задача 8. Поменять местами: не всё так просто! (необязательная, повышенной сложности)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)

# Меняем значения местами без использования третьей переменной
a = a + b
b = a - b
a = a - b

print(a, b)
