# Напишите программу, которая принимает 
# две строки вида “a/b” - дробь с числителем
# и знаменателем. Программа должна возвращать 
# сумму и произведение* дробей. Для проверки
# своего кода используйте модуль fractions

import fractions 

# проверка функцией
n_1 = fractions.Fraction(2, 3)
print(n_1)

n_2 = fractions.Fraction(5, 7)
print(n_2)

print(n_1 + n_2)
print(n_1 * n_2)

num_1 = '2/3'
num_2 = '5/7'

num_1 = num_1.split('/')
num_2 = num_2.split('/')
# # print(type(num_1))
# # print(num_2)

for i in range(len(num_1)):
    num_1[i] = int(num_1[i])
# # print(type(num_1))
# # print(num_1)
for i in range(len(num_2)):
    num_2[i] = int(num_2[i])
# # print(num_2)
    

total = (f'{(num_2[1] * num_1[0] + num_1[1] * num_2[0])}/{(num_1[1] * num_2[1])}')
print(total)  # сумма 

production = (f'{(num_1[0] * num_2[0])}/{(num_1[1] * num_2[1])}')
print(production) # произведение
