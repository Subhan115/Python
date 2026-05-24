import random
import sys
import time

# --- Helper Functions for Mobile Game Feel ---
def type_effect(text, speed=0.02):
    """Prints text with a smooth typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def draw_line():
    print("\n" + "=" * 50)

def display_intro():
    print("\n" + "*" * 50)
    print("         GUESS THE NUMBER: ARCADE EDITION        ")
    print("*" * 50)
    draw_line()

def display_outro(player_name):
    draw_line()
    print("*" * 50)
    print("                    GAME OVER                    ")
    print("*" * 50)
    type_effect(f"\nThanks for playing, {player_name}! GG!\n", 0.04)

def show_rules():
    print("\n=================== HOW TO PLAY ===================")
    print(" -> The system will think of a secret number between 1 and 100.")
    print(" -> Your job is to guess it! You have special power-up guesses:\n")
    print("    [🥈 SILVER GUESS] : Gives a hint within 1 to 10 digits of the answer.")
    print("    [🥇 GOLDEN GUESS] : Gives a hint exactly 5 digits away from the answer.")
    print("    [💎 DIAMOND GUESS]: Gives a hint exactly 3 digits away from the answer.")
    print("\n *Note: Power-up hints can be higher or lower than the actual target!*")
    print("\n -> SURVIVAL MODE: Strict allocation! 1 Silver, 1 Golden, 1 Diamond per round.")
    print(" -> CREATIVE MODE: You hack the game and choose your own inventory numbers!")
    print("===================================================")

# --- Core Game Mechanics ---
def generate_hint(secret, tier):
    """Calculates the special hint value based on the power-up tier."""
    if tier == "silver":
        offset = random.randint(1, 10)
    elif tier == "golden":
        offset = 5
    else:  # diamond
        offset = 3
        
    direction = random.choice([-1, 1])
    hint_val = secret + (offset * direction)
    return max(1, hint_val)

def play_round(round_num, inventory):
    secret_number = random.randint(1, 100)
    attempts = 0
    
    # Track active hints for the current round
    active_hints = {"silver": "None", "golden": "None", "diamond": "None"}
    
    print(f"\n*** ROUND {round_num} ***")
    type_effect("The secret number has been calibrated between 1 and 100...")
    
    inv = inventory.copy()
    
    while True:
        # Display status information closely packed
        print(f"\n[Attempts: {attempts}] | Inventory -> Silver: {inv['silver']} | Golden: {inv['golden']} | Diamond: {inv['diamond']}")
        print(f"[Active Hints]    -> Silver: {active_hints['silver']} | Golden: {active_hints['golden']} | Diamond: {active_hints['diamond']}")
              
        choice = input(" -> Enter guess or item name:\n >>> ").strip().lower()
        
        # Handle Power-up activations
        if choice in ['silver', 'golden', 'diamond']:
            if inv[choice] > 0:
                inv[choice] -= 1
                hint = generate_hint(secret_number, choice)
                active_hints[choice] = str(hint)
                print(f">> SCAN ACTIVATED: New {choice} reading logged at: {hint}")
            else:
                print(f"X Out of ammo for {choice} hints!")
            continue
            
        # Handle regular numeric guess
        try:
            guess = int(choice)
        except ValueError:
            print("X Invalid input! Enter a number or a valid power-up name.")
            continue
            
        attempts += 1
        
        if guess == secret_number:
            print(f"\n** SUCCESS! You found the number {secret_number} in {attempts} tries! **")
            return True
        elif guess < secret_number:
            print("▲ TOO LOW! Try aiming higher.")
        else:
            print("▼ TOO HIGH! Try aiming lower.")

# --- Main Game Flow ---
def main():
    display_intro()
    
    player_name = input("Enter your Arcade Call-Sign (Name):\n >>> ").strip()
    if not player_name:
        player_name = "Player 1"
        
    print(f"\nWelcome to the grid, {player_name}!")
    
    rules_choice = input("Would you like to read the game protocols? (y/n):\n >>> ").strip().lower()
    if rules_choice in ['y', 'yes']:
        show_rules()
        
    print("\nSelect Game Mode:")
    print(" 1) Survival Mode (1 Silver, 1 Golden, 1 Diamond)")
    print(" 2) Creative Mode (Custom Inventory Rules)")
    
    mode = ""
    while mode not in ['1', '2']:
        mode = input("Select Mode (1 or 2):\n >>> ").strip()
        
    inventory = {"silver": 1, "golden": 1, "diamond": 1}
    
    if mode == '2':
        print("\n[CREATIVE MODE ACTIVATED] - Configure your cheats:")
        while True:
            try:
                inventory["silver"] = int(input(" Set number of Silver Guesses:\n >>> "))
                inventory["golden"] = int(input(" Set number of Golden Guesses:\n >>> "))
                inventory["diamond"] = int(input(" Set number of Diamond Guesses:\n >>> "))
                break
            except ValueError:
                print("X Please input valid integers for configuration.\n")

    print("\nSelect Match Duration (Options: 1, 3, 5, or 7):")
    total_rounds = 0
    while total_rounds not in [1, 3, 5, 7]:
        try:
            total_rounds = int(input("Choose number of rounds:\n >>> "))
        except ValueError:
            pass
            
    print("\n🚀 Initializing System. Prepare Yourself! 🚀")
    draw_line()
    time.sleep(1)
    
    for r in range(1, total_rounds + 1):
        play_round(r, inventory)
        
        if r == total_rounds:
            print("\nYou have completed all selected rounds!")
            break
            
        next_action = input("\nRound complete! Press [Enter] for next round, or type 'quit' to exit:\n >>> ").strip().lower()
        if next_action in ['quit', 'q', 'exit']:
            print(f"\nExiting match early after round {r}...")
            break
        else:
            draw_line()
            
    display_outro(player_name)

if __name__ == "__main__":
    main()
