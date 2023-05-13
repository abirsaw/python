print("Voting")
age=int(input("Enter the age of the person:"))
if age>=18:
    print("You're eligible to vote ")
else:
    p=18-age
    print("You're not eligible\n",p,"years left to be eligible")