# Задача 5. Часы

# Получение количества минут от пользователя
total_minutes = int(input('Введите количество минут: '))

# Вычисление часов и оставшихся минут
hours = total_minutes // 60
remaining_minutes = total_minutes % 60

# Вывод результата
print(f'{total_minutes} минут - это {hours} часов и {remaining_minutes} минут.')
