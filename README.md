# Beepy-Game-Project

🎯 Beepy Reaction Game using Python

A fun and interactive reaction speed game built using Python.
The game plays a beep sound and shows a random key (A, S, D, F).
Your job is to press the correct key quickly (within 2 seconds)!
The game ends when you press the wrong key or are too slow.

🚀 Features

✔ Real-time beep sound alerts
✔ Random key generation (A, S, D, F)
✔ Reaction time measurement
✔ Score tracking system
✔ Game ends on mistake or timeout
✔ Beginner-friendly Python project

🛠️ Technologies Used
Technology	Purpose
Python	Main programming language
random	Random key selection
time	Calculate reaction time
keyboard	Detect user key input
winsound	Beep sound (Windows)
📂 Project Structure
BeepyGame/
│
├── beepy_game.py          # Main game file
├── README.md              # Project documentation
└── requirements.txt       # Required libraries (keyboard)

📥 Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/BeepyGame.git
cd BeepyGame

2️⃣ Install Required Library
pip install keyboard


(winsound works only on Windows; macOS/Linux users get terminal beep \a)

▶️ How to Run the Game
python beepy_game.py

🎮 Game Rules
Action	Result
Press the correct key within 2 seconds	👍 Score +1
Press the wrong key or take too long	❌ Game Over
Keys used in game	A, S, D, F
Start game	Press ENTER
💻 Sample Code Snippet
import random
import time
import keyboard

def beep_sound():
    print('\a')  # Cross-platform beep

def beepy_game():
    keys = ['a', 's', 'd', 'f']
    score = 0

    print("\n🎮 Welcome to Beepy Game! Press ENTER to start.")
    input()

    while True:
        current_key = random.choice(keys)
        beep_sound()
        print(f"\nPress: {current_key.upper()}")

        start = time.time()
        key_pressed = keyboard.read_key()
        reaction_time = time.time() - start

        if key_pressed == current_key and reaction_time <= 2:
            score += 1
            print(f"Correct! 👍 Time: {round(reaction_time, 2)}s | Score: {score}")
        else:
            print(f"\n❌ Wrong or too slow! You pressed '{key_pressed}'")
            break

    print(f"\n🏁 Final Score: {score}")

🧠 Concepts Learned
Concept	Explanation
Randomization	Chooses random keys
Time Measurement	Tracks reaction time
Keyboard Event	Capturing key press
Game Loop	Runs until user fails
Conditional Logic	Correct/Incorrect input
🌟 Future Enhancements

🚀 Add GUI using Tkinter or Pygame
📊 Display high score history (CSV)
🎵 Add custom sounds for correct/wrong answers
🧑‍🤝‍🧑 Multiplayer challenge mode
📱 Convert to Android or EXE version

📝 License

This project is open-source under the MIT License.
Feel free to use, modify, and improve!

🙌 Acknowledgements

Inspired by simple reaction-based console games.
Built using Python standard libraries.
