List=[]
ch='y'
while ch!='n':
    num=int(input("Enter inputs: "))
    List.append(num)
    ch=input("Do you want to continues? (Y/N) ")
Newlist=[]
for elem in List:
    if(elem%2==0):
        Newlist.append(elem)
Newlist.sort()
print(Newlist)
