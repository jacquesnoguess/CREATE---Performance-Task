balances = {
    'John':100,
    'Bob':50
}

def deposit():
    pass

def withdraw():
    print('dawg')

def check_balances():
    pass

def main():
    while True:
        name = input('Welcome. Enter your account name: ')
        if name in balances:
            action = input("Welcome back "+name+'. What would you like to do? \n [Withdraw]    [Deposit]    [Check Balance] \n\n')
            if action.lower() == 'withdraw':
                print('yeah')
            elif action.lower() == 'deposit':
                print('awesome')
            elif action.lower() == 'check balance':
                print('ah')
            else:
                input('Action not recognized. Try again?')
        else:
            print('no')

main()
