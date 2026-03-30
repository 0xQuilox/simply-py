# ============================================================
#  CLI CALCULATOR
#  Phase 1 Project — Mobile Development Programme
# ============================================================
#  TEACHING NOTES (for the instructor):
#  - Each operation is its own function (Single Responsibility)
#  - get_number() is reused for both inputs (Don't Repeat Yourself)
#  - get_operation() handles menu display AND choice validation
#  - main() controls program flow — it ties everything together
#  - Error handling shows students real-world defensive coding
# ============================================================


# ── OPERATION FUNCTIONS ──────────────────────────────────────
# Each function does ONE job: take two numbers, return a result.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Division by zero is a real error — we return None to signal failure
    if b == 0:
        return None
    return a / b


# ── INPUT FUNCTIONS ──────────────────────────────────────────

def get_number(prompt):
    """
    Ask the user for a number and keep asking until they give a valid one.
    This is called a 'validation loop' — very common in real programs.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("  ⚠  That's not a valid number. Please try again.\n")


def get_operation():
    """
    Display the menu and return the user's choice (1–5).
    Keeps asking until the user picks a valid option.
    """
    print()
    print("  Select an operation:")
    print("  ┌─────────────────────┐")
    print("  │  1.  Addition   (+) │")
    print("  │  2.  Subtraction(-) │")
    print("  │  3.  Multiply   (*) │")
    print("  │  4.  Divide     (/) │")
    print("  │  5.  Quit           │")
    print("  └─────────────────────┘")

    valid_choices = ["1", "2", "3", "4", "5"]

    while True:
        choice = input("  Enter choice (1-5): ").strip()
        if choice in valid_choices:
            return choice
        print("  ⚠  Please enter a number between 1 and 5.\n")


def display_result(a, operator, b, result):
    """
    Format and print the result in a clear, readable way.
    Keeps display logic separate from calculation logic.
    """
    # Format numbers: show as int if they have no decimal part (e.g. 5.0 → 5)
    def fmt(n):
        return int(n) if n == int(n) else round(n, 6)

    print()
    print(f"  ┌─────────────────────────────┐")
    print(f"  │  {fmt(a)} {operator} {fmt(b)} = {fmt(result)}")
    print(f"  └─────────────────────────────┘")


# ── MAIN PROGRAM ─────────────────────────────────────────────

def main():
    """
    Controls the overall flow of the program.
    This is the only function that calls all the others.
    """
    print()
    print("  ╔═══════════════════════════╗")
    print("  ║     CLI CALCULATOR        ║")
    print("  ║   Phase 1 — Python        ║")
    print("  ╚═══════════════════════════╝")

    # Keep running until the user chooses to quit
    while True:

        choice = get_operation()

        # Exit the program
        if choice == "5":
            print()
            print("  Goodbye! Keep coding. 👋")
            print()
            break

        # Get the two numbers from the user
        a = get_number("\n  Enter first number:  ")
        b = get_number("  Enter second number: ")

        # Perform the chosen operation
        if choice == "1":
            result = add(a, b)
            display_result(a, "+", b, result)

        elif choice == "2":
            result = subtract(a, b)
            display_result(a, "-", b, result)

        elif choice == "3":
            result = multiply(a, b)
            display_result(a, "*", b, result)

        elif choice == "4":
            result = divide(a, b)
            if result is None:
                print()
                print("  ⚠  Error: You can't divide by zero!")
            else:
                display_result(a, "/", b, result)

        # Ask if they want to do another calculation
        print()
        again = input("  Calculate again? (y/n): ").strip().lower()
        if again != "y":
            print()
            print("  Goodbye! Keep coding. 👋")
            print()
            break


# ── ENTRY POINT ──────────────────────────────────────────────
# This is standard Python — only run main() if this file is run directly,
# not if it is imported by another file.

if __name__ == "__main__":
    main()
