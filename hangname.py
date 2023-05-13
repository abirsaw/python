import random
word_list = ["aardvark", "baboon", "camel"]
choice=random.choice(word_list)
print(choice)
word=input("Enter the word \n").lower()
random_choice=random.choice(choice)
for i in choice:
    if i==word:
        print("right")
    else:
        print("wrong")