import random
import time

# 1. Introduction and Name
print("Welcome to Snake Water Gun Game.")
print("It's a modified version of the classic Rock, Paper and\nScissor game.")
Name = input("Enter your name: ")

# 2. Score system initialization
User_Score = 0
Computer_Score = 0

# 3. Rules logic
Rules_Text = """
--------------------------------------------------
                GAME RULES
--------------------------------------------------
1. Snake vs. Water: Snake drinks Water. 
   -> Snake WINS!

2. Water vs. Gun: Water douses the Gun. 
   -> Water WINS!

3. Gun vs. Snake: Gun kills the Snake. 
   -> Gun WINS!

4. If both choose the same, it's a DRAW!
--------------------------------------------------
"""

# Rules Choice Loop
while True:
    Rules_Choice = input(f"{Name}, Would you like to read the rules (yes/no): ").lower()
    if Rules_Choice == "yes":
        print(Rules_Text)
        break
    elif Rules_Choice == "no":
        print("Ok, you may continue.")
        break
    else:
        print(f"Invalid choice '{Rules_Choice}'. Select again.")

# 4. Round Selection
while True:
    try:
        Total_Rounds = int(input(f"\nHow many rounds do you want to play? (1, 3, 5, 7): "))
        if Total_Rounds in [1, 3, 5, 7]:
            break
        else:
            print("Please choose specifically from 1, 3, 5, or 7.")
    except ValueError:
        print("Invalid input! Please enter a number.")

# 5. Difficulty Selection
while True:
    
    Difficulty_Input = input(f"\nSelect Difficulty - (F)air / (M)edium or (H)ard: ").upper()
    
    
    if Difficulty_Input in ["F", "FAIR", "M", "MEDIUM"]:
        Difficulty = "M"  
        print("Difficulty set to Fair/Medium. The game is balanced!")
        break
    elif Difficulty_Input in ["H", "HARD"]:
        Difficulty = "H"
        print("Difficulty set to Hard. The computer is watching your patterns...")
        break
    else:
        print("Invalid choice! Please type 'Fair' or 'Hard'.")

print(f"\n--- Game Started: Best of {Total_Rounds} ---")

# 6. Core Game Loop
for Round_Num in range(1, Total_Rounds + 1):
    print(f"\n--- Round {Round_Num} of {Total_Rounds} ---")
    
    User_Input = input("Choose (S)nake, (W)ater, or (G)un: ").upper()
    
    if User_Input == "S": User_Choice = "Snake"
    elif User_Input == "W": User_Choice = "Water"
    elif User_Input == "G": User_Choice = "Gun"
    else:
        print("Invalid choice! Computer gets a point for your mistake.")
        User_Choice = "Invalid"

    # Suspense System
    if User_Choice != "Invalid":
        print("Computer is thinking...")
        time.sleep(1)
        print("Analyzing your move...")
        time.sleep(1)

    # Difficulty Logic
    Options = ["Snake", "Water", "Gun"]
    if Difficulty == "H" and User_Choice != "Invalid":

        if random.random() < 0.40:
            if User_Choice == "Snake": Computer_Choice = "Gun"
            elif User_Choice == "Water": Computer_Choice = "Snake"
            elif User_Choice == "Gun": Computer_Choice = "Water"
        else:
            Computer_Choice = random.choice(Options)
    else:
        Computer_Choice = random.choice(Options)

    print(f"Computer chose: {Computer_Choice}!")

    # Comparison Logic
    if User_Choice == Computer_Choice:
        print("It's a Draw! (No points awarded)")
    elif (User_Choice == "Snake" and Computer_Choice == "Water") or \
         (User_Choice == "Water" and Computer_Choice == "Gun") or \
         (User_Choice == "Gun" and Computer_Choice == "Snake"):
        print(f"Round {Round_Num} goes to {Name}!")
        User_Score += 1
    else:
        print(f"Round {Round_Num} goes to Computer!")
        Computer_Score += 1

    print(f"Current Score -> {Name}: {User_Score} | Computer: {Computer_Score}")

# 7. Final Match Result
print("\n" + "="*35)
print("        FINAL MATCH RESULT       ")
print("="*35)
print(f"{Name}'s Total Score: {User_Score}")
print(f"Computer's Total Score: {Computer_Score}")
print("-" * 35)

if User_Score > Computer_Score:
    print(f"RESULT: CONGRATULATIONS {Name.upper()}! YOU WON! 🏆")
    if Difficulty == "H":
        print("Incredible! You beat the computer on Hard mode!")
elif Computer_Score > User_Score:
    print("RESULT: COMPUTER WON! Better luck next time. 🤖")
else:
    print("RESULT: THE MATCH IS A TIE! 🤝")

print("="*35)
print("Allah Hafiz! Thanks for playing.")
