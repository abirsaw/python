print("BMI 2.0")

height=float(input("Enter Your Height:\n"))
weight=float(input("Enter Your Weight:\n"))
bmi=round(float(weight/(height**2)),2)
print("Your BMI is :\n",bmi)

if bmi<18.5:
    print("you are underweight")
elif bmi<25:
    print("You have a normal weight")
elif bmi<30:
    print("you are overweight")
elif bmi<35:
    print("you are obsese")
else:
    print("You are clinically obese")