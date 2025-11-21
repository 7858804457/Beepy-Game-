import random
import time
import keyboard

try:
    import winsound      # For Windows beep sound
except:
    winsound = None      # For Linux/Mac (no winsound)

def beep_sound():
    if winsound:
        winsound.Beep(1000, 300)  # Frequency=1000Hz, Duration=300ms
    else:
        print("\a")  # Cross-platform beep using terminal sound

def beepy_game():
    keys = ['a', 's', 'd', 'f']
    score = 0
    print("\n🎮 Welcome to Beepy Reaction Game!")
    print("Press the key that appears quickly. Game ends on mistake or timeout.")
    print("Ready...? Press ENTER to start!")
    input()

    start_time = time.time()

    while True:
        current_key = random.choice(keys)
        beep_sound()
        print(f"\nPress: {current_key.upper()}")

        start = time.time()

        # Wait for correct key or timeout
        key_pressed = keyboard.read_key()

        reaction_time = time.time() - start

        if key_pressed == current_key and reaction_time <= 2:
            score += 1
            print(f"Correct! 👍 Reaction Time: {round(reaction_time, 2)}s | Score: {score}")
        else:
            print(f"\n❌ Wrong or too slow! You pressed '{key_pressed}' in {round(reaction_time, 2)}s")
            break

    print(f"\n🏁 Game Over! Final Score: {score}")
    print(f"🕒 Total Play Time: {round(time.time() - start_time, 2)} seconds")
    print("Thanks for playing! 🐝")

# Run the game
beepy_game()
