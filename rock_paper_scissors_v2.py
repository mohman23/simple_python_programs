#Rock beats scissors but loses to paper.
#Scissors beat paper but loses to rock.
#Paper beats rock, but loses to scissors.

#If both players throw the same object, it’s a tie.

print("Lets play rock, paper, scissors.")

player1 = input("Enter player1's choice: ")
player2 = input("Enter player2's choice: ")

if player1 == "" or player2 == "":
	print("Please enter the correct details, you seem to have missed something.")	
elif player1 == "rock" and player2 == "rock":
	print("Its a tie!")
elif player1 == "scissors" and player2 == "scissors":
	print("Its a tie!")
elif player1 == "paper" and player2 == "paper":
	print("Its a tie!")		
elif player1 == "rock":
	if player2 == "scissors":
		print("Player1 wins!")
	elif player2 == "paper":
		print("Player2 wins!")
	elif player2 != "rock" or player2 != "scissors" or player2 != "paper":
		print("Please enter the correct details, rock, paper or scissors.")	
elif player1 == "scissors":
	if player2 == "paper":
		print("Player1 wins!")
	elif player2 == "rock":
		print("Player2 wins")
	elif player2 != "rock" or player2 != "scissors" or player2 != "paper":
		print("Please enter the correct details, rock, paper or scissors.")		
elif player1 == "paper":
	if player2 == "rock":
		print("Player1 wins")
	elif player2 == "scissors":
		print("Player2 wins")
	elif player2 != "rock" or player2 != "scissors" or player2 != "paper":
		print("Please enter the correct details, rock, paper or scissors.")	
else:
	print("Please enter the correct details, rock, paper or scissors.")
