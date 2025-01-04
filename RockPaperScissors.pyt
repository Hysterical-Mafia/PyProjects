import random



#Asking User to Start


StartOrStop = input(print("Would You Like to Play Rock,Paper,Scissors? Yes or No?"))

Start_User_Choice = StartOrStop

Start_User_Choice = StartOrStop.lower()

#Starting the Game
    
if Start_User_Choice == "yes":
#The LIST of Rock, Paper, Scissors
    values= ["Rock", "Paper", "Scissors"]

#The Inputs of Rock, Paper, Scissors
    pchoice = input("Choose One of the Following (Rock,Paper,Scissors): "  )
    aichoice = random.choice(values)

#INPUTS to Lowercase
    aichoice = ((aichoice).lower())
    pchoice = ((pchoice).lower())

#Showing the Choices

    print(pchoice)
    print(aichoice)

#Calculations / The Face Offs

    if pchoice == aichoice:
        print("It is a Tie! Both Players have Chosen " + (pchoice))
    elif pchoice == "rock":
        if aichoice == "scissors":
            print("You Win!")
        else:
            print("Computer Wins!")

    elif pchoice == "scissors":
        if aichoice == "paper":
            print("You Win!")
        else:
            print("Computer Wins")

    elif pchoice == "paper":
        if aichoice == "scissors":
            print("Computer Wins!")
        else:
            print("Player Wins!")
else:
    print("Alright then, The game is here if you change your mind!")


