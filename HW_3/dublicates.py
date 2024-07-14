# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

reestr = [1, 1, 1, 1, 1, 2, 2, 2, 4, 4, 4, 5]
print(reestr)

# создание частотного словаря
# ключ - элемент списка
# значение - сколько раз в списке
result = {}
for i in reestr:
    if i not in result:
        result[i] = reestr.count(i)
print(result)

# создание списка из ключей по условию value
keys = []
for key in result:
    if result[key] > 1:
        keys.append(key) 
print(f'{keys = }')

# чуть более красиво и короче?
# keys = [key for key in result if result[key] > 1]
# print(keys)

# просто на заметку для себя
# keys = list(res.keys()) # список из keys
# print(keys)
