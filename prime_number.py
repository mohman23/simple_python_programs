num = int(input("Please enter a number to check if it's prime or not: "))

print("Number you entered is:", num)

# Special case for 1
if num == 1:
    print("1 is neither prime nor composite, it is a unit.")

# Check for prime
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("The number you entered isn't a prime number.")
            break
    else:
        # This else belongs to the for loop, not the if!
        print("The number you entered is a prime number.")
else:
    print("Please enter a positive integer greater than 0.")
