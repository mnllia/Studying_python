from random import randint
from datetime import datetime
# Давай по новой Миша, все в инплейс!
def my_sorted(arr):
    #return arr
    #count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    #        count += 1
    #print(count / len(arr) ** 2)
    return arr

N = 16
Hi_bound = 1000000
arr = []
for i in range(N):
	arr += [randint(0,Hi_bound)]
#print(arr)
#print(sorted(arr))
#my_sorted(arr)
#print(arr)
dt1 = datetime.now()
#print(sorted(arr) == my_sorted(arr))
for i in range(10000):
    my_sorted(arr)
dt2 = datetime.now()
delta = dt2-dt1
print(delta.microseconds,delta.microseconds // 10000 )
input()
