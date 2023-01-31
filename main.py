MAX_LINES = 3


def inp_deposit():
    while True:
        deposit = (input("\nEnter the amount to deposit : $"))
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
        deposit = (input("\nEnter the amount to deposit : $"))
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount.")
    return deposit


def main():
    balance = inp_deposit()
