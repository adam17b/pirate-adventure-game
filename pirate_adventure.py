import random

inventory = []

def start_game():
    print("*** Welcome to Curse of the Kraken's Tooth! ***")
    print("You awaken, shipwrecked on an uncharted island...")

    shipwreck_beach()

def shipwreck_beach(): #First location
    print("*** Shipwreck Beach ***")
    print("----------------------------")   
    print("Broken masts and tattered sails mark your ruined vessel.")
    print("----------------------------") 

    choice = input("What do you do? (Search / Jungle / Shore): ")
    if choice.lower() == "search":
        print("You find a rusty cutlass... could be useful!")
        print("----------------------------")  
    elif choice.lower() == "jungle":
        explore_jungle() 
    elif choice.lower() == "shore":
        explore_shore()
    elif choice.lower() == "quit":
        player_quit()
    else:
        print("Make up your mind, landlubber!")
        print("----------------------------")  

def explore_jungle():
    print("*** Jungle ***")
    print("----------------------------")  
     
    diceRoll = random.randint(1, 10) 

    if diceRoll <= 3:  # Monkey appears
        print("A grumpy monkey blocks your path, chattering angrily!")
        print("----------------------------")   
        choice = input("What do you do? (Try to Befriend / Intimidate / Run Away): ")
        print("----------------------------")  

        if choice.lower() == "befriend":
            print("You cautiously offer it a piece of fruit...")
            print("----------------------------")  
            if diceRoll >= 5:  # Check the initial diceRoll
                print("The monkey has calmed down and offered you an old silver key!")
                print("----------------------------")  
                inventory.append("Old Key")
            else:  # No need for diceRoll check here
                print("The monkey has no interest in being your friend...")
                print("----------------------------")     
        elif choice.lower() == "intimidate":
                print("You roar and wave your arms...")
                print("----------------------------")    # Placeholder 
        elif choice.lower() == "run away":
                print("You turn and flee!")
                print("----------------------------")    # Placeholder 
        else:
                print("The monkey doesn't understand, it just screeches louder!")
                print("----------------------------")   


    # Placeholder for choices - we'll add those next

def explore_shore():
    print("*** Shore ***")
    print("----------------------------")  

    print("You take a walk down the coast towards the shore...")
    print("----------------------------")  


def player_quit():
    print("Thanks for playing!")
    print("----------------------------")  

start_game()