print("Python Calculator")

def add(P,Q):
    return P+Q
def subtract(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q
def divide(P,Q):
    return P//Q

print("Enter the operation:")
print("a.add")
print("b.subtarct")
print("c.multiply")
print("d.divide")

choice=input("Please enter the choice(a/b/c/d):    ").lower()

num_1=float(input("Enter the first number:\n"))
num_2=float(input("Enter the second number:\n"))

if choice=="a":
 print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice=='b':
 print(num_1,"-",num_2,"=",subtract(num_1,num_2))
elif choice=='c':
 print(num_1,"*",num_2,"=",multiply(num_1,num_2))
elif choice=='d':
 print(num_1,"/",num_2,"=",divide(num_1,num_2))
else:
   print("Invalid operation")





    

