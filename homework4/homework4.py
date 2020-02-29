# Задание 1. Со значениями по умолчанию
# Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:

# 1-е число – сколько строк будет в песне. По умолчанию 3
# 2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
# 3-е число – если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце стоит «!».
# По умолчанию 0


def create_song(q_ty_str=3, q_ty_la=3, i=0):
    la_list = []

    for x in range(q_ty_la):
        la_list.append("la")

    song = "-".join(la_list)
    song = song + "\n"
    song = song * q_ty_str
    if i == 0:
        last_char = "."
    else:
        last_char = "!"

    song = song[:-1] + last_char
    return song


result_song = create_song (2, 5, 1)
print(result_song)


# Задание 2 Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов.
# Учитываем, что может быть повторяющиеся значения аргументов.

def second_champion(*arguments):
    set_champ = set(arguments)
    list_champ = list(set_champ)
    list_champ.sort()
    return list_champ[-2]


result = second_champion(1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 2, 7, 6, 7)
print(result)


# Задание 3
# # Напишите функцию, которая удаляет все небуквенные символы внутри строки (ограничимся латинским алфавитом).
# # Проверьте, что вы правильно закодили с помощью инструкции assert.

def only_alphabet(str1):
    str2 = ''
    for i in range(len(str1)):
        if str1[i].isalpha():
            str2 += str1[i]
    return str2


res = only_alphabet("Some text,,, 343 !!! again text&*!")
print(res)
