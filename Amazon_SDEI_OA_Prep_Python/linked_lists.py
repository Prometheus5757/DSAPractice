'''
Singly linked lists
'''
class SinglyNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

# Connecting nodes with each other
head.next = A
A.next = B
B.next = C # C points to nothing

print("head of cursor: ", head) # shows value of first node (1)


#Traverse the list: O(n)

curr = head
print("linked list traversal:")
while curr: #while the current node is not None (aka last node)
    print("current node: ", curr)
    curr = curr.next



# Display Linked List - O(n)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))
    # we use join here, to add a ' -> ' symbol between each element of a list

display(head)


#Search for node value - O(n)

def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False

print(search(head, 7))

'''
Doubly Linked Lists
'''

class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)
    
head = tail = DoublyNode(1) #need access to both head and tail
print("\n\nDoubly Linked Lists:")
print("head: ", head)
print("tail: ", tail)

# Display - O(n)
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" <-> ".join(elements))

display(head)

#insert at beginning - O(1)
def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head) #create a new node, with the next node being our current head
    head.prev = new_node #set the previous node for our head to be new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, 3)
display(head)

#insert at beginning - O(1)
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail) #create a new node, with the previous node being our current tail
    tail.next = new_node #set the next node for our tail to be new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 7)
display(head)
