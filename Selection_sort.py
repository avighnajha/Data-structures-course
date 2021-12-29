import random
import time

start_time = time.time()

def selection_sort(list):
    sorted = []
    for i in range(0, len(list)):
        index_move = index_min(list)
        sorted.append(list.pop(index_move))
    return sorted
def index_min(list):
    min_index = 0
    for i in range(1, len(list)):
        if list[i] < list[min_index]:
            min_index=i
    return min_index

list = []
for i in range(10000):
    n = random.randint(1, 50000)
    list.append(n)
print(selection_sort(list))
time = (time.time() - start_time)

print(f"Time takes: {time} to run ")