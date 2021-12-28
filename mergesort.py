def merge_sort(list):

    """
    Sorts a list in ascending order, returns a NEW sorted list.
    DIvide: First find midpoint of list and split.
    Conquer: Recursively sort teh sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """

    #Base case
    if len(list)<=1:
        return list
    #divide
    left_half, right_half = split(list) #split is our function

    #conquer
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right) #merge is our function

def split(list):
    """
    Divide the unsorted list at midpoint into sublists and returns 2 sublists - left and right
    """

    mid = len(list)//2

    left = list[:mid]
    right = list[mid:]
    return left, right

def merge(left, right):
    """
    Merges 2 lists or arrays sorting them in the process
    Returns a new merged list
    """
    l = []
    i = 0 #index of left
    j = 0 #index of right

    while i<len(left) and j< len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1

    while i<len(left):
        l.append(left[i])
        i+=1
    while j<len(right):
        l.append(right[j])
        j+=1
    return l
    

def verify_sorted(list):
    n = len(list)

    if n ==0 or n==1:
        return True
    
    return list[0]< list[1] and verify_sorted(list[1:])


list = [3,49,257,235,66,22]

l = merge_sort(list)
print(l)
print(verify_sorted(l))