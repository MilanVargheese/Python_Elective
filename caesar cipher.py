#Encrypt

string=input("Enter the String :")
key=int(input("Enter the Key: "))
encrypt=""
for char in string:
    ordvalue=ord(char)
    codevalue=ordvalue+key
    if(codevalue>ord('z')):
        codevalue=ord('a')+(codevalue-ord('z')-1)
    encrypt+=chr(codevalue)
print(encrypt)

#Decrypt

string=input("Enter the String :")
key=int(input("Enter the Key: "))
decrypt=""
for char in string:
    ordvalue=ord(char)
    codevalue=ordvalue-key
    if(codevalue<ord('a')):
        codevalue=ord('z')-(ord('a')-codevalue-1)
    decrypt+=chr(codevalue)
print(decrypt)
