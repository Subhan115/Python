# Guess The Number (Arcade Edition) 🎮

A custom number guessing game built in Python. I made this to practice control flow, loop management, and terminal UI design.

## 🕹️ How the Game Works
The computer picks a secret number from 1 to 100. Instead of just guessing blindly, you have three limited power-ups to help you scan for hints:

- **🥈 Silver Guess:** Gives a rough hint within 10 digits of the answer.
- **🥇 Golden Guess:** Narrows it down to exactly 5 digits away.
- **💎 Diamond Guess:** Highly accurate hint, exactly 3 digits away.

*Note: The hints can be higher or lower than the actual number, so you still have to use logic to figure out the exact target.*

## ⚙️ Game Modes
- **Survival Mode:** You only get 1 of each power-up hint per round. Use them wisely!
- **Creative Mode:** Lets you "hack" the game configurations and set your own starting power-up count.

## 💻 Tech Stack & Features
- **Language:** Python 3
- **Typewriter Effect:** Uses `sys.stdout.flush` to print text smoothly line-by-line for a retro arcade feel.
- **Zero Dependencies:** Uses only standard libraries (`random`, `sys`, `time`), meaning it requires no extra `pip install` commands to run.

---
Developed by Subhan.

