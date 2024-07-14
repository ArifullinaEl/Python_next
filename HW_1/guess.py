# Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” 
# или “меньше” после каждой попытки. 
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

offer = 10

print('Программа загадала число, отгадайте его')
print(f'У вас будет {offer} попыток')

num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(num)

while offer > 0:
    offer -=1
    user_number = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
    if user_number < LOWER_LIMIT or user_number > UPPER_LIMIT:
        print(f'Вы ввели неверное число, попробуйте еще раз, у вас осталось {offer} попыток')
    elif user_number > num:
        print(f'Загаданное число меньше, попробуйте еще раз, у вас осталось {offer} попыток')
    elif user_number < num:
        print(f'Загаданное число больше, попробуйте еще раз, у вас осталось {offer} попыток')
    else:
        print(f'Вы угадали!')
        break
else:
    print('Попыток больше нет')
    quit()
