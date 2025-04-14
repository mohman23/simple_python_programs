#my working program to check if a number is prime or not.

num = int(input("Please enter a number to check if it's prime or not: "))

print("Number you entered is:", num)

# Special case for 1
if num == 1:
    print("1 is neither prime nor composite, it is a unit.")

# Check for prime
elif num > 1:
    for i in range(2, num):
        #This for loop will keep running until it checks all numbers between 2 and num-1.
        if num % i == 0:
            print("The number you entered isn't a prime number.")
            break
    else:
        #This else belongs to the for loop, not the if!
        #The else attached to a for loop only runs if the loop didn’t break early.
        #It's a special Python feature which allows else to run with a for loop.
        print("The number you entered is a prime number.")
else:
    print("Please enter a positive integer greater than 0.")
