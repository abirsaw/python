print("Reverse of number")
a=int(input("Enter the number"))
rev=0
while(a>0):
    b=a%10
    rev=rev*10+b
    a=a//10
print("Reverse of number",rev)