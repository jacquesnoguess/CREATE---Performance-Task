balances = {
    'john':100,
    'bob':50
}

def await_action1(name):
    action = input("Welcome back "+name+'. What would you like to do? \n [Withdraw]    [Deposit]    [Check Balance]    [Exit] \n\n')
    if action.lower() == 'withdraw':
        withdraw(balances, name)
    elif action.lower() == 'deposit':
        deposit(balances, name)
    elif action.lower() == 'check balance':
        check_balances(balances,name)
    elif action.lower() == 'exit' or action.lower() == 'quit':
        quit()
    else:
        print('\nAction not recognized. Try again?\n')
        await_action1(name)

def await_action2(name):
    action = input("\nWhat would you like to do? \n [Withdraw]    [Deposit]    [Check Balance]    [Exit] \n\n")
    if action.lower() == 'withdraw':
        withdraw(balances, name)
    elif action.lower() == 'deposit':
        deposit(balances, name)
    elif action.lower() == 'check balance':
        check_balances(balances,name)
    elif action.lower() == 'exit' or action.lower() == 'quit':
        quit()
    else:
        print('\nAction not recognized. Try again?\n')
        await_action2(name)

def create_account(balances):
    name = input("What would you like your name to be: \n").strip()
    while len(name) < 1:
        print("Invalid name. Please try again.")
        create_account(balances)
    else:
        balances.update({name.lower():0})

def deposit(balances, name):
    print("\nYour current balance is "+str(balances[name])+"$")
    amount = int(input('How much would you like to deposit? \n\n'))
    newbalance = balances[name]+amount
    print('\nNew balance: '+str(int(newbalance))+"$")
    balances.update({name:newbalance})    
    await_action2(name)

def withdraw(balances, name):
    print("\nYour current balance is "+str(balances[name])+"$")
    amount = int(input('How much would you like to withdraw? \n\n'))
    if amount > balances[name]:
        print("\nError: this account doesn't have that much money. Please try again.")
        withdraw(balances,name)
    else:
        newbalance = balances[name]-amount
        balances.update({name:newbalance})
        print('\nNew balance: '+str(int(newbalance))+"$")
        await_action2(name)


def check_balances(balances,name):
    print("\nYour balance is "+str(balances[name])+"$")
    await_action2(name)

def main():
    while True:
        name = input('Welcome. Enter your account name: ')
        if name.lower() in balances:
            await_action1(name)
        else:
            yn = input('Name not found in database. Would you like to create an account?\n[Yes]    [No]\n')
            if yn.lower() == 'yes' or 'y':
                create_account(balances)
            if yn.lower() == 'no' or 'n':
                main()


main()
