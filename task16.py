digits = list(map(int, str(int(input("Введите трехзначное число: "))))) 
digits[0], digits[1] = digits[1], digits[0] 
print("Число после перестановки:", int("".join(map(str, digits))))
