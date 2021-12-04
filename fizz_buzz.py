for i in range(1,101):
    print(i)
    if (i % 3 == 0) and (i % 5 != 0):
        i == "Fizz"
        print("Fizz")
    elif (i % 5 == 0) and (i % 3 != 0):
        i == "Buzz"
        print("Buzz")
    elif i % 15 == 0:
        i == "FizzBuzz"
        print("FizzBuzz")
        
