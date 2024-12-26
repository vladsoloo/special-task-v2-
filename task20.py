def process_number(num):
    # Убедимся, что число является четырехзначным
    if len(str(num)) != 4:
        raise ValueError("Число должно быть четырехзначным")

    # a) Число, полученное при прочтении цифр справа налево
    reversed_num = int(str(num)[::-1])
    
    # b) Число, образуемое перестановкой первой и второй, третьей и четвертой цифр
    swapped_first_last = int(str(num)[1] + str(num)[0] + str(num)[3] + str(num)[2])
    
    # c) Число, образуемое перестановкой второй и третьей цифр
    swapped_second_third = int(str(num)[0] + str(num)[2] + str(num)[1] + str(num)[3])
    
    # d1) Число, образуемое перестановкой двух первых и двух последних цифр (выделение цифр)
    first_two_last_two = int(str(num)[2:] + str(num)[:2])
    
    # d2) Число, образуемое перестановкой двух первых и двух последних цифр (без выделения цифр)
    original_str = str(num)
    swapped_first_last_combined = int(original_str[2] + original_str[3] + original_str[0] + original_str[1])

    return {
        "reversed": reversed_num,
        "swapped_first_last": swapped_first_last,
        "swapped_second_third": swapped_second_third,
        "first_two_last_two_with_digits": first_two_last_two,
        "first_two_last_two_without_digits": swapped_first_last_combined
    }

number = 5434
results = process_number(number)

print(f"Оригинальное число: {number}")
print(f"Число, полученное при прочтении справа налево: {results['reversed']}")
print(f"Число после перестановки первой и второй, третьей и четвертой цифр: {results['swapped_first_last']}")
print(f"Число после перестановки второй и третьей цифр: {results['swapped_second_third']}")
print(f"Число после перестановки двух первых и двух последних цифр (выделяя цифры): {results['first_two_last_two_with_digits']}")
print(f"Число после перестановки двух первых и двух последних цифр (без выделения цифр): {results['first_two_last_two_without_digits']}")