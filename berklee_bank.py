bank_dict = {
    "Priya": {"balance": 100, "pin": "4821"},
    "Carlos": {"balance": 300, "pin": "1092"},
    "Amira": {"balance": 0, "pin": "0000"},
    "Jordan": {"balance": 7788, "pin": "9999"},
}


def show_welcome():
    """
    Task: Print a welcome message for Berklee Bank.
    Name: show_welcome.
    Input: none.
    Side Effects: prints to the screen.
    Return: none.
    """
    pass
 
 
def login(bank_dict):
    """
    Task: Ask for name and PIN; keep asking again until they match an account.
    Name: login.
    Input: bank_dict.
    Side Effects: reads user input; prints an error message when the name or PIN is wrong.
    Return: str (the name of the user who logged in).
    """
    pass
 
 
def show_menu():
    """
    Task: Show the menu (check balance, deposit, withdraw, leave) and get the user's choice.
    Name: show_menu.
    Input: none.
    Side Effects: prints the menu; reads user input.
    Return: str (the user's choice).
    """
    pass
 
 
def check_balance(name, bank_dict):
    """
    Task: Show how much money the user has.
    Name: check_balance.
    Input: name, bank_dict.
    Side Effects: prints the balance.
    Return: none.
    """
    pass
 
 
def deposit(name, bank_dict):
    """
    Task: Ask how much money to put in and add it to the user's balance.
    Name: deposit.
    Input: name, bank_dict.
    Side Effects: reads user input; changes bank_dict[name]["balance"]; prints the new balance.
    Return: none.
    """
    pass
 
 
def withdraw(name, bank_dict):
    """
    Task: Ask how much money to take out; if it is more than the balance, ask again until it is not, then subtract it.
    Name: withdraw.
    Input: name, bank_dict.
    Side Effects: reads user input; prints an error when the amount is too large; changes bank_dict[name]["balance"]; prints the new balance.
    Return: none.
    """
    pass
 
 
def log_out():
    """
    Task: Ask the user if they want to leave after an action.
    Name: log_out.
    Input: none.
    Side Effects: reads user input; prints a goodbye message if they leave.
    Return: bool (True if the user wants to leave, False to go back to the menu).
    """
    pass

def run_unit_tests():
    test_bank = {
        "Priya": {"balance": 100, "pin": "4821"},
        "Amira": {"balance": 0, "pin": "0000"},
    }

    print("show_welcome")
    show_welcome()# Expecting the welcome message
 
    print("login")
    # Type: name "Bob", PIN "1111"  -> Expecting an error, then it asks again
    # Then type: name "Priya", PIN "4821"
    print(login(test_bank))  # Expecting Priya
 
    print("show_menu")
    print(show_menu())  # Expecting the menu

    print("check_balance")
    check_balance("Priya", test_bank)  # Expecting: balance is $100
 
    print("deposit")
    # Type: 50
    deposit("Priya", test_bank)
    print(test_bank["Priya"]["balance"])  # Expecting 150
 
    print("withdraw")
    # Type: 500  -> Expecting an error (more than the balance), then it asks again
    # Then type: 30
    withdraw("Priya", test_bank)
    print(test_bank["Priya"]["balance"])  # Expecting 120
 
    print("log_out")
    # Type: yes
    print(log_out())  # Expecting a goodbye message, then True
    # Type: no
    print(log_out())  # Expecting False
 
 
