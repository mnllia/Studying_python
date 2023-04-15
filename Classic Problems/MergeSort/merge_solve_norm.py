a = open('test2.in')
b = open('test2.out', 'w')
str_list = list(a)
n = int(str_list[0])
m1 = [int(s) for s in str_list[1].split(' ')]
m2 = [int(s) for s in str_list[2].split(' ')]

m3 = []
m4 = sorted(m1+m2)
ind1 = 0
ind2 = 0
for i in range(2 * n):
    if ind1 == 1000:
        m3 += m2[ind2:]
        break
    if ind2 == 1000:
        m3 += m1[ind1:]
        break
    if m1[ind1] < m2[ind2]:
        m3 += [m1[ind1]]
        ind1 += 1
    elif m1[ind1] > m2[ind2]:
        m3 += [m2[ind2]]
        ind2 += 1

if m3 == m4:
    print('Nice')
else:
    print('Nah')