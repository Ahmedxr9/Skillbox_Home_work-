# Задача 7. Режем число на части

# Получение четырехзначного числа от пользователя
number = int(input('Введите четырехзначное число: '))

# Извлечение каждой цифры отдельно
thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
units = number % 10

# Вывод результатов
print(f'Тысячи: {thousands}')
print(f'Сотни: {hundreds}')
print(f'Десятки: {tens}')
print(f'Единицы: {units}')
