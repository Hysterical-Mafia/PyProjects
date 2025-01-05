#Dice Rolling Sim
import random
#Ask user how many dice to roll
player_dice_roll = int(input("How many dice would you like to roll?"))

    #def a function for this
def dice_sim():
    i = 0
    #create a while loop,
    while i < player_dice_roll:
        roll = random.randint(1,6)
        #print the roll along with the sequence that the roll came in
        print(f"Roll {i+1}: {roll}")
        i = i + 1 

dice_sim()
    