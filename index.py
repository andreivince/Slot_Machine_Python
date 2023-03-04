import random # Random

MAX_LINES = 3 # It's used all capslock when variable is constant and not gonna change
MAX_BET = 300
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = { # Frequency of symbols
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = { # Value of symbols
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    """
    This function takes the columns of the slot machine, the number of lines being played, the bet amount, and a
    dictionary that maps symbols to their values. It returns the amount of winnings and the lines on which the
    player won.
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    """
    This function takes the number of rows and columns in the slot machine, and a dictionary that maps symbols to
    their frequency. It returns a list of columns, each of which is a list of symbols.
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # Copy of all_symbols # Make sure to have [:] to create a copy
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value) # Insert value to column

        columns.append(column)

    return columns

def print_slot_machine(columns):
    """
    This function takes a list of columns, each of which is a list of symbols. It prints out the symbols arranged in
    rows and columns, with a separator between each symbol.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

# Function to take deposit

def deposit():
    """
    This function prompts the user to enter a deposit amount and returns that amount as an integer.
    """
    while True: # Loop
        amount = input("Deposit $: ") # Input asking for deposit
        if amount.isdigit(): # Check if it's a number
            amount = int(amount) # Transforming amount string to int
            if amount > 0: # Deposit can't be 0 or less
                break # Break Loop
            else:
                print("Should be greater than 0")
        else:
            print("Enter a valid number")

    return amount

# Function to take number of lines

def get_number_of_lines():
    """
    This function prompts the user to enter the number of lines they want to play and returns that number as an integer.
    """
    while True:
        lines = input("Choose number of lines: (1 to " + str(MAX_LINES) + ") ") # One way to concatenate
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: # Check if the value is between these two values
                break
            else:
                print("Enter a valid number")
        else:
            print("Enter a number")
    return lines

# Function to take bet

def get_bet():
    """
    This function prompts the user to enter a bet amount and returns that amount as an integer.
    """
    while True:
        bet = input(f"What you would like to bet: ({MIN_BET} to {MAX_BET})") # Insert variables
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET: # Check if the value is between these two values
                break
            else:
                print(f"Amount must be ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Enter a number")
    return bet

def spin(balance):
    """
    This function takes the player's balance as a parameter and returns the amount of winnings or losses from the spin.
    """
    lines = get_number_of_lines()

    # Deposit needs to be > than bet
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("You don't have enough money")
        else:
            break
    # Deposit needs to be > than bet

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won!! ${winnings}!")
    print(f"You won on lines: {winning_lines}")
    return winnings - total_bet

# Main Function
def main():
    """
    This function is the main function of the program. It prompts the user to enter a deposit amount, and then allows
    them to play the slot machine until they choose to quit.
    """
    balance = deposit() # Transforming all the functions to variables
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (Q to quit)")
        if answer.lower() == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

main()
