"""sqlite3.OperationalError"""
from utils.grant_access import Granter
from utils.password_manager import PassMng
from getpass import getpass

WELCOME_MESSAGE = """Welcome to AiO Password Manager"""

USER_PROMPT = """
The following options are provided:
--> 1 - Store password
--> 2 - Get password
--> 3 - Delete password
--> 4 - Update password
--> 5 - Change master password
--> 6 - Help
--> 7 - Exit
--> 0 - Credits"""

HELP_MESSAGE = """
!! DOES NOT STORE PASSWORDS IN PLAINTEXT !!

! The master password you entered at first will never change unless you change it
! All passwords stored are first encrypted to ensure security
! This program does not show your passwords
! The `Get password` option will retrieve your password and put it on your computer clipboard for copy/pasting
"""

CREDITS = """
+----------------------------+
| Written by: Filiberto Rios |
+----------------------------+
"""


def main():
    PassMng.create_table()
    password = getpass('Enter master password: ')
    access = Granter(password)
    while not access.granted:
        print('Access denied')
        password = getpass('Enter mater password: ')
        access = Granter(password)
    else:
        entered()


def entered():
    print(WELCOME_MESSAGE)
    user_choice = ''

    while user_choice != 7:
        print("Available Accounts".center(20, "-"))
        PassMng.show_accounts()
        print(USER_PROMPT)
        try:
            user_choice = int(input("Make a selection: "))
        except ValueError:
            user_choice = 99999

        if user_choice == 1:
            store()
        elif user_choice == 2:
            get()
        elif user_choice == 3:
            delete()
        elif user_choice == 4:
            update()
        elif user_choice == 5:
            change_master()
        elif user_choice == 6:
            print(HELP_MESSAGE)
        elif user_choice == 7:
            print('Goodbye')
        elif user_choice == 0:
            print(CREDITS)


def store():
    account = input("Account: ")
    password = getpass()

    pass_mng = PassMng(account)
    pass_mng.store_pass(password)


def get():
    account = input("Account: ")
    pass_mng = PassMng(account)

    if pass_mng.get_password():
        print('!! Successfully copied to clipboard !!\n')
    else:
        print('!! An error occurred !!\n')


def delete():
    account = input("Account: ")
    pass_mng = PassMng(account)
    if pass_mng.account_exists:
        pass_mng.delete_pass()
        print("!! Operation successful !!\n")
    else:
        print("!! Account doesn't exist !!\n")


def update():
    account = input('Account: ')
    pass_mng = PassMng(account)
    if pass_mng.account_exists:
        passwd = getpass('New password: ')
        pass_mng.update_pass(passwd)
        print('!! Operation successful !!\n')
    else:
        print("!! Account doesn't exist !!\n")


def change_master():
    passwd = getpass("New master password: ")
    pass_mng = PassMng()
    pass_mng.update_master(passwd)
    print("!! Operation successful !!\n")


if __name__ == '__main__':
    main()
