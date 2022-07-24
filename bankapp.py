import random as rd
import  ast
data = {}
balance = 0
list_of_account_num = []
i = 3
x = 1

# 1. Create an account with the account number generated if they do not have an account.
#  All generated account numbers should begin with 0
# 2. Log in to the program if they have an account
# 3. Deposit money
# 4. Withdraw money from the account if they have a sufficient amount.
# 5. Users should be able to transfer money to other users in the account
# 6. Users should be able to check their account balances.
# The program should keep running until the user decides to make it log out and/or quit.
# The account data should be stored in a dictionary that looks like that below and kept 
# in a file for persistent storage


   
# data = {
#     '0123445677' : {
#         "first_name":"John",
#         "last_name" : "Doe ",
#         "login_pin" : "8424"
#         "transaction_pin": "0934",
#         "balance" : 0
#     }
# }


with open("bankdata.txt", "r") as file:
    data = file.read()
    # data = eval(file.read())


def generate_ac():
    account_no = rd.randrange(100404008, 999999999, 2)
    account_no = f'0{account_no}'
    # account_no = "0106047168"
    # with open("bankdata.txt", "r") as file:
        # data = file.read()
        # data = eval(file.read())
    # list_of_account_num = data.keys()
    # while account_no in list_of_account_num  == True: 
    #     account_no = rd.randrange(10040400, 99999999, 3)
    #     account_no = f'00{account_no}'

    return account_no

def test_login (login_pin):
    if len(login_pin) == 4:
            try:
                int(login_pin)
            except ValueError:
                return False
    if len(login_pin) == 4 and type(int(login_pin)) == int:
        return True
    else:
        return False

def test_transact_pin (transaction_pin):
    if len(transaction_pin) == 4:
            try:
                int(transaction_pin)
            except ValueError:
                return False
    if len(transaction_pin) == 4 and type(int(transaction_pin)) == int:
        return True
    else:
        return False

    

print("""Welcome to Trust Bank
        Enter S for  Sign up
        Enter L for login and """)
user_input = input("> ").lower()


#####SIGN UP
if user_input  == "s":
    account_num = generate_ac()
    first_name = input("Please enter your First Name :").lower()
    last_name = input("Please enter your Last Name :").lower()

    login_pin = input("Please choose a 4 digit Login pin :")
    if test_login(login_pin) == True:
        login_pin = login_pin
    elif test_login(login_pin) == False:
        print("invalid login pin, login pin must be 4 digits")
        quit()

    transaction_pin = input("Please enter your 4 digit transaction pin :")
    if test_login(transaction_pin) == True:
        transaction_pin = transaction_pin
    elif test_login(transaction_pin) == False:
        print("invalid transaction pin, pin must be 4 digits")
        quit()
   

   
    print(f"Dear {first_name}, Your account number is {generate_ac()}, please save it")

    data = {account_num:{
        "first_name":first_name,
        "last_name" : last_name,
        "login_pin" : login_pin,
        "transaction_pin": transaction_pin,
        "balance" : 0,
        }}
    

    with open("bankdata.txt", "a") as file:
        # file.write(str(data))
        file.write(str(f"{data}\n"))

##### LOGIN
elif user_input == "l":
    user_account = input("Please input your account number :")
    user_login = input("Please input your login pin :")

    with open("bankdata.txt", "r") as file:
        data = (file.readlines())
        for line in data:
            data1 = ast.literal_eval(line)
            if user_account in data1:
                if user_login == data1[user_account]['login_pin']:
                    print(f"welcome {data1[user_account]['first_name']}")

                    old_bal = data1[user_account]['balance']

                else:
                    print("Wrong account number or Login pin")
                    quit()


                
    
    print("""
    To Deposit money , enter 1
    To Withdraw, enter 2
    To Transfer, enter 3
    To Check bal, enter 4
    """)
    transaction_choice = input("Please enter a number > :")
    if transaction_choice == "1":
        deposit_amount = int(input("Please input amount to deposit :"))
        new_bal = int(old_bal) + deposit_amount + 4
        balance = str(new_bal)
        print(new_bal)
    elif  transaction_choice == "2":
        withdrawal_amount = int(input("Please input amount to withdraw :"))
    elif  transaction_choice == "3":
        transfer_amount = int(input("Please input amount to Transfer :"))
    elif  transaction_choice == "4":
        print(f"Your account balance is {data1[user_account]['balance']}")
    else:
        print("invalid input")

            
##end of login          
            

else:
    print("invalid input")

    

    