# Задача 3. Следующее и предыдущее числа

# Получение числа от пользователя
number = int(input('Введите число: '))

# Вычисление следующего и предыдущего чисел
next_number = number + 1
previous_number = number - 1

# Вывод результата
print(f'После числа {number} идет число {next_number}')
print(f'До числа {number} идет число {previous_number}')
