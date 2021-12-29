import random

def is_sorted(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

def bogosort(list):
    attempts = 0
    while not is_sorted(list):
        random.shuffle(list)
        attempts +=1
    return list, attempts


list = [4,2,5,5,4,2,3,1]

print(bogosort(list))