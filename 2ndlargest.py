num1=int(input("enter the first numner:"))
num2=int(input("enter the second number:"))
num3=int(input("Enter the third number:"))

if(num1>num2 and num1<num3)or(num1<num2 and num1>num3):
    print("middle number",num1)
elif(num2>num1 and num2<num3)or(num1<num2 and num2>num3):
    print("middle number",num2)
elif(num3>num2 and num3<num1)or(num3<num2 and num3>num1):
    print("middle number:",num3)
