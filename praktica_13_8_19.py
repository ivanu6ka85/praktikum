summa_zakaza = 0
cena_bileta_1 = 990
cena_bileta_2 = 1390

try:
    coupons = int(input('Какое количество билетов нужно? Ответ: '))
    if coupons <= 0:
        raise ValueError("Неверное значение")
        print('Неверное значение')
except ValueError as error:
        print(error)
for coupon in range(coupons):
    print('Сколько лет посетителю конференции?')
    age = int(input('Введите возраст: '))
    if age < 18:
        summa_zakaza += 0
    if 18 <= age < 25:
        summa_zakaza += cena_bileta_1
    if 25 <= age:
        summa_zakaza += cena_bileta_2
if coupons > 3 :
        summa_zakaza = summa_zakaza-summa_zakaza*0.1
        print(f'Поздравляем!При заказе более трех билетов, скидка 10%! Итого: {summa_zakaza} рублей')
else:
    print(f'Сумма к оплате: {summa_zakaza} рублей')
