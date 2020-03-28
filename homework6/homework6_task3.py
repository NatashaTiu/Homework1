# Записывает в новый файл все слова в алфавитном порядке из другого файла с текстом. Каждое слово на новой строке.
# Рядом со словом укажите сколько раз оно встречалось в тексте

with open("hmwrk6_task3.txt", "r") as f8:
    read_f = f8.read()

l = read_f.split()
c = len(l)
while c > 0:
    l[c-1] = l[c-1].strip('!(),".-').lower()
    c -= 1

l.sort()

d = {}
for i in range(len(l)):
    if l[i] in d:
        d[l[i]] += 1
    else:
        d[l[i]] = 1

print(d)
