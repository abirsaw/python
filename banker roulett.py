import random
print("Banker Roulette")

names=input("Enter the names:\n")
n_name=names.split(", ")
new_name=random.randint(n_name)
print(new_name)
