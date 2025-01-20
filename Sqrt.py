number=int(input("Enter the number: "))
if(number<2):
    print("Square root: ",number)
else:
    a=number
    b=(a+(number/a))/2
    while abs(b-a)!=0:
        a=b
        b=(a+(number/a))/2
    print("Square root: ",b)
