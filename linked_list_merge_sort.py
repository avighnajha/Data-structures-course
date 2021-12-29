from Linked_lists import LinkedList

"""Again we split the functions into a whole merge_sort function, a split function annd a merge function """

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    -Recursicely divide linked list into sublists containing a single node
    -Repeatedly merge the sublists to produce sorted siblists until one remains
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list) #Our own function

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right) #Our function


def split(linked_list):
    """Divide the unsorted list at midpoint into sublists. Works in o(kln(n))"""

    if linked_list == None or linked_list.head == None:
        left_half = linked_list 
        right_half = None

        return left_half, right_half
    
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        return left_half, right_half

def merge(left, right):
    """
    Merges 2 linked lists sorting by data in the nodes, returns a new merged list.
    Linear time 
    """
    # create a new linked list with nodes from merging left and right

    merged = LinkedList()
    # Now we add a fake head that we get rid of later

    merged.add(0)

    current = merged.head # Set current as the head of linked list

    #get head nodes of left and right linked list
    left_head  = left.head
    right_head = right.head

    # iterate over left and iright until we reach the tail node of either

    while left_head or right_head:
        if left_head == None:
            current.next_node = right_head 
            #we just switch focus to the right head as the left list is now finished. This is the same as the merge bit in Merge_sort
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            #if the node is neither a head nor tail
            left_data = left_head.data
            right_data = right_head.data

            if left_data<right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head =  right_head.next_node
        
        current = current.next_node

    head = merged.head.next_node
    merged.head = head

    return merged

l = LinkedList()

l.add(35)
l.add(5)
l.add(84)
l.add(1023)
l.add(9)
l.add(23)
l.add(92)
l.add(55)

sorted = merge_sort(l)
print(sorted)

