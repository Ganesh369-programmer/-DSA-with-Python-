
class Node:
    def __init__(self , value):
        self.data = value
        self.next = None

def print_LL(head):
    temp = head

    while(temp != None):
        if(temp.next == None):
            print(temp.data)
            temp = temp.next
        else:
            print(temp.data , end="->")
            temp = temp.next 
    return 

#this function take more time complexity 
def take_input():
    value = int(input('Enter the Value :'))
    head = None

    while(value != -1):
        newNode = Node(value)
        if head == None:
            head = newNode
        else:
            temp = head 
            while (temp.next != None):
                temp = temp.next
            temp.next = newNode

        value = int(input("Enter the Value :"))

    return 


#this function takes less time complexity 
def better_input():
    value = int(input('Enter the value :'))
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

        value = int(input("enter the value :"))
    return head

# newhead = take_input()
newhead = better_input()
print_LL(newhead)