#Дана последовательность натуральных ненулевых чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.


z=[4,4,4,4,4,4, 5, 6, 6, 6, 7, 8, 8, 8, 8, 8, 6, 4, 4, 4, 0]
if len(z) == 0:
    curr_seq_len = 0
    max_seq_len = 0
else:
    curr_seq_len = 1
    max_seq_len = 1
for x in range(len(z) - 1):
    if z[x] == z[x+1]:
        curr_seq_len += 1
        max_seq_len = max(max_seq_len, curr_seq_len)
    else:
        curr_seq_len = 1

print(max_seq_len)

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