print("WELCOME TO LOVE CALCULATOR")
name1= input("what is your name?")
name2= input("what is their name?")
 
combine_str=name1+name2
lower_name=combine_str.lower()

t=lower_name.count("t")
r=lower_name.count("r")
u=lower_name.count("u")
e=lower_name.count("e")

true= t+r+u+e

l=lower_name.count("l")
o=lower_name.count("o")
v=lower_name.count("v")
e=lower_name.count("e")

love=l+o+v+e

love_score=int(str(true)+str(love))

print(f"your love score is{love_score}")

