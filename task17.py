def swap_digits(number):

    num_str = str(number)

    if len(num_str) != 3:
        raise ValueError("Число должно быть трехзначным.")

    swapped_str = num_str[0] + num_str[2] + num_str[1]

    swapped_number = int(swapped_str)

    return swapped_number


number = 123
swapped_number = swap_digits(number)
print(f"Число после перестановки: {swapped_number}")
