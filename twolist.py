List1=[]
List2=[]

def inputList(List):
    ch='y'
    while ch!='n':
        num=int(input("Enter Element: "))
        List.append(num)
        ch=input("Do you want to continues? (Y/N) ")
    return List

print("Enter inputs for List 1")
List1=inputList(List1)
print("Enter inputs for List 2")
List2=inputList(List2)
    
Newlist=[]

for elem1 in List1:
    for elem2 in List2:
        if(elem1==elem2):
            Newlist.append(elem1)
print("New List: ",Newlist)
