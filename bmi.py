# weight = input("your weight")
# height=input("your height")
# new_height=int(height)
# new_height= float(height ** 2)
# BMI= (weight/new_height)
# print(BMI)



# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_height = float(height)
new_weight = int(weight)
bmi=new_weight/(new_height ** 2)
new_bmi=int(bmi)
print(new_bmi)