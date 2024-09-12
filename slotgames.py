import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def deposit():
    while True:
        amount = input("Enter the amount of money you want to deposit in $: ")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter an amount above zero.")
        else:
            print("Enter a valid amount.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines you want to bet on (1-{MAX_LINES}): ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Enter valid digits.")

    return lines


def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? (min: ${MIN_BET}, max: ${MAX_BET}): ")

        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Enter an amount within ${MIN_BET} --- ${MAX_BET}.")
        else:
            print("Enter a valid amount.")


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for key, value in symbols.items():  # Fixed 'item()' to 'items()'
        for _ in range(value): 
            all_symbols.append(key)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)  # Fixed 'appened' to 'append'

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def check_winnings(columns, lines, bet, values):
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
            winning_lines.append(line + 1)
    return winnings, winning_lines  # Return both winnings and winning lines


def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        else:
            print(f"You don't have enough balance to bet that amount. Your current balance is ${balance}.")

    print(f"You are betting ${bet} on {lines} line(s), and your total bet is: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings} on line(s): {', '.join(map(str, winning_lines))}.")

    balance += winnings - total_bet  # Update the balance after the bet
    return balance


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        spin = input("Press Enter to spin or 'q' to quit: ")
        if spin == 'q':
            break
        balance = game(balance)  # Pass the balance to the game and update it

    print(f"You left the game with ${balance}.")


main()
