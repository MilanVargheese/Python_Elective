List=[]
ch='y'
while ch!='n':
    num=int(input("Enter inputs: "))
    List.append(num)
    ch=input("Do you want to continues? (Y/N) ")
print("Largest element: ", max(List))
print("Smallest element: ", min(List))

