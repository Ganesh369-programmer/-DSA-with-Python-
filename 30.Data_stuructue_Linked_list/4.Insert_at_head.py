from common import print_LL

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    
def take_input():
    value = int(input('Enter the value :-'))
    head = None
    tail = None
    while(value != -1):
        newNode = Node(value)

        if(head == None):
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        value = int(input('Enter the value -> '))

    return head

def insert_at_head(head , data):
    newNode = Node(data)
    newNode.next = head
    head  = newNode
    return head

head = take_input()
print_LL(head)

print('after the inserting at head')
head = insert_at_head(head , 100)
print_LL(head)