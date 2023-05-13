def findgcd(a,b):
    if(b==0):
        return a
    else:
        return findgcd(b,a%b)
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    gcd=findgcd(num1,num2)
    lcm=(num1*num2)
    print("LCM is:",lcm)