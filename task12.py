number = int(input("введите трехзначнное число: "))
sto = number // 100
des = (number // 10)%10
ed = number % 10
sum = sto + des + ed
print(f'число едениц = {ed}, число десятков = {des}, а сумма равна = {sum}')
