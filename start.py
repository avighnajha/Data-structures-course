
# def binary_search(list, target):
#     list.sort()
#     first = 0
#     last = len(list)-1
#     while first <= last:
#         mid = (first+last)//2
#         if list[mid] == target:
#             return mid
#         elif list[mid]<target:
#             first = mid +1
#         else:
#             last = mid - 1
#     return None
# print(binary_search([4,1,2,3,5,6], 3))

def rec_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return rec_binary_search(list[midpoint+1:], target)
            elif list[midpoint] > target:
                return rec_binary_search(list[:midpoint], target)
print(rec_binary_search([1,2,3,4, 5,6], 7))