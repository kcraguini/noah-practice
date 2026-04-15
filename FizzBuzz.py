# num is the variable for this loop and the range is 1-100
for num in range (1, 101):
    #checking if the number is divisible by 3 and 5
    if num % 3 ==0 and num % 5 ==0:
        print("FizzBuzz")
    elif num % 3 == 0:  
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    # if the number isnt divisible by these two numbers, itll just print the regular number
    else:
        print(num)