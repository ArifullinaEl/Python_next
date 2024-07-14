# Напишите программу, которая получает 
# целое число и возвращает его 
# шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

DIV_SIXTEEN = 16
number = int(input('Введите число: '))
print(hex(number)) # проверка

hex = '0123456789abcdef'
result = ''

while number > 0:
        result =  hex[number % 16] + result
        number //= DIV_SIXTEEN
        # print(number)
        # print(result)
print(result) 
