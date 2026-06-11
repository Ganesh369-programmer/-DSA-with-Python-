from common import Node , better_input , print_LL

head = better_input()

def insert_at_tail(head , data):
    newNode = Node(data)
    #base case
    if head == None:
        return newNode

    temp = head 
    while(temp.next != None):
        temp = temp.next 
    temp.next = newNode

    return head


def insert_at_tail_rec(head ,data):
    temp = head
    if(temp.next == None):
        newNode = Node(data)
        return newNode
         
    temp.next = insert_at_tail_rec(temp.next , data)

    return temp

ans = insert_at_tail_rec(head , 100)
print_LL(ans)
    