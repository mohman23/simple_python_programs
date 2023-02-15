#Rock beats scissors but loses to paper.
#Scissors beat paper but loses to rock.
#Paper beats rock, but loses to scissors.

#If both players throw the same object, it’s a tie. 

import random

print("Lets play rock, paper, scissors.")

human = input("You human, please enter your choice, rock, paper or scissors: ")

rand_num = random.randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
elif rand_num == 2:
	computer = "scissors"

print("Human chose: ", human)
print("Computer chose: ", computer)

if human == "" or computer == "":
	print("Please enter the correct details, you seem to have missed something.")	
elif human == "rock" and computer == "rock":
	print("Its a tie!")
elif human == "scissors" and computer == "scissors":
	print("Its a tie!")
elif human == "paper" and computer == "paper":
	print("Its a tie!")		
elif human == "rock":
	if computer == "scissors":
		print("Human wins!")
	elif computer == "paper":
		print("Computer wins!")
	elif computer != "rock" or computer != "scissors" or computer != "paper":
		print("Please enter the correct details, rock, paper or scissors.")	
elif human == "scissors":
	if computer == "paper":
		print("Human wins!")
	elif computer == "rock":
		print("Computer wins!")
	elif computer != "rock" or computer != "scissors" or computer != "paper":
		print("Please enter the correct details, rock, paper or scissors.")		
elif human == "paper":
	if computer == "rock":
		print("Human wins!")
	elif computer == "scissors":
		print("Computer wins!")
	elif computer != "rock" or computer != "scissors" or computer != "paper":
		print("Please enter the correct details, rock, paper or scissors.")	
else:
	print("Please enter the correct details, rock, paper or scissors.")
