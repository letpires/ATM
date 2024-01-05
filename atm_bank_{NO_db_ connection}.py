# ADMIN ACCOUNT: 211001 - Password: 123

# Convention used:
# PascalCase for function names
# camel_case for variables
# -----------------------------


# IMPORTS USED THROUGHOUT THE CODE:
import time
from datetime import datetime
# from datetime import date
import numpy as np

# Visualization
import matplotlib.pyplot as plt


#-------------------------------------
# FUNCTION THAT SHOWS THE OPTIONS MENU:

def DisplayMenu(options):
    """Display a menu with numbered options to the user."""
    
    # Print the menu title
    print("ATM Menu:")

    # Enumerate and display each option with a corresponding number
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")


def AccountBalance(account_logged):
    """It sums all the values in the historic, as the historic includes positive and negative values."""

    hist_transactions = accounts[account_logged]["history"]
    ammount = sum(hist_transactions)

    return ammount


# Initialize a list to store generated transaction numbers
transaction_history = []
def GenerateTransactionNumber(account_logged):
    """Generates a unique transaction number for the account, based on the timestamp, account number, 
    and previous transaction count. """
    

    current_timestamp = int(time.time())
    transaction_number = f'TR-{account_logged}-{current_timestamp}-{len(transaction_history) + 1}'

    # # Verifique se o número de transação é único
    # while transaction_number in transaction_history:
    #     # Se não for único, regenere com um novo contador
    #     transaction_number = f'#TN-{current_timestamp}-{len(transaction_history) + 1}'
    
    # Adicione o número de transação à lista de histórico
    transaction_history.append(transaction_number)
    
    return transaction_number


def Deposit(account_logged):
    """Makes a deposit into a specified account, updating your transaction history, date and type of transaction."""

    hist_transactions = accounts[account_logged]["history"]
    date_transactions = accounts[account_logged]["date_transactions"]
    type_transaction = accounts[account_logged]["type_transaction"]
    number_transaction = accounts[account_logged]["transaction_number"]

    # Prompt user for deposit amount and convert it to float
    deposit = float(input("How much do you want to deposit?: "))

    # Add deposit to transaction history
    hist_transactions.append(deposit)

    #current_date = date.today() # Just get the date
    # Get current date and time and format it
    current_date = datetime.now() 
    formatted_date = current_date.strftime("%m/%d/%Y %H:%M:%S")
    date_transactions.append(formatted_date)

    # Add the "Deposited" type to the list of transaction types
    type_transaction.append('Deposited')

    # Using function to generate a unique transaction number
    transaction_number = GenerateTransactionNumber(account_logged)    
    number_transaction.append(transaction_number)


    return hist_transactions, date_transactions, type_transaction


def Withdrawal(account_logged):
    """Make a withdrawal from a specified account, updating your transaction history, date and type of transaction."""

    # Get account information
    hist_transactions = accounts[account_logged]["history"]
    date_transactions = accounts[account_logged]["date_transactions"]
    type_transaction = accounts[account_logged]["type_transaction"]
    number_transaction = accounts[account_logged]["transaction_number"]

    # Ask the user for the withdrawal amount and convert it to float
    withdrawal_amount = float(input("How much do you want to withdraw?: "))

    # Calling 'AccountBalance' function
    ammount = AccountBalance(account_logged)

   
   # Using conditional to check if you have money to withdraw.
    if withdrawal_amount > ammount:
        print("You do not have enough BALANCE to make the withdrawal.")


    elif withdrawal_amount <= 0:
        print("Invalid!")

    else:
        # SUCESSFUL WITHDRAWAL PROCESS

        current_date = datetime.now()  
        # Formatting data to string
        formatted_date = current_date.strftime("%m/%d/%Y %H:%M:%S")

        # Adding the values to the empty list.
        # '-abs' convert value to negative because it is withdrawal.
        hist_transactions.append(-abs(withdrawal_amount)) 
        date_transactions.append(formatted_date)
        type_transaction.append('Withdrew')

        # Generate a unique transaction number
        transaction_number = GenerateTransactionNumber(account_logged)    
        number_transaction.append(transaction_number)

    return hist_transactions, date_transactions, type_transaction


def PlotAccountBalances(accounts, balances):
    """Create a bar chart to display customer account and balances."""

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(accounts, balances, color='skyblue')
    plt.xlabel("Account Names")
    plt.ylabel("Balance")
    plt.title("Customer Account Balances")

    # Rotate the x-axis labels for better readability (optional)
    plt.xticks(rotation=45)

    # Display the plot
    plt.tight_layout()
    plt.show()


def GetOpenAccounts(item):
    """Checks if the 'open' key exists in the item and returns its value, or False if it does not."""

    return dict(item[1]).get("open", False)



#----------
# MAIN CODE
# Define the menu options as a list
MENU_OPTIONS = ["Check Balance", "Deposit", "Withdraw", "Transaction History", "Quit"]
ADMIN_MENU_OPTIONS = ["All open accounts and balance", "All transaction history", "Deposits history" ,
                      "Withdrawls history", "Plot a graph", "Quit"]

account_logged = ""
index_next_account_available = 111001
accounts = {
    # ADMIN ACCOUNT
    "211001": {
        "pin": "123"
    },
    # REGULAR ACCOUNTS
    "111001": {
        "balance": 0,
        "history": [],
        "date_transactions": [],
        "type_transaction": [],
        "transaction_number": [],
        "pin": "123"
    },
    "111002": {
        "balance": 0,
        "history": [],
        "date_transactions": [],
        "type_transaction": [],
        "transaction_number": [],
        "pin": "123"
    },
    "111003": {
        "balance": 0,
        "history": [],
        "date_transactions": [],
        "type_transaction": [],
        "transaction_number": [],
        "pin": "123"
    },
    "111004": {
        "balance": 0,
        "history": [],
        "date_transactions": [],
        "type_transaction": [],
        "transaction_number": [],
        "pin": "123"
    },
    "111005": {
        "balance": 0,
        "history": [],
        "date_transactions": [],
        "type_transaction": [],
        "transaction_number": [],
        "pin": "123"
    },
    "111006": {
        "balance": 0,
        "history": [],
        "date_transactions": [],
        "type_transaction": [],
        "transaction_number": [],
        "pin": "123"
    },
    "111007": {
        "balance": 0,
        "history": [],
        "date_transactions": [],
        "type_transaction": [],
        "transaction_number": [],
        "pin": "123"
    },
    "111008": {
        "balance": 0,
        "history": [],
        "date_transactions": [],
        "type_transaction": [],
        "transaction_number": [],
        "pin": "123"
    },
    "111009": {
        "balance": 0,
        "history": [],
        "date_transactions": [],
        "type_transaction": [],
        "transaction_number": [],
        "pin": "123"
    },
    "111010": {
        "balance": 0,
        "history": [],
        "date_transactions": [],
        "type_transaction": [],
        "transaction_number": [],
        "pin": "123"
    },
}



while True:
    while True:

        choice = input("Welcome. Do you have an account with us (Y) or are you a new customer (N) ?")

        # Check if the user has an existing account or is a new customer.
        if choice == 'Y':
            account_number = input("Please enter your valid 6-digit account number")
            pin_number = input("Please enter your 4-digit pin number")

            if accounts[account_number]["pin"] == pin_number:
                account_logged = account_number
                break

        # Condition for new customer.
        if choice == 'N':
            choice2 = input("Would you like to open an account with us? (Y/N)")
            
            if choice2 == 'Y':
                account_logged = str(index_next_account_available)
                index_next_account_available = index_next_account_available + 1
                print("Your 6 digit account number is: $", account_logged)
                print("Your 4 digit PIN number i: $", accounts[account_logged]["pin"])
                accounts[account_logged]["open"] = True
                break
            
            elif choice2 == 'N':
                print("Thank you and have a nice day. Goodbye.")

    # If the user account is equal to 211001, the bank administration is acessed.
    if account_logged == "211001":
        while True:

            # ADMIN MENU.
            DisplayMenu(ADMIN_MENU_OPTIONS)

            # User input
            choice = input("Please select an option: ")

            # Conditional code depending on the menu option the user chooses.
            if choice == '1':
                # Filter open accounts using the 'GetOpenAccounts' function
                open_accounts = filter(lambda item: GetOpenAccounts(item), accounts.items())

                # Iterate over the filtered accounts and display the balance of each one
                for item in list(open_accounts):
                    amount = AccountBalance(item[0])
                    print(f"Account {item[0]} balance is: ${amount}")

            elif choice == '2':
                open_accounts = filter(lambda item: GetOpenAccounts(item), accounts.items())
                print("Transaction History:")
                for item in list(open_accounts):

                    hist_transactions = accounts[item[0]]["history"]
                    date_transactions = accounts[item[0]]["date_transactions"]
                    type_transaction = accounts[item[0]]["type_transaction"]
                    number_transaction = accounts[item[0]]["transaction_number"]

                    if len(hist_transactions) > 0:
                        
                        print(f'Account number: {item[0]}') #Print account number for identification
                        for i in range(len(hist_transactions)):
                            print(date_transactions[i], number_transaction[i], type_transaction[i], f'${hist_transactions[i]}')

                    else:
                        print("You have no transactions yet!")

            elif choice == '3':
                open_accounts = filter(lambda item: GetOpenAccounts(item), accounts.items())
                open_accounts_list = list(open_accounts)
                deposits = []
                accounts_code = []
                dates = []
                numbers = []

                # print(open_accounts_list)
                #Printa número da conta do primeiro - proximo open_Accounts_list[1][0]
                #print(open_accounts_list[0][0]) 
                # print(open_accounts_list[0][1]['type_transaction'])

                if len(open_accounts_list) == 0:
                    print("You have no open account yet!")
                
                else:
                    for item in range(len(open_accounts_list)):
                        account_transactions = open_accounts_list[item][0]
                        hist_transactions = open_accounts_list[item][1]["history"]
                        date_transactions = open_accounts_list[item][1]["date_transactions"]
                        type_transaction = open_accounts_list[item][1]["type_transaction"]
                        number_transaction = open_accounts_list[item][1]["transaction_number"]
                 

                        for i in range(len(type_transaction)):
                            if type_transaction[i] == 'Deposited':
                                deposits.append(hist_transactions[i])
                                accounts_code.append(account_transactions)
                                dates.append(date_transactions[i])
                                numbers.append(number_transaction[i])

                            elif type_transaction[i] == 'Withdrew':
                                pass

                            else:
                                print("There is no transactions deposited in this account")
                        

                # Use argsort from NUMPY to get the sorted indices of transaction values
                sorted_indices = np.argsort(deposits)

                # Reverse the order of indices to get the order from largest to smallest
                sorted_indices = sorted_indices[::-1]

                # Create ordered lists based on indexes
                sorted_transaction_values = [deposits[i] for i in sorted_indices]
                sorted_account_numbers = [accounts_code[i] for i in sorted_indices]
                sorted_transaction_numbers = [numbers[i] for i in sorted_indices]
                sorted_dates = [dates[i] for i in sorted_indices]


                formatted_transactions = []
                for value, account, number, date in zip(sorted_transaction_values, sorted_account_numbers, sorted_transaction_numbers, sorted_dates):
                    formatted_transaction = f"Account number: {account} Transaction number: {number} Deposit: ${value} Data: {date}"
                    formatted_transactions.append(formatted_transaction)

                # Display formatted strings
                for transaction in formatted_transactions:
                    print(transaction)

            elif choice == '4':
                open_accounts = filter(lambda item: GetOpenAccounts(item), accounts.items())
                open_accounts_list = list(open_accounts)
                withdrew = []
                accounts_code = []
                dates = []
                numbers = []


                if len(open_accounts_list) == 0:
                    print("You have no open account yet!")
                
                else:
                    for item in range(len(open_accounts_list)):
                        account_transactions = open_accounts_list[item][0]
                        hist_transactions = open_accounts_list[item][1]["history"]
                        date_transactions = open_accounts_list[item][1]["date_transactions"]
                        type_transaction = open_accounts_list[item][1]["type_transaction"]
                        number_transaction = open_accounts_list[item][1]["transaction_number"]

                        for i in range(len(type_transaction)):

                            if type_transaction[i] == 'Withdrew':
                                withdrew.append(hist_transactions[i])
                                accounts_code.append(account_transactions)
                                dates.append(date_transactions[i])
                                numbers.append(number_transaction[i])
                            
                            elif type_transaction[i] == 'Deposited':
                                pass

                            else:
                                print("There is no transactions deposited in this account")
                        
                
            
                sorted_indices = np.argsort(withdrew)

                # Reverse the order of indices to get the order from largest to smallest
                sorted_indices = sorted_indices[::-1]

                # Create ordered lists based on indexes
                sorted_transaction_values = [withdrew[i] for i in sorted_indices]
                sorted_account_numbers = [accounts_code[i] for i in sorted_indices]
                sorted_transaction_numbers = [numbers[i] for i in sorted_indices]
                sorted_dates = [dates[i] for i in sorted_indices]


                formatted_transactions = []
                for value, account, number, date in zip(sorted_transaction_values, sorted_account_numbers, sorted_transaction_numbers, sorted_dates):
                    formatted_transaction = f"Account number: {account} Transaction number: {number} Withdrew: ${value} Data: {date}"
                    formatted_transactions.append(formatted_transaction)

                # Display formatted strings
                for transaction in formatted_transactions:
                    print(transaction)


            elif choice == '5':
                open_accounts = filter(lambda item: GetOpenAccounts(item), accounts.items())

                accounts_graph = []
                balance_graph = []
                for item in list(open_accounts):
                    amount = AccountBalance(item[0])
                    print(f"Account {item[0]} balance is: ${amount}")
                    balance_graph.append(amount)
                    accounts_graph.append(item[0])

                #Calling function to plot a graph
                PlotAccountBalances(accounts_graph, balance_graph)

            elif choice == '6':
                print('Leaving the program!')
                break


            else:
                print('Invalid option. Try again')

    else:
        while True:

            # Calling the function that shows the options menu.
            DisplayMenu(MENU_OPTIONS)

            # User input
            choice = input("Please select an option: ")

            # Conditional code depending on the menu option the user chooses.
            if choice == '1':
                ammount = AccountBalance(account_logged)
                print("Your account balance is: $", end="")
                print(ammount)


            elif choice == '2':
                Deposit(account_logged)


            elif choice == '3':
                Withdrawal(account_logged)


            elif choice == '4':

                hist_transactions = accounts[account_logged]["history"]
                date_transactions = accounts[account_logged]["date_transactions"]
                type_transaction = accounts[account_logged]["type_transaction"]

                if len(hist_transactions) > 0:
                    print("Transaction History:")
                    for i in range(len(hist_transactions)):
                        print(date_transactions[i], type_transaction[i], f'${hist_transactions[i]}')

                else:
                    print("You have no transactions yet!")

            elif choice == '5':
                print('Leaving the program!')
                break


            else:
                print('Invalid option. Try again')


