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
import mysql.connector
from mysql.connector import Error


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
    
    # Add transaction number to history list
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


def ChangePINCode(account_logged):
    """Change the PIN code."""

    # Validation PIN code for 4 digits
    while True:
        pin_number = input("Please enter the PIN number (4 digits): ")

        if pin_number.isdigit() and len(pin_number) == 4:
            break
        else:
            print("Invalid PIN number. A PIN number must be exactly 4 digits.")

    
    try:

        # Establish the connection
        cnx = CreateConnection()
        
        if cnx is None:
            raise Exception("Failed to establish connection.")

        # Create a cursor object
        cursor = cnx.cursor()

        print(f"UPDATE accounts SET pinNumber = '{pin_number}' WHERE accountId = '{account_logged}'")

        # Execute a query
        cursor.execute(f"UPDATE accounts SET pinNumber = '{pin_number}' WHERE accountId = '{account_logged}'")

        # Commit changes to the database
        cnx.commit()

        # Close the connection
        cnx.close()

    except Error as e:
        print("Error occurred:", e)
        return None


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


def CreateConnection():
    """Create a connection to the database."""

    try:
        # Establish the connection
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_PASSWORD",
            database="atm_plus"
        )

        print("Connection to the DB was successful!")
        return cnx

    except Error as e:
        print("Error in the connection with MySQL", e)

        return None

def GetNextAccountIdFromDatabase(type_account):
    """Load the database from a mysql."""

    try:

        # Establish the connection
        cnx = CreateConnection()
        if cnx is None:
            raise Exception("Failed to establish connection.")
        
        # Create a cursor object
        cursor = cnx.cursor()

        typeNumber = type_account == "Checking" and 1 or 2

        print(f"SELECT * FROM customerdata WHERE isActive = 0 AND accountId like '{typeNumber}%' LIMIT 1")

        # Execute a query
        cursor.execute(f"SELECT * FROM customerdata WHERE isActive = 0 AND accountId like '{typeNumber}%' LIMIT 1")

        # Fetch all the rows
        accountId = cursor.fetchall()
        
        # Close the connection
        cnx.close()

        return accountId

    except Error as e:
        print("Error occurred:", e)

        return None
    


def UpdateAccountStatus(accountId):
    """Update the account status to active in the database."""

    try:
        # Establish the connection
        cnx = CreateConnection()

        if cnx is None:
            raise Exception ("Failed to establish the connection.")
        # Create a cursor object
        cursor = cnx.cursor()

        print(f"UPDATE customerdata SET isActive = 1 WHERE accountId = '{accountId}'")

        # Execute a query
        cursor.execute(f"UPDATE customerdata SET isActive = 1 WHERE accountId = '{accountId}'")

        # Commit changes to the database
        cnx.commit()

        # Close the connection
        cnx.close()

    except Error as e:
        print("Error occurred:", e)


def CreateAccountToDatabase(account_data, accountId):
    """Create user."""


    try:
        # Establish the connection
        cnx = CreateConnection()

        if cnx is None:
            raise Exception ("Failed to establish the connection.")
        # Create a cursor object
        cursor = cnx.cursor()


        print(f"INSERT INTO accounts (accountId, pinNumber, accountType, isActive, firstName, lastName, dateOfBirth, phoneNumber, provinceId) VALUES({accountId[0][0]}, {accountId[0][1]}, '{account_data[0]}', 1, '{account_data[1]}', '{account_data[2]}', '{account_data[3]}', '{account_data[4]}', {account_data[5]})")

        # Execute a query
        cursor.execute(f"INSERT INTO accounts (accountId, pinNumber, accountType, isActive, firstName, lastName, dateOfBirth, phoneNumber, provinceId) VALUES('{accountId[0][0]}', {accountId[0][1]}, '{account_data[0]}', 1, '{account_data[1]}', '{account_data[2]}', '{account_data[3]}', '{account_data[4]}', {account_data[5]})")

        # Commit changes to the database
        cnx.commit()

        # Close the connection
        cnx.close()

    except Error as e:
        print("Error occurred:", e)


def GetAccountFromDatabase(accountId, pinNumber):
    """Load the account from a mysql."""

    try:

        # Establish the connection
        cnx = CreateConnection()

        # Create a cursor object
        cursor = cnx.cursor()

        # Execute a query
        cursor.execute(f"SELECT * FROM accounts WHERE accountId = '{accountId}' AND pinNumber = '{pinNumber}' AND isActive = 1")

        # Fetch all the rows
        account = cursor.fetchall()
    
    except Exception as e:
        print(" Error occurred:", e)
        account = None
    
    finally:
        if cnx.is_connected():
            #   Close the connection
            cnx.close()

    return account


def GetProvinceName(province):
    "Getting province Name"
    
    match province:
        case 1:
            return "BC"
        case 2:
            return "AL"
        case 3:
            return "MB"
        case 4:
            return "ON"
        case 5:
            return "YT"
        case 6:
            return "QC"
        case 7:
            return "NF"
        case 8:
            return "NB"
        case 9:
            return "NS"
        case _:
            print("Invalid province")
            return None


def CreateAccount():
    """Create a new account."""

    while True:
        first_name = input("Insert your first name: ")
        if len(first_name) > 0 and all(char.isalpha() or char.isspace() for char in first_name):
            break
        else:
            print("Invalid first name. Please use only alphabetic characters and spaces, and ensure it is not empty.")

    while True:
        last_name = input("Insert your last name: ")
        
        # Verifica se o sobrenome não está vazio e se contém apenas caracteres alfabéticos ou espaços
        if len(last_name) > 0 and all(char.isalpha() or char.isspace() for char in last_name):
            break
        else:
            print("Invalid last name. Please use only alphabetic characters and spaces, and ensure it is not empty.")



    while True:
        date_of_birth = input("Insert your date of birth (YYYY-MM-DD): ")

        if len(date_of_birth) == 10 and date_of_birth[4] == '-' and date_of_birth[7] == '-' \
            and date_of_birth[:4].isdigit() and date_of_birth[5:7].isdigit() and date_of_birth[8:].isdigit():
            break
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")



    while True:
        phone_number = input("Insert your phone number (NNNNNNNNNN): ")

        if phone_number.isdigit() and len(phone_number) == 10:
            break
        else:
            print("Invalid phone number. Please enter a 10-digit number without any spaces or punctuation.")


    while True:
        province = input("Insert your province(BC, AL, MB, ON, YT, QC, NF, NB, NS): ")

        match (province):
            case "BC":
                province = 1
            case "AL":
                province = 2
            case "MB":
                province = 3
            case "ON":
                province = 4
            case "YT":
                province = 5
            case "QC":
                province = 6
            case "NF":
                province = 7
            case "NB":
                province = 8
            case "NS":
                province = 9
            case _:
                print("Invalid province")
                continue
        
        break


    while True:
        type_account = input("Insert your type of account (Checking or Saving): ")
        
        # Convert the input to a consistent case for comparison
        type_account = type_account.strip().capitalize()

        # Validate
        if type_account in ["Checking", "Saving"]:
            break
        else:
            print("Invalid input. Please enter either 'Checking' or 'Saving'.")


    return (type_account, first_name, last_name, date_of_birth, phone_number, province)
    

def DisplayAllAccountsFromDB():
    """Display all customers."""

    try:

        # Establish the connection
        cnx = CreateConnection()

        if cnx is None:
            raise Exception ("Failed to establish the connection.")

        # Create a cursor object
        cursor = cnx.cursor()

        # Execute a query
        cursor.execute(f"SELECT * FROM accounts ORDER BY lastName ASC;")

        # Fetch all the rows
        accountsFromDb = cursor.fetchall()
        
        # Close the connection
        cnx.close()

    except Error as e:
        print("Error occurred:", e)


    # Display the accounts
    for account in accountsFromDb:

        #print(account)
        #print(type(account))
        province_name = GetProvinceName(account[7])


        print(f"Account: {account[0]}, PIN: {account[1]}, Nome: {account[2]} {account[3]}, Date of Birth: {account[4].strftime('%d/%m/%Y')}, Phone Number: {account[5]}, Province: {province_name}, Account Type: {account[6]}")


#----------
# MAIN CODE
# Define the menu options as a list
MENU_OPTIONS = ["Check Balance", "Deposit", "Withdraw", "Transaction History", "Change PIN code", "Quit"]
ADMIN_MENU_OPTIONS = ["All open accounts and balance", "All transaction history", "Deposits history" ,
                      "Withdrawls history", "Plot a graph", "Display accounts", "Quit"]

account_logged = ""
accounts = {
    # ADMIN ACCOUNT
    "211001": {
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

            # Calling the function that checks if the account exists in the database.
            accountId = GetAccountFromDatabase(account_number, pin_number)

            if accountId or (accounts.get(account_number) is not None and accounts[account_number].get("pin") is not None and accounts[account_number]["pin"] == pin_number):
                account_logged = accountId and str(accountId[0][0]) or account_number

                accounts[account_logged] = {
                    "balance": 0,
                    "history": [],
                    "date_transactions": [],
                    "type_transaction": [],
                    "transaction_number": [],
                    "open": True,
                }

                break

        # Condition for new customer.
        if choice == 'N':
            choice2 = input("Would you like to open an account with us? (Y/N)")
            
            if choice2 == 'Y':
                account_data = CreateAccount()
                accountId = GetNextAccountIdFromDatabase(account_data[0])
                account_logged = str(accountId[0][0])

                print("Your 6 digit account number is: $", account_logged)
                print("Your 4 digit PIN number i: $", accountId[0][1])

                # Creating the account in the database
                CreateAccountToDatabase(account_data, accountId)

                # deactivating the account in the database
                UpdateAccountStatus(account_logged)

                accounts[account_logged] = {
                    "balance": 0,
                    "history": [],
                    "date_transactions": [],
                    "type_transaction": [],
                    "transaction_number": [],
                    "open": True,
                }

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
                DisplayAllAccountsFromDB()
            
            elif choice == '7':
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
                ChangePINCode(account_logged)

            elif choice == '6':
                print('Leaving the program!')
                break


            else:
                print('Invalid option. Try again')


