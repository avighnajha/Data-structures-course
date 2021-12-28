class Node():
    """
    An object for storing a single node of a linked list models 2 attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "<Node data: %s>"% self.data

# N1 = Node(10)
# #print(N1)
# N2 = Node(20)

# N1.next_node = N2
# print(N1.next_node)

class LinkedList: 
    """Singly linked list"""
    """We're basically making a datastructure and making all the methods for it just like lists have .sort() and shit like that"""
    def __init__(self):
        self.head = None 
    def is_empty(self):
        return self.head == None
    def size(self):
        """Returns number of nodes in a list and runs in linear time"""
        current = self.head
        count =0

        while current:
            count +=1
            current  = current.next_node
        return count

    def add(self, data):
        """This method adds makes the current head of the list into the 2nd node and adds a new node at the head of the list. Takes constant time as we just reasign properties to different data."""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """Search for the first node with data that matches the key, Returns node or NONE if not found 
        Takes O(n) if not found
        """
        current  = self.head 

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def __repr__(self):
        """Return a string representation of the list basically used to allow us to actially see the list, Takes O(n) time"""
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]"% current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]"% current.data)
            else:
                nodes.append("[%s]"%current.data)

            current = current.next_node
        return "-->".join(nodes)


l = LinkedList()

l.add(1)
l.add(2)
l.add(3)
l.add(92)
n = l.search(92)
print(n)
print(l)