import time
import random

starttime  = time.time()
def quicksort(list):
    if len(list)<=1:
        return list
    less_than = []
    greater_than = []
    pivot = list[0]
    for i in list[1:]:
        if i < pivot:
            less_than.append(i)
        else:
            greater_than.append(i)
    #print("%15s %1s %-15s" %(less_than, pivot, greater_than))
    return quicksort(less_than)+[pivot]+quicksort(greater_than)


list = []
for i in range(10000):
    n = random.randint(1, 50000)
    list.append(n)
print(quicksort(list))

print(f"Code took: {time.time()-starttime}s")