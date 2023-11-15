# Задача 6. Проверяем бухгалтера

# Получение двух чисел от пользователя
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

# Получение двух последних цифр каждого числа
last_two_digits_first = first_number % 100
last_two_digits_second = second_number % 100

# Сложение полученных двух чисел
sum_last_two_digits = last_two_digits_first + last_two_digits_second

# Вывод результата
print(f'Сумма двух последних цифр: {sum_last_two_digits}')
