a = open('test2.in')
b = open('test2.out', 'w')
str_list = list(a)
n = int(str_list[0])
m1 = [int(s) for s in str_list[1].split(' ')]
m2 = [int(s) for s in str_list[2].split(' ')]
#print(len(m1), m1[:10])
#print(len(m2), m2[:10])

#n = int() #  Каждый элемент 1 раз
#m1 = [int(n) for n in .split(' ')]
#m2 = [int(n) for n in .split(' ')]

m4 = sorted(m1+m2)
m3 = []
for i in range(2 * n):
    if m1 == []:
        m3 += m2
    elif m2 == []:
        m3 += m1
    elif m1[0] >= m2[0]:
        m3 += [m2[0]]
        m2.pop(0)
    else:
        m3 += [m1[0]]
        m1.pop(0)


if len(m3) != len(m4):
    print('Wrong len', len(m3), len(m4))
if m3 == m4:
    print('SUCCESS!!')
else:
    print('Oooops')
    print(len(m3))


#print(m3, file= b)
input()