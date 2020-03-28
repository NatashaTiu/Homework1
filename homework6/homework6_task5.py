# Файл имеет вид таблицы: Фамилия Имя Отдел Зарплата (В первой строке заголовки колонок)
# Посчитайте сколько отделов на фирме
# Определите максимальную зарплату
# Определите максимальную зарплату в каждом отделе
# Выведите «Отдел Макс_Зарплата  Фамилия_человека_с_такой_зарплатой» в новый файл

l = []
l_total = []
with open("hmwrk6_task5", "r") as get_all:
    all_r = get_all.readline()
    all_table = get_all.readlines()

for line in all_table:
    l = line.split()
    l_total.append({
        'surname': l[0],
        'name': l[1],
        'unit': l[2],
        'salary': l[3]
    })

#print(l_total)

set1 = set()


def count_units():
    for i in range(len(l_total)):
        set1.add (l_total[i].get('unit'))
    return len(set1)

a = count_units()
print("The quantity of units: ", a)


list_of_salaries = []

def max_salary():
    for i in range(len(l_total)):
        list_of_salaries.append(int(l_total[i].get('salary')))
        list_of_salaries.sort()
    return list_of_salaries[-1]


b = max_salary()
print(b)

max_salaryes_in_units = {}
list1 = []
while len(set1) > 0:
   list1.append(set1.pop())


dict2 = {}
for index in range(len(list1)):
    dict2[list1[index]] = {
        'surname': '',
        'name': " ",
        'salary': 0
    }

for i in range(len(l_total)):
    if int(l_total[i]['salary']) > dict2[l_total[i]['unit']]["salary"]:
        dict2[l_total[i]['unit']].update({
            'surname': l_total[i]['surname'],
            'name': l_total[i]['name'],
            'salary': int(l_total[i]['salary'])
        })


def max_salary_in_unit():
    result = []
    for i, unit in enumerate(dict2):
        result.append({
            'unit': unit,
            'salary': dict2[unit]['salary']
        })
    return result

# Second variant for max salary in unit:
# def max_salary_in_unit():
    # result = {}
    # for i, unit in enumerate(dict2):
    #     result[unit] = dict2[unit]['salary']
    # return result

max_unit_salary = max_salary_in_unit()
#print(max_unit_salary)

total_res = []
def max_salary_to_file():
    for i, unit in enumerate(dict2):
        result = []
        result.append(unit)
        result.append(dict2[unit]["salary"])
        result.append(dict2[unit]['surname'])
        total_res.append(result)
    return total_res


#print(l_total)

d = max_salary_to_file()
print(d)

d_s = '\n'.join([' '.join(str(x) for x in row) for row in d])
print(d_s)

with open("hmwrk6_task5.1.txt", "a") as f1:
    f1.write('Unit Max_salary Surname\n')
    f1.write(d_s)


