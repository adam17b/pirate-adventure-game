def start_game():
    print("*** Welcome to Curse of the Kraken's Tooth! ***")
    print("You awaken, shipwrecked on an uncharted island...")

    shipwreck_beach()
    # ... we'll add more shortly 

    # ... your existing code ...

def shipwreck_beach():  # Our first location
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
    print("You venture into the dense undergrowth...")

def explore_shore():
    print("You take a walk down the coast towards the shore...")

def player_quit():
    print("Thanks for playing!")
    
        
# (Rest of the code stays the same)
start_game()