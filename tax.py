print("Welcome Tax calculator")
Tax=0
pr=int(input("enter the bike price\n"))
if pr>100000:
    tax=15/100*pr
elif pr>50000 and pr<=100000:
    tax=10/100*pr
else:
    tax=5/100*pr

print("Tax to be paid",tax)
 