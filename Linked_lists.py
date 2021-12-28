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

    def insert(self, data, index):
        """Inserta a new node containing data at the index required. Basically we state what position we want it at and on each iteration of the while loop decrease the value of position till it equals 1 meaning that the target position is the next one. Then we can name the next_node of the current as the new data we have and the the next_node of the new data as wahtever was on the required index.
        Insertion takes O(1) but finidn node at insertion point takes linear. Therefore overall linear time as we take worst case.
        """
        if index == 0:
            self.add(data)
        
        if index>0:
            new = Node(data)
            position = index
            current = self.head

            while position>1:
                current.next_node
                position -= 1
            prev = current
            next = current.next_node
            prev.next_node = new
            new.next_node = next

    def remove(self, key):
        """Removes node containing data that matches the key, returns NOne if key doesnt exist, takes O(n) time."""
        current = self.head 
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position+=1
            return current

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