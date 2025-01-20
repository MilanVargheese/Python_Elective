binary=input("Enter Binary value: ")
length=len(binary)
decimal=0
for i in range(length):
    decimal+=int(binary[length-i-1])*int(2**i)
print(decimal)
