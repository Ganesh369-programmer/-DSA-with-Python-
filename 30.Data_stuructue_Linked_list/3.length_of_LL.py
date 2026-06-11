from common import Node , better_input , print_LL

def lengthofLL(head):
    temp = head
    ans = 0

    while(temp != None):
        temp = temp.next 
        ans += 1

    return ans

headofLL = better_input()
# length = lengthofLL(headofLL)
# print(length)


def lengthofrecursion(head):
    if(head == None):
        return 0

    answer = lengthofrecursion(head.next)

    return answer + 1

length = lengthofrecursion(headofLL)
print(length)