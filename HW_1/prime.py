# # Напишите код, который запрашивает число 
# и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: 
# “Число является простым, если делится нацело только 
# на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел 
# и чисел больше 100 тысяч.

MIN_LIMIT = 0
MAX_LIMIT = 100000

while True:
    number = int(input(f'Введите число от {MIN_LIMIT} до {MAX_LIMIT}: '))
    if number < MIN_LIMIT or number > MAX_LIMIT:
        print('Вы ввели неверное число, попробуйте еще раз')
    elif number == 0:
        print(f'Вы ввели {number}, {number} не является ни простым, ни составным числом, попробуйте еще раз') 
    elif number == 1:
        print(f'Вы ввели {number}, {number} не является ни простым, ни составным числом, попробуйте еще раз')
    else:
        break
 
count = 0
for i in range(2, number // 2+1):
    if (number % i == 0):
        count += 1
if (count <= 0):
    print(f'Число {number} простое')
else:
    print(f'Число {number} составное')