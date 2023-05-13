print("welcome to tip calculator!")
bill=float(input("what was the total bill?$"))
tip=int(input("How much tip would you like yo give?"))
people=int(input("how many people are there"))
bill_with_people=tip/100*bill+bill
each_person=float(bill_with_people/people)
print(each_person)