class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, head: Node, data: int) -> Node:
        # Complete this recursive function
        if(head == None):
            newNode = Node(data)
            return newNode
        
        head.next = LinkedList.insert_at_tail(self , head.next , data)
        
        return head
