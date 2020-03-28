from homework4.homework4 import only_alphabet

#5.1 Создайте список 2 в степени N, где N от 0 до 20.
rez = [2**n for n in range(0, 20)]
print(rez)

#5.2 У вас есть список целых чисел. Создайте новый список остатков от деления на 3 чисел из исходного списка.
rez = [0, 1, 3, 5, 6, 8, 9, 10, 11]
new_rez = [n % 3 for n in rez]
print(new_rez)

#5.3 У вас есть список, в котором могут быть разные типы данных. Создайте новый список только чисел из этого списка.
l =[1, "2", "string some", True, "asaa", "123some text!!! 12", "Hello! what???", 4.67, ["fff", 56]]
l = [x for x in l if (type(x) == int or type(x) == float)]
print(l)

# 5.4 У вас есть список, в котором могут быть разные типы данных. Создайте новый список только строк, при этом удалите
# усе небуквенные символы из них. Воспользуйтесь функцией из предыдущего задания
# (импортируйте её из другого своего файла)

l_in = [1, "2", "string some", True, "asaa", "123some text!!! 12", "Hello! what???"]
l_out = [''.join(x for x in string if x.isalpha()) for string in l_in if type(string) == str]
print(l_out)

#second variant
l_in = [1, "2", "string some", True, "asaa", "123some text!!! 12", "Hello! what???"]
l_out1 = [x for x in [only_alphabet(string) for string in l_in if type(string) == str] if x != '']
print(l_out1)

#У вас есть словарь – характеристик человека. Ключи например: “name”, “surname”, “age”, “position”, “address”, “skills”.
#Сгенерируйте новый словарь с такими же ключами, а в значениях типы значений.

d = {"name": "Natasha", "surname": "Tiutiunnyk", "age": 65, "position": "QA engineer", "address": "Kyiv some str.566", "skills": ["smart", "sadsad", "dfsd"]}
d1 = {k: type(v) for k, v in d.items()}
print(d1)


# Сгенерируйте новый словарь с только парами ключ-значение, если значение исходного словаря было строкой.
# Значения нового словаря должны быть переведены в нижний регистр и удалены всё небуквенные символы из них.

d = {k: only_alphabet(d[k].lower()) for k in d if type(d[k]) == str}
print(d)
