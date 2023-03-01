MAX_LINES = 3 # It's used all capslock when variable is constant and not gonna change
MAX_BET = 300
MIN_BET = 1

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
    
main()