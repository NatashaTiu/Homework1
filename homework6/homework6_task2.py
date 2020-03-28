#song
# 2.1.1 записать вашу песню la-la-la в текстовый файл с помощью print

from homework4.homework4 import create_song

song = create_song(4, 5, 1)
f = open("hmwrk6_task2.txt", "a")
print(song, file=f)
f.close()

# 2.1.2 записать вашу песню la-la-la в текстовый файл с помощью методов

song2 = create_song(2, 8, 0)
f = open("hmwrk6_task2.txt", "a")
f.write(song2)
f.close()

# 2.2 записать вашу песню la-la-la в текстовый файл с помощью менеджером контекста для файлов (with … as).

song3 = create_song(1, 1, 0)
with open("hmwrk6_task2.txt", "a") as f:
    f.write(song3)

# Person
# 2.1.1 Прочитать и вывести на экран код файла, в котором вы создавали класс Person

f2 = open("D:\study\infopulse\homework\homework5\homework5_1.py", "r")
for line in f2:
    print(line)
f2.close()

# 2.2 Прочитать и вывести на экран код файла, в котором вы создавали класс Person с помощью менеджером контекста для
# файлов (with … as).

with open("D:\study\infopulse\homework\homework5\homework5_1.py", "r") as f3:
    for line in f3:
        print(line)

#Задание со слайда 8
# Задание: считываем построчно строки из файла и выводим строки, добавляя в конец этих строк восклицательный знак.

with open("D:\study\infopulse\homework\homework5\homework5_1.py", "r") as f4:
    for line in f4:
        print(line.rstrip()+"!")

# задание со слайда 9
# Записываем “Number: строка из файла” из одного файла в другой. Не забываем закрывать файлы

f6 = open("hmwk6_task2.2", "a")
f5 = open("D:\study\infopulse\homework\homework5\homework5_1.py", "r")
i = 1
for line in f5:
    f6.write(str(i))
    f6.write(line)
    i += 1
f6.close()
f5.close()

# Напишите программу, которая пытается преобразовать текст из файла в число. Файл должен все равно закрываться в блоке
# finally. Если преобразование удалось (в блоке else) – выводится сообщение «I did it!»

with open("hmwrk6_task3.txt", "r") as f7:
    read_f = f7.read()
    try:
        read_f = int(read_f)
    except:
        print("Text in file is not an integer")
    else:
        print("I did it!")
    finally:
        f7.close()
