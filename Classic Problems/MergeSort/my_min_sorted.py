from random import randint
# Давай по новой Миша, все в мин!
def my_min(arr, start):
    for i in range(start, len(arr)):
        if arr[i] < arr[j]:
            
    return j

def my_sorted(arr):
    #return arr
    #count = 0
    for i in range(len(arr)):
        j = my_min(arr, i)
    return arr

N = 5000
Hi_bound = 1000000
arr = []
for i in range(N):
	arr += [randint(0,Hi_bound)]
#print(arr)
#print(sorted(arr))
#my_sorted(arr)
#print(arr)
print(sorted(arr) == my_sorted(arr))
input()
