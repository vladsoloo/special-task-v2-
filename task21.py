def count_units_and_tens(n):
    # Проверяем, что n больше 9
    if n <= 9:
        raise ValueError("n должно быть больше 9")

    # Количество единиц (последняя цифра)
    units = n % 10
    
    #  Количество десятков (вторая с конца цифра)
    tens = (n // 10) % 10

    return units, tens

# Пример использования
n = 1234  # Можно изменить это число на любое больше 9
units, tens = count_units_and_tens(n)

print(f"Число {n}:")
print(f"Количество единиц: {units}")
print(f"Количество десятков: {tens}")
