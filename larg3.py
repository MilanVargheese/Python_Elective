List=[]
ch='y'
while ch!='n':
    num=int(input("Enter inputs: "))
    List.append(num)
    ch=input("Do you want to continues? (Y/N) ")
List.sort(reverse = True)
print(List[2])
