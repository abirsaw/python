def rsum(n):
    if n<=1:
        return n
    else:
        return n+rsum(n-1)
num=int(input("Enter the numbers:"))
ttl=rsum(num)
print("The sum is:",ttl)