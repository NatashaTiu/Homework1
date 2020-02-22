#Воспользуйтесь одним print(), но при этом выводите с новой строки:
#1.1 Сначала выведите третий символ этой строки.
#1.2 Во второй строке выведите предпоследний символ этой строки.
# 1.3 В третьей строке выведите первые пять символов этой строки.
# 1.4 В четвертой строке выведите всю строку, кроме последних двух символов.
# 1.5 В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся, начиная с первого символа).
#1.6 В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
#1.7 В седьмой строке выведите все символы в обратном порядке.
#1.8 В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
#1.9 В девятой строке выведите все символы строки через один в обратном порядке, начиная с предпоследнего.
#1.10 В десятой строке выведите все символы в обратном порядке без первого и последнего элемента.
#1.11 Ну, и напоследок выведите длину данной строки.


try:
    a = input ("Enter some string: ")
    print(a[2], a[-2], a[0:5], a[:-2], a[::2], a[1::2], a[::-1], a[::-2], a[-2::-2], a[-2:0:-1], len(a), sep="\n")
except IndexError:
    print("String should have 3 or more symbols")

# 2. Пользователь вводит строку. Разрежьте её на две части – равные, если длина строки чётная, а если длина строки нечётная, то длина первой части должна быть на один символ больше.
# Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.

b = input ("Enter some string: ")
if len(b)%2>0:
    c = b[0:len(b)//2+1]
    d = b[len(b)//2+1:]
else:
    c = b[0:len(b) // 2]
    d = b[len(b) // 2 :]

b=d+c
print (b)

# 3.1 Напишите счетчик с помощью конструкции while, который выводит числа от 0 до 10.
c=0
while c<=10:
    print (c)
    c +=1


# 3.2 Напишите счетчик с помощью конструкции while, который выводит числа от 20 до 1. Попробуйте вывести числа в одной строчке, разделённые пробелом
d=20
while d>=1:
    print(d)
    d -=1

# 3.3 Напишите цикл while, в котором вы, если число чётное, каждую итерацию уменьшаете его в 2 раза.
# Вы делите целое чётное число на 2 пока от него не останется нечётный остаток. Посчитайте сколько раз вы делили нацело на 2.
e = input ("Enter some number: ")
e=int(e)
f = 0
if e == 0:
    print("Infinity")
else:
    while e%2 ==0:
        e=e/2
        f +=1
print(f)


# 4.1 Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым
list = [1, 4, 6, 8, 89]

while len(list)>0:
    list = list[1:]
    print (list)


# 4.2 Как сделать это же задание со строкой: напишите цикл, который выводит на экран и «удаляет» первый символ строки, пока она не станет пустой?
str = ("89 df dfs fssfs 21")

while len(str)>0:
    str = str[1:]
    print (str)

# 4.3 Напишите цикл, который выводит на экран и удаляет элементы списка от самого маленького до самого большого, пока он не останется пустым.
list = [1, 56, 4, 6, 8, 3, 89]
list.sort()
while len(list)>0:
    list = list[1:]
    print (list)

# 4.4 Дана последовательность натуральных ненулевых чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
z=[4, 5, 6, 6, 6, 7, 8, 8, 8, 8, 8, 6, 4, 4, 4, 0]
x =0
y = 0
l=[]
while x<len(z)-1:
   if z[x] == z[x+1]:
        y +=1
        x +=1
        print("yes", x)
        print("y= ", y)
        l.append(y)
        print(l)
        l.sort()
        print("q-ty: ", l[-1]+1)
   else:
       x+=1
       y=0
       print ("no", x)

#5 Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не является числом (любым), то должна выполняться конкатенация,
# т. е. соединение, строк. В остальных случаях введённые числа суммируются.
a = input ("Enter 1st number: ")
b = input ("Enter 2nd number: ")

try:
    a=float(a)
    b=float(b)
    d=a+b
    print(d)
except:
    print(a+b)

#6.1 Пишем функцию, которая попросит ввести число. Пока он не введёт правильно, просите его ввести. Функция возвращает введённое число.
def  check_isNumber():

    while True:
        i = input("Enter number:")
        try:
             i = float(i)
        except:
            print ("It is not number. Please, try again enter number")
        else:
            break
    return i

m = check_isNumber()

print(m)

# 6.2 Пишем функцию, которая попросит пользователя ввести слово (строка без пробелов в середине, а вначале и в конце пробелы могут быть).
# Пока он не введёт правильно, просите его ввести. Функция возвращает введённое слово.
while True:
    x = input("Enter word: ")
    x=x.strip()
    b=x
    x = x.split(" ")
    if len(x) !=1:
        print("Try again!")
    elif  b.isalpha() !=1:
        print("Try again!")
    else:
        print("Yes")
        break


#6.3 Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

def  check_isIntercalary(year):
    aa = year
    if aa % 400 == 0:
        answer ="YES"

    elif aa % 100 == 0:
        answer ="NO"

    elif aa % 4 == 0 and not aa % 100 == 0:
        answer ="YES"

    else:
        answer ="NO"
    return answer

answer_isYearIntercalary = check_isIntercalary(2100)

print(answer_isYearIntercalary)

#6.4 Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами. Если треугольник существует, вернёт True, иначе False

def  check_isTriangle(first, second, third):
    listOfNum=[first, second, third]
    listofNumNew = sorted(listOfNum)
    if listofNumNew[-1]>=listofNumNew[0]+listofNumNew[1]:
        answer ="NO"
    else:
        answer ="YES"
    return answer

answer_isTriangle = check_isTriangle(3, 5, 9)

print(answer_isTriangle)

# 6.5 Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами и если существует, то возвращает тип треугольника
# Equilateral triangle (равносторонний), Isosceles triangle (равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not a triangle).
a=3
b=4
c=5
def  check_TypeTriangle(first, second, third):
    listOfNum=[first, second, third]
    print (listOfNum)
    listofNumNew = sorted(listOfNum)
    if listofNumNew[-1]>=listofNumNew[0]+listofNumNew[1]:
        answer ="Not a triangle"
    else:
        if first == second == third:
            answer ="Equilateral triangle."
        elif first == second or first == third or  second == third:
            answer = "Isosceles triangle."
        else:
            answer = "Versatile triangle."

    return answer

answer_TypeTriangle = check_TypeTriangle(a, b, c)

print(answer_TypeTriangle)


# 6.6 Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
# вычисляющую расстояние между точками с координатами (x1, y1) и (x2, y2). Считайте четыре действительных числа от пользователя и выведите результат работы этой функции.

x1=1
x2=3
y1=6
y2=-9

def distance(x1, y1, x2, y2):
    dist=((x2-x1)**2+(y1-y2)**2)**(1/2)
    return dist

my_dist= distance (x1, y1, x2, y2)
print(my_dist)


#7.
str="We are not what we should, be!!!\n We are not what we need to be. But at least we are not what we used to be (Football Coach)"

#7.1 Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
x=str.split()
print(len(x))

# 7.2 Удалите знаки препинания в списке слов (пройдитесь циклом все слова и удалите методом strip знаки препинания)
c=len(x)
while c>0:
    x[c-1]=x[c-1].strip('!(),".-')
    c -= 1
#y=" ".join(x)
#print(y)

# 7.3 Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
x.sort()
print(x)

#7.4 Посчитать, сколько раз встречается каждое слово.
#(Подсказка: создавать словарь, где ключи — это слова из текста, а в значениях подсчитываем количество «встречаний» этого слова)
#Слова с большой буквы и с маленькой это все равно одно и тоже слово

str="We are not what we should, be!!!\n We are not what we need to be. But at least we are not what we used to be (Football Coach)"
l=str.split()
c=len(l)
while c>0:
    l[c-1]=l[c-1].strip('!(),".-').lower()
    c -= 1

d = {}
for i in range(len(l)):
    if l[i] in d:
        d[l[i]] += 1
    else:
        d[l[i]] = 1


print(d)