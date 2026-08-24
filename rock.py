# ============================================================
#  ROCK PAPER SCISSORS
#  Phase 1 — Game Development Course (Age 10+)
# ============================================================
#
#  CONCEPTS COVERED:
#    - Variables          (player_choice, computer_choice, score)
#    - Lists              (choices = ["rock", "paper", "scissors"])
#    - Input / Output     (input(), print())
#    - Conditions         (if / elif / else — nested)
#    - Loops              (while — play again, game rounds)
#    - Functions          (def — each job has its own function)
#    - Importing modules  (random)
#    - Dictionaries       (win_map — maps what beats what)
#    - String methods     (.lower(), .strip())
#    - f-strings          (formatted output)
# ============================================================

import random   # For the computer's random choice


# ──────────────────────────────────────────────
#  DATA: CHOICES & WIN MAP
#
#  choices — a list of the three valid moves
#  win_map — a dictionary: the key BEATS the value
#             e.g. "rock" beats "scissors"
#
#  TEACHER NOTE: This is a smarter way than writing
#  9 separate if/elif checks for every combination.
#  The dictionary does the heavy lifting for us.
# ──────────────────────────────────────────────
CHOICES = ["rock", "paper", "scissors"]

WIN_MAP = {
    "rock":     "scissors",   # rock beats scissors
    "paper":    "rock",       # paper beats rock
    "scissors": "paper",      # scissors beats paper
}

# Emoji display map — makes the output more fun
EMOJI = {
    "rock":     "🪨 Rock",
    "paper":    "📄 Paper",
    "scissors": "✂️  Scissors",
}


# ──────────────────────────────────────────────
#  FUNCTION: display_welcome
#  Job: Print the game banner
# ──────────────────────────────────────────────
def display_welcome():
    print("=" * 45)
    print("   ✂️   ROCK  PAPER  SCISSORS   🪨")
    print("=" * 45)
    print("Beat the computer. First to 5 wins!")
    print()


# ──────────────────────────────────────────────
#  FUNCTION: get_computer_choice
#  Job: Pick a random choice for the computer
#  Returns: a string — "rock", "paper", or "scissors"
#
#  TEACHER NOTE:
#    random.choice(list) picks one random item
#    from a list. It's the same as randint but
#    for lists instead of numbers.
# ──────────────────────────────────────────────
def get_computer_choice():
    return random.choice(CHOICES)


# ──────────────────────────────────────────────
#  FUNCTION: get_player_choice
#  Job: Ask the player to type their move.
#       Keep asking until they type something valid.
#  Returns: a valid string — "rock", "paper", or "scissors"
#
#  TEACHER NOTE:
#    .lower()  — converts "Rock" or "ROCK" to "rock"
#    .strip()  — removes accidental spaces before/after
#    We check if the result is "in" the CHOICES list
#    using Python's `in` keyword — same as searching a list!
# ──────────────────────────────────────────────
def get_player_choice():
    while True:
        print("Your options: rock | paper | scissors")
        raw = input("Your choice: ")
        choice = raw.strip().lower()   # clean up the input

        if choice in CHOICES:          # search the list
            return choice
        elif choice in ["r", "p", "s"]:   # allow shortcuts
            shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}
            return shortcuts[choice]
        else:
            print(f"  ❌ '{raw}' is not valid. Try again!\n")


# ──────────────────────────────────────────────
#  FUNCTION: determine_winner
#  Job: Decide who won a single round.
#       Uses the WIN_MAP dictionary instead of
#       a long chain of if/elif checks.
#  Parameters:
#    player   — the player's choice (string)
#    computer — the computer's choice (string)
#  Returns: "player", "computer", or "tie"
#
#  TEACHER NOTE:
#    WIN_MAP[player] looks up what the player's
#    choice beats. If that equals the computer's
#    choice, the player wins. Clean and clever!
# ──────────────────────────────────────────────
def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif WIN_MAP[player] == computer:   # player's move beats computer's move
        return "player"
    else:
        return "computer"


# ──────────────────────────────────────────────
#  FUNCTION: display_round_result
#  Job: Print what both players chose and who won
#  Parameters:
#    player, computer — their choices (strings)
#    result           — "player", "computer", or "tie"
# ──────────────────────────────────────────────
def display_round_result(player, computer, result):
    print()
    print(f"  You played:       {EMOJI[player]}")
    print(f"  Computer played:  {EMOJI[computer]}")
    print()

    if result == "tie":
        print("  🤝  It's a tie!")
    elif result == "player":
        print(f"  🎉  You win! {EMOJI[player]} beats {EMOJI[computer]}!")
    else:
        print(f"  💀  Computer wins! {EMOJI[computer]} beats {EMOJI[player]}!")


# ──────────────────────────────────────────────
#  FUNCTION: display_scoreboard
#  Job: Show the current score for both players
#  Parameters:
#    player_score, computer_score — integers
#    target                       — score needed to win
# ──────────────────────────────────────────────
def display_scoreboard(player_score, computer_score, target):
    print()
    print(f"  ── SCORE ── You: {player_score}  |  Computer: {computer_score}  |  First to {target} ──")
    print()


# ──────────────────────────────────────────────
#  FUNCTION: display_bar
#  Job: Show a simple text progress bar for the score
#  TEACHER NOTE: This is a mini algorithm — it uses
#  a loop to build a string character by character.
# ──────────────────────────────────────────────
def display_bar(player_score, computer_score, target):
    player_bar  = "█" * player_score  + "░" * (target - player_score)
    computer_bar = "█" * computer_score + "░" * (target - computer_score)
    print(f"  You      [{player_bar}]  {player_score}/{target}")
    print(f"  Computer [{computer_bar}]  {computer_score}/{target}")


# ──────────────────────────────────────────────
#  FUNCTION: play_round
#  Job: Run a single round — get choices, decide winner,
#       display result, return who won
#  Returns: "player", "computer", or "tie"
# ──────────────────────────────────────────────
def play_round():
    player   = get_player_choice()
    computer = get_computer_choice()
    result   = determine_winner(player, computer)
    display_round_result(player, computer, result)
    return result


# ──────────────────────────────────────────────
#  FUNCTION: play_game
#  Job: Run a full game to a target score (default: 5)
#       Track wins for both players across rounds.
#       End when someone reaches the target.
# ──────────────────────────────────────────────
def play_game(target=5):
    player_score   = 0
    computer_score = 0
    round_number   = 0

    # History list — stores result of every round
    history = []   # e.g. ["player", "tie", "computer", ...]

    while player_score < target and computer_score < target:
        round_number += 1
        print(f"\n{'─' * 45}")
        print(f"  Round {round_number}")
        print(f"{'─' * 45}")

        result = play_round()
        history.append(result)   # record this round in our list

        # Update scores based on result
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
        # Ties don't change the score

        display_bar(player_score, computer_score, target)

    # ── Game over ──
    print(f"\n{'=' * 45}")
    print("  GAME OVER")
    print(f"{'=' * 45}")
    print(f"  Final score — You: {player_score}  |  Computer: {computer_score}")
    print()

    if player_score == target:
        print("  🏆  YOU WIN THE MATCH! Brilliant!")
    else:
        print("  🤖  Computer wins the match! Better luck next time.")

    # Show round-by-round history using a for loop
    print(f"\n  Round history ({len(history)} rounds played):")
    for i, r in enumerate(history):   # enumerate gives index + value
        icon = "✅" if r == "player" else "❌" if r == "computer" else "➖"
        print(f"    Round {i + 1}: {icon} {r.capitalize()}")


# ──────────────────────────────────────────────
#  FUNCTION: choose_target
#  Job: Ask player how many points to play to
#  Returns: an integer (3, 5, or 7)
# ──────────────────────────────────────────────
def choose_target():
    print("Play to how many wins?")
    print("  1 → First to 3")
    print("  2 → First to 5")
    print("  3 → First to 7")

    while True:
        choice = input("Your choice (1/2/3): ").strip()
        if choice == "1": return 3
        elif choice == "2": return 5
        elif choice == "3": return 7
        else: print("Please type 1, 2, or 3.")


# ──────────────────────────────────────────────
#  FUNCTION: main
#  Job: Entry point — welcome, loop for play-again
# ──────────────────────────────────────────────
def main():
    display_welcome()

    while True:
        target = choose_target()
        play_game(target)

        print()
        again = input("Play again? (yes / no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("\nThanks for playing! ✂️ 🪨 📄\n")
            break
        print()


# ──────────────────────────────────────────────
#  ENTRY POINT
# ──────────────────────────────────────────────
if __name__ == "__main__":
    main()