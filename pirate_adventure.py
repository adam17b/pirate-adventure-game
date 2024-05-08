import random

inventory = []

def start_game():
    print("*** Welcome to Curse of the Kraken's Tooth! ***")
    print("You awaken, shipwrecked on an uncharted island...")

    shipwreck_beach()

def shipwreck_beach():  #First location
    print("Broken masts and tattered sails mark your ruined vessel.")

    choice = input("What do you do? (Search / Jungle / Shore): ")
    if choice.lower() == "search":
        print("You find a rusty cutlass... could be useful!") 
    elif choice.lower() == "jungle":
        explore_jungle() 
    elif choice.lower() == "shore":
        explore_shore()
    elif choice.lower() == "quit":
        player_quit()
    else:
        print("Make up your mind, landlubber!") 

def explore_jungle():
     
    diceRoll = random.randint(1, 10) 

    if diceRoll <= 3:  # Monkey appears
        print("A grumpy monkey blocks your path, chattering angrily!") 
        choice = input("What do you do? (Try to Befriend / Intimidate / Run Away): ")

        if choice.lower() == "befriend":
            print("You cautiously offer it a piece of fruit...")
            if diceRoll >= 5:  # Check the initial diceRoll
                print("The monkey has calmed down and offered you an old silver key!")
                inventory.append("Old Key")
            else:  # No need for diceRoll check here
                print("The monkey has no interest in being your friend...")   
        elif choice.lower() == "intimidate":
                print("You roar and wave your arms...")  # Placeholder 
        elif choice.lower() == "run away":
                print("You turn and flee!")  # Placeholder 
        else:
                print("The monkey doesn't understand, it just screeches louder!") 


    # Placeholder for choices - we'll add those next

def explore_shore():
    print("You take a walk down the coast towards the shore...")

def player_quit():
    print("Thanks for playing!")
    
start_game()