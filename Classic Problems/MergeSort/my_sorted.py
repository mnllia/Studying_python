from random import randint
# тех задание - sorted самому
def my_sorted(arr_in):
    arr_out = []
    for i in range(len(arr_in)):
        arr_out += [min(arr_in)]
        arr_in.pop(arr_in.index(min(arr_in)))
    return arr_out
N = 100
arr = []
for i in range(N):
	arr += [randint(0,100)]
print(sorted(arr) == my_sorted(arr))
input()