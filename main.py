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
symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_win(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line+1)
    return winnings, winnings_lines


def get_mach_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_mach(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def inp_deposit():
    while True:
        deposit = (input("Enter the amount to deposit : $"))
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount.")
    return deposit


def inp_num_lines():
    while True:
        lines = (
            input("Enter the number of lines to bet [1-" + str(MAX_LINES)+"]"))
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 & lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number.")
        else:
            print("Please enter a valid number.")
    return lines


def get_bet():
    while True:
        bet = (
            input(f"What would you like to BET [{MIN_BET}-{MAX_BET}] on each line : $"))
        if bet.isdigit():
            bet = int(bet)
            if bet >= MIN_BET & bet <= MAX_BET:
                break
            else:
                print("Please enter a valid BET.")
        else:
            print("Please enter a valid BET.")
    return bet


def game(balance):
    lines = inp_num_lines()
    while True:
        bet = get_bet()
        total_bet = lines*bet
        if total_bet > balance:
            print(f"Insufficient balance. Current balance ${balance}.")
        else:
            break
    print(
        f"You are betting ${bet} on {lines} lines. Total amount of bet is ${total_bet}")

    slots = get_mach_spin(ROWS, COLS, symbol_count)
    print_slot_mach(slots)
    winnings, winnings_lines = check_win(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}")
    print(f"You won on lines : ", *winnings_lines)
    return winnings-total_bet


def main():
    balance = inp_deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("Press enter to spin(q to quit)")
        if spin == 'q' or spin == 'Q':
            break
        balance += game(balance)
    print(f"You left with {balance}")


main()
