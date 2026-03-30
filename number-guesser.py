# ============================================================
#  GUESS THE NUMBER GAME
#  Phase 1 — Game Development Course (Age 10+)
# ============================================================
#
#  CONCEPTS COVERED:
#    - Variables          (secret_number, guess, attempts)
#    - Input / Output     (input(), print())
#    - Conditions         (if / elif / else)
#    - Loops              (while)
#    - Functions          (def)
#    - Debugging          (try / except for bad input)
#    - Lists (bonus)      (history list to track guesses)
#    - Import / modules   (random)
# ============================================================

import random   # We import the random module so Python can pick a surprise number

# ──────────────────────────────────────────────
#  FUNCTION: display_welcome
#  Job: Print a welcome banner when the game starts
# ──────────────────────────────────────────────
def display_welcome():
    print("=" * 40)
    print("   🎮  GUESS THE NUMBER GAME  🎮")
    print("=" * 40)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?\n")


# ──────────────────────────────────────────────
#  FUNCTION: get_difficulty
#  Job: Ask the player to choose a difficulty level
#  Returns: the maximum number of attempts allowed
# ──────────────────────────────────────────────
def get_difficulty():
    print("Choose a difficulty:")
    print("  1 - Easy   (15 attempts)")
    print("  2 - Medium (10 attempts)")
    print("  3 - Hard   ( 5 attempts)")

    while True:                          # Keep asking until we get a valid answer
        choice = input("\nYour choice (1/2/3): ")

        if choice == "1":
            print("Easy mode — good luck!\n")
            return 15
        elif choice == "2":
            print("Medium mode — you've got this!\n")
            return 10
        elif choice == "3":
            print("Hard mode — brave choice!\n")
            return 5
        else:
            print("Please type 1, 2, or 3.")   # Handles unexpected input


# ──────────────────────────────────────────────
#  FUNCTION: get_player_guess
#  Job: Ask the player to type a number.
#       Handles the case where they type letters by accident.
#  Returns: a valid integer guess
# ──────────────────────────────────────────────
def get_player_guess():
    while True:
        raw = input("Your guess: ")

        try:                             # "try" to convert the input to a number
            guess = int(raw)             # int() converts text → integer
            if 1 <= guess <= 100:        # Make sure it's in the valid range
                return guess
            else:
                print("Please guess a number between 1 and 100.")
        except ValueError:               # If int() fails (e.g. player typed "abc")
            print("That doesn't look like a number — try again!")


# ──────────────────────────────────────────────
#  FUNCTION: give_hint
#  Job: Tell the player whether their guess is too high, too low, or correct.
#       Also gives a "warm/cold" hint based on how close they are.
#  Parameters:
#    guess         — what the player guessed
#    secret_number — the number we're hiding
#  Returns: True if the player guessed correctly, False otherwise
# ──────────────────────────────────────────────
def give_hint(guess, secret_number):
    difference = abs(guess - secret_number)   # abs() gives the positive distance

    # First: is it correct?
    if guess == secret_number:
        return True   # Correct! Signal to the game loop that we're done.

    # Second: too high or too low?
    if guess < secret_number:
        direction = "Too low! ⬆"
    else:
        direction = "Too high! ⬇"

    # Third: warm/cold hint based on how close they are
    if difference <= 5:
        temperature = "🔥 You're burning hot!"
    elif difference <= 15:
        temperature = "☀️  Getting warm..."
    elif difference <= 30:
        temperature = "❄️  Cold..."
    else:
        temperature = "🧊 Freezing cold!"

    print(f"  {direction}  {temperature}")
    return False   # Not correct yet


# ──────────────────────────────────────────────
#  FUNCTION: display_history
#  Job: Show all previous guesses so the player can see their pattern
#  Parameters:
#    history — a list of numbers the player has guessed so far
# ──────────────────────────────────────────────
def display_history(history):
    if len(history) > 1:                 # Only show history if there's more than one guess
        print(f"  Previous guesses: {history}")


# ──────────────────────────────────────────────
#  FUNCTION: calculate_score
#  Job: Give the player a score based on how few attempts they used
#  Parameters:
#    attempts_used  — how many guesses it took
#    max_attempts   — the maximum allowed for this difficulty
#  Returns: an integer score
# ──────────────────────────────────────────────
def calculate_score(attempts_used, max_attempts):
    # More attempts remaining = higher score
    remaining = max_attempts - attempts_used
    score = (remaining + 1) * 100
    return score


# ──────────────────────────────────────────────
#  FUNCTION: play_game
#  Job: Run one full round of the game
#       This is the main game loop — it ties everything together
# ──────────────────────────────────────────────
def play_game():
    # STEP 1: Pick a secret number using the random module
    secret_number = random.randint(1, 100)   # randint picks a random integer

    # STEP 2: Set up game variables
    max_attempts = get_difficulty()
    attempts_used = 0
    history = []     # An empty list — we'll add each guess to this

    # STEP 3: The main game loop
    while attempts_used < max_attempts:
        attempts_left = max_attempts - attempts_used
        print(f"\nAttempts left: {attempts_left}")
        display_history(history)

        # Get the player's guess
        guess = get_player_guess()
        attempts_used += 1        # Increment (add 1) to the attempt counter
        history.append(guess)     # Add this guess to our history list

        # Check the guess
        correct = give_hint(guess, secret_number)

        if correct:
            # Player guessed correctly!
            score = calculate_score(attempts_used, max_attempts)
            print(f"\n🎉 CORRECT! The number was {secret_number}!")
            print(f"   You got it in {attempts_used} attempt(s).")
            print(f"   Your score: {score} points")
            return   # Exit the function — game is over

    # If we reach here, the player ran out of attempts
    print(f"\n💀 Game over! You ran out of attempts.")
    print(f"   The secret number was {secret_number}.")
    print(f"   Better luck next time!")


# ──────────────────────────────────────────────
#  FUNCTION: main
#  Job: The entry point — controls the overall flow
#       Asks if the player wants to play again after each round
# ──────────────────────────────────────────────
def main():
    display_welcome()

    while True:   # Outer loop: keeps the game running until player quits
        play_game()

        print("\n" + "-" * 40)
        again = input("Play again? (yes / no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("\nThanks for playing! 👋")
            break   # Exit the outer loop


# ──────────────────────────────────────────────
#  ENTRY POINT
#  This is the standard Python pattern for running a script directly.
#  If this file is imported by another program, main() won't run automatically.
# ──────────────────────────────────────────────
if __name__ == "__main__":
    main()
