MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


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
        bet = (input(f"What would you like to BET [{MIN_BET}-{MAX_BET}] on each line : $"))
        if bet.isdigit():
            bet = int(bet)
            if bet >= MIN_BET & bet <= MAX_BET:
                break
            else:
                print("Please enter a valid BET.")
        else:
            print("Please enter a valid BET.")
    return bet


def main():
    balance = inp_deposit()
    lines = inp_num_lines()
    while True:
        bet = get_bet()
        total_bet = lines*bet
        if total_bet > balance:
            print(f"Insufficient balance. Current balance ${balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total amount of bet is ${total_bet}")
main()
