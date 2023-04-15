from random import randint # Тех задание - inplace, и не степени двойки
def my_merge(m1,m2):
    n = len(m1)
    m3 = []
    ind1 = 0
    ind2 = 0
    for i in range(n * 2):
        if ind1 == n:
            m3 += m2[ind2:]
            break
        if ind2 == n:
            m3 += m1[ind1:]
            break
        if m1[ind1] < m2[ind2]:
            m3 += [m1[ind1]]
            ind1 += 1
        elif m1[ind1] > m2[ind2]:
            m3 += [m2[ind2]]
            ind2 += 1
    return m3

def my_sorted(a):
    n = len(a)
    if n == 3:

    else:
        Hn = n // 2
        b = my_merge(my_sorted(a[:Hn]),my_sorted(a[Hn:]))
    #print(a,b)
    return b

k = 10
N = 2 ** k
Hi_bound = 1000000
arr = []
for i in range(N):
    arr += [randint(0,Hi_bound)]
print(my_sorted(arr) == sorted(arr))