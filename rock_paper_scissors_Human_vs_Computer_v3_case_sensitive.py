#Rock beats scissors but loses to paper.
#Scissors beat paper but loses to rock.
#Paper beats rock, but loses to scissors.

#If both players throw the same object, it’s a tie. 

import random

human_wins = 0
computer_wins = 0
tie = 0



for i in range(3):

	print("Lets play rock, paper, scissors.")

	human = input("You human, please enter your choice, rock, paper or scissors: ").lower()

	computer = random.choice(['rock', 'paper', 'scissors'])

	print("Human chose: ", human)
	print("Computer chose: ", computer)

	if human == "" or computer == "":
		print("Please enter the correct details, you seem to have missed something.")	
	elif human == "rock" and computer == "rock":
		print("Its a tie!")
		tie = tie + 1
	elif human == "scissors" and computer == "scissors":
		print("Its a tie!")
		tie = tie + 1
	elif human == "paper" and computer == "paper":
		print("Its a tie!")	
		tie = tie + 1	
	elif human == "rock":
		if computer == "scissors":
			print("Human wins!")
			human_wins = human_wins + 1
		elif computer == "paper":
			print("Computer wins!")
			computer_wins = computer_wins + 1
		elif computer != "rock" or computer != "scissors" or computer != "paper":
			print("Please enter the correct details, rock, paper or scissors.")	
	elif human == "scissors":
		if computer == "paper":
			print("Human wins!")
			human_wins = human_wins + 1
		elif computer == "rock":
			print("Computer wins!")
			computer_wins = computer_wins + 1
		elif computer != "rock" or computer != "scissors" or computer != "paper":
			print("Please enter the correct details, rock, paper or scissors.")		
	elif human == "paper":
		if computer == "rock":
			print("Human wins!")
			human_wins = human_wins + 1
		elif computer == "scissors":
			print("Computer wins!")
			computer_wins = computer_wins + 1
		elif computer != "rock" or computer != "scissors" or computer != "paper":
			print("Please enter the correct details, rock, paper or scissors.")	
	else:
		print("Please enter the correct details, rock, paper or scissors.")

print("Player1: ", human_wins, "Player2: ", computer_wins, "Tie: ", tie)
	

while True:
	if human_wins > computer_wins:
		print("Human won the tournament!")
	elif computer_wins > human_wins:
		print("Computer won the tournament!")
	elif tie > human_wins:
		print("It's a draw!")
	elif tie > computer_wins:
		print("It's a draw!")		
	elif human_wins == computer_wins:
		print("Its a draw!")
	break		
