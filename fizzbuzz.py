print("FizzBuzz")
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print("FizzbUzz")
    elif(i%5==0):
        print("BUzz")
    elif(i%3==0):
        print("Fizz")
    else:
        print(i)