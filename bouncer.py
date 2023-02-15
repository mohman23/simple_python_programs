#This prgram will ask a user for his/her age.
#if the age is between 18 - 21, wear a wristband.
#if the age is 21+, you can drink, normal entry.
#else, you are too young, sorry, no entry.

age = input("How old are you: ")

#the value return was a string, so we are converting it to int.

if age != "":
	age = int(age)
	if age >= 18 and age < 21:
		print("You are",age,"years old, you can enter, but you'll need to wear a wristband.")
	elif age >= 21:
		print("You are",age,"years old, you can enter and you are allowed to drink.")
	elif age == "":
		print("Please enter a number.")	
	else:
		print("You are",age,"years old, sorry, you can't enter, little one!")	
else:
	print("Please enter your age.")


# VERSION 2 with slightly refactored conditional logic
age = input("How old are you: ")

#if age is true, then run the code, which means, age will be true if we enter a number, if we enter an empty string,
#then age will be false, because an empty string is false.
if age:
	age = int(age)
	if age >= 21:
	    print("You are good to enter and can drink!")
	elif age >= 18:
	    print("You can enter, but need a wristband!")
	else: 
		print("You can't come in, little one! :(")
else:
	print("Please enter an age!")
