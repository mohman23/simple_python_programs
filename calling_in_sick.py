#Calling in Sick
#In this exercise you will be given a few variables that will be set randomly to Boolean values (True  or False ):

#actually_sick  - when you legit have the flu!
#kinda_sick  - you're feeling under the weather and it's enough to treat yoself with a day off if you can spare it
#hate_your_job  - work sucks, I know... 
#You're also given a random number of sick_days between 0 and 10.

#Finally, there is a variable called calling_in_sick  that you must set to True  or False  based on the following scenarios:

#Set to True if: 

#you're actually_sick  and you have sick_days  remaining
#you're kinda_sick  and hate_your_job  and you have sick_days  remaining
#Otherwise, set to False.

actually_sick = None
kinda_sick = None
hate_your_job = None
#sick_days = 0

calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
actually_sick = input("Are you sick? Enter Yes if you are sick, else leave blank. ")
sick_days = input("How many sick leaves do you have left? Enter a number: ")

kinda_sick = input("Are you kinda sick? Enter Yes if you are kind sick, else leave blank. ")
hate_your_job = input("Do you hate your job? Enter Yes if you hate your job, else leave blank. ")

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

sick_days = int(sick_days)
if actually_sick and sick_days > 0:
    calling_in_sick = True
    print("You are sick, please take a leave.")
    exit_if=True

elif kinda_sick and hate_your_job and sick_days > 0:

    calling_in_sick = True
    print("You are kinda sick and you hate your job, so take a sick leave.")

else:
    calling_in_sick = False
    print("Sorry, no sick leave for you.")

label .end


# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#This isn't complete.
#Need to work on this.
