# import unittest
# #
# # class TestClass(unittest.TestCase):
# #     def setUp(self):
# #         print ("\n set up of", self)
# #
# #     def tearDown(self):
# #         print ("\n tear down of", self)
# #
# #     def test_1(self):
# #         print("test1")
# #
# #     def test_2(self):
# #         print("test2")
# #
# # if __name__ == "__main__":
# #     unittest.main()



# l =[1, "2", "string some", True, "asaa", "123some text!!! 12", "Hello! what???"]
# # new_l = []
# # for i in l:
# #     i = str(i)
# #     new_l.append(i)
# #
# new_l = [int(x) for x in l  if str(x).isdigit()]
# print(new_l)

#
#У вас есть список, в котором могут быть разные типы данных. Создайте новый список только строк, при этом удалите
# усе небуквенные символы из них. Воспользуйтесь функцией из предыдущего задания
# (импортируйте её из другого своего файла)

from homework4.homework4 import only_alphabet

l_in = [1, "2", "string some", True, "asaa", "123some text!!! 12", "Hello! what???"]
l_out1 = [only_alphabet(string) for string in l_in if type(string) == str]
print(l_out1)

dict_abc = {"a": 1, "b": 2, "c": 3, "d": 3}
dict_123 = {v:k for k, v in dict_abc.items()}
print(dict_123)

d = {"name": "Natasha", "surname": "Tiutiunnyk", "age": 65, "position": "QA engineer", "address": "Kyiv some str.566", "skills": ["smart", "sadsad", "dfsd"]}
d1 ={k:type(v) for k, v in d.items()}
print(d1)
#Сгенерируйте новый словарь с только парами ключ-значение, если значение исходного словаря было строкой.
# Значения нового словаря должны быть переведены в нижний регистр и удалены всё небуквенные символы из них.
from homework4.homework4 import only_alphabet
d = {k: only_alphabet(d[k].lower()) for k in d if type(d[k]) == str}
print(d)