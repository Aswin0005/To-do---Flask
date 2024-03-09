list1 = []

newItem = input("Enter your Task")

def insert(newItem):
    list1.append(newItem)

def delete(deleteItem):
    list1.remove(deleteItem)

def edit(oldName,newName):
    oldIndex = list1.index(oldName)
    list1[oldIndex] = newName
    '''for i in range(0,len(list1)):
        if(oldName == list1[i]):
            list1.pop(i)
            list1.insert(i,newName)'''

insert(newItem)
print(list1)
edit('Bread','Jam')
print(list1)
delete('Jam')
print(list1)
