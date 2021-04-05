import random
database = {}
def init():
    
    isValidatedOptionSelected = False
    print('Welcome to AD Bank')
    while isValidatedOptionSelected ==False:
        haveAccount =int(input("Do you have an account number with us: 1(yes) 2(no) \n"))
        if(haveAccount ==1):
            isValidatedOptionSelected = True
            login()
        elif(haveAccount ==2):
            isValidatedOptionSelected = True
            register()
        else:
            print("You have selected a wrong option")
            return False
def login():
    print('Login to your account')
    accountNo = input('Kindly enter your account no \n')
    passwordLogin = input('Enter your password \n')
    print('Sucessfuly logged in')
    userOperations = int(input('Will you like to continue? 1(yes) 2(no) \n'))
    if(userOperations ==1):
        print('What would you like to do')
        bankOperation()
    elif(userOperations ==2):
        print('Thank you, kindly exit.')
    else:
        print('Kindly enter a valid option')

def register():
    print('Kindly register')
    email =input('Please enter your email: \n')
    first_name=input('Kindly enter your first name: \n')
    last_name=input('Kindly enter your  last name: \n')
    password = input('Create a password \n')
    accountNumber = generationAccountNumber()
    database[accountNumber] = [first_name ,last_name, email, password]
    #return database
    print(accountNumber)
    more_transactions = int(input('Will you like to continue  1(yes) 2(no) \n'))
    if(more_transactions ==1):
        login()
    elif(more_transactions ==2):
        print('Thank you, Kindly exit')
    else:
        print('invalid option! Kindly enter a valid option')

def bankOperation():
    bank_options =int(input("What would you like to do? 1(Balance) 2(Withdraw) 3(Transfer) 4(Recharge) \n"))
    if(bank_options ==1):
        print('Account Balance is .....')
    elif(bank_options ==2):
        withdrawal =int(input('Kindly enter the amount \n'))
        print('Sucessful')
    elif(bank_options == 3):
        bank_options =int(input('Kindly select the bank you want to transfer to 1(Zenith Bank) 2(Access Bank) 3(Gtb) 4(More)'))
        selected_options = input('kindly enter the account number')
        print('sucessful')
    elif(bank_options ==4):
        mobile = input('Kindly enter your mobile number: \n')
        print('Sucessful')
    else:
        print('This is not a valid option')
        
def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)
init()