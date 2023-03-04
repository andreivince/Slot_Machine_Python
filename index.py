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

def get_slot_machine_spin(rows, cols, symbols):
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

def print_slot_machine(columns): # Transposing a dataset means swapping its rows and columns so that the rows become columns and the columns become rows
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], " | ")
            else:
                print(column[row])

                
        
        
        
# Function to take deposit

def deposit():
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

# Main Function 
def main():
    balance = deposit() # Transforming all the functions to variables
    lines = get_number_of_lines()
    
    # Deposit need to be > than bet
    while True: 
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("You don't have enough money")
        else: 
            break
    # Deposit need to be > than bet
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
main()