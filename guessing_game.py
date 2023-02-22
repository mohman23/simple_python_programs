import random

random_number = random.randint(1,10)
#random_number = 5

#guess = None


guess = input("Guess a number between 1 and 10: ")
guess = int(guess)

play_again = None

while True:
#for x in range(10,):	
	#guess = input("Guess a number between 1 and 10: ")
	#guess = int(guess)

	if guess < random_number:
		print("Too low, try again!")
		guess = int(input("Guess a number between 1 and 10: "))
	elif guess > random_number:
		print("Too high, try again!")
		guess = int(input("Guess a number between 1 and 10: "))
	if guess == random_number:
		print("You guessed it! You won!")
		play_again = input("Do you want to continue playing? (y/n)")
		if play_again == "y":
			random_number = random.randint(1,10)
			guess = input("Guess a number between 1 and 10: ")
			guess = int(guess)
		else:
			print("Thank you for playing.")
			break

#print(random_number)
