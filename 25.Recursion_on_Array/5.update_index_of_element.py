def updateIndex(l1 , x , index , anslist):
    if(len(l1) == index):
        return 
    
    if (l1[index] == x):
        anslist.append(index)

    updateIndex(l1 , x , index + 1 , anslist)

anslist = []
updateIndex([3 , 2 , 5 , 4 , 2 , 8 , 3 , 2] , 2 , 0 , anslist)
print(anslist)