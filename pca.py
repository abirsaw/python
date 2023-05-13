# b=int(input("Enter the base of traingle:"))
# h=int(input("Enter the height of traingle:"))
# print(h,b)
# area=(b*h)/2
# print(area)

# a=int(input("Enter the first number"))
# b=int(input("Enter the second number:"))
# temp=a
# a=b
# b=temp
# print("after the swapping: ",a)
# print("after the swapping:",b)

# print("square root")
# num=float(input("Enter the number:"))
# num_sqrt=num**0.5
# print(f"the sqaure root is:{num_sqrt}")

# import cmath
# a=float(input("Enter the value of a:"))
# b=float(input("Enter the value of b:"))
# c=float(input("Enter the value of c:"))
# d=(b**2)-(4*a*c)
# s1=(-b-cmath.sqrt(d))/(2*a)
# s2=(-b+cmath.sqrt(d))/(2*a)
# print(f"The solution of s1 and s2{s1,s2}")

print("simflying floating numbers")
num1=float(input("enter the first number:"))
num2=float(input("Enter the second number:"))

print("Enter the operation you want to perform")

ch=input("Enter the operation you want to perform:")
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

print(num1,ch,num2,":",result)
