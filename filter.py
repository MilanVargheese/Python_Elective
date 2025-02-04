List=[]
ch='y'
while ch!='n':
    num=int(input("Enter inputs: "))
    List.append(num)
    ch=input("Do you want to continues? (Y/N) ")
Newlist=[]
numb=int(input("Enter the filter number: "))
for elem in List:
    if(elem<numb):
        Newlist.append(elem)
print(Newlist)
