def GCD(x,y):
    r=x%y
    if(r==0):
        return y
    else:
        return GCD(y,r)
n=int(input("Enter the first number :"))
m=int(input("Enter the second number :"))
print("The GCD of two numbers is:", GCD(n,m))