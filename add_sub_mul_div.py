print("Simplying Floating numbers")

num1=float(input("Enter the first number:\n"))
num2=float(input("Enter the scond number:\n"))

print("Enter the operation you would like to do:\n")

ch=input("Enter the ch you want to do:\n")
result=0
if ch=='+':
    result=num1+num2
elif ch=='-':
    result=num1-num2
elif ch=='*':
    result=num1*num2
elif ch=='/':
    result=num1/num2
else:
 print("invalid operation")

print(num1, ch , num2, ":",result)
