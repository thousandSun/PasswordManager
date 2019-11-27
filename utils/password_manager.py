import pyperclip
from utils.database_connection import DatabaseConnection
from utils.thousandSunEncryption.decrypter_obj import Decrypter
from utils.thousandSunEncryption.encrypter_obj import Encrypter
from sqlite3 import IntegrityError


class PassMng:
    """
    Manages passwords using given account name and allows for
    manipulation based on given account name
    """
    def __init__(self, account: str = 'master'):
        self.account = account
        self.host = 'Passwords.db'

    def store_pass(self, password):
        enc = Encrypter(password)
        try:
            with DatabaseConnection(self.host) as connection:
                cursor = connection.cursor()

                cursor.execute('INSERT INTO passwords VALUES(?, ?)', (self.account, enc.encrypted))
        except IntegrityError:
            print(f'Account with name {self.account} already exists, use `Update` to set password')

    def get_password(self) -> bool:
        try:
            with DatabaseConnection(self.host) as connection:
                cursor = connection.cursor()

                cursor.execute('SELECT pass FROM passwords WHERE name=?', (self.account,))
                passwd = cursor.fetchone()[0]
        except TypeError:
            return False

        dec = Decrypter(passwd)
        pyperclip.copy(dec.decrypted.decode())
        return True

    def delete_pass(self):
        with DatabaseConnection(self.host) as connection:
            cursor = connection.cursor()

            cursor.execute('DELETE FROM passwords WHERE name=?', (self.account,))

    def update_pass(self, password):
        enc = Encrypter(password)
        with DatabaseConnection(self.host) as connection:
            cursor = connection.cursor()

            cursor.execute('UPDATE passwords SET pass=? WHERE name=?', (enc.encrypted, self.account))

    def update_master(self, password: str):
        enc = Encrypter(password)
        with DatabaseConnection(self.host) as connection:
            cursor = connection.cursor()

            cursor.execute('UPDATE passwords SET pass=? WHERE name=?', (enc.encrypted, self.account))

    @property
    def account_exists(self):
        with DatabaseConnection(self.host) as connection:
            cursor = connection.cursor()

            cursor.execute('SELECT EXISTS(SELECT * FROM passwords WHERE name=?)', (self.account,))
            exists = cursor.fetchone()
        return exists[0]

    @staticmethod
    def create_table():
        with DatabaseConnection("Passwords.db") as connection:
            cursor = connection.cursor()

            cursor.execute('CREATE TABLE IF NOT EXISTS passwords(name text primary key, pass text)')

    @staticmethod
    def show_accounts():
        with DatabaseConnection('Passwords.db') as connection:
            cursor = connection.cursor()

            cursor.execute('SELECT name FROM passwords WHERE name<>?', ('master',))
            accounts = cursor.fetchall()

        for account in accounts:
            print(account[0].ljust(20, " "))
