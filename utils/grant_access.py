from utils.database_connection import DatabaseConnection
from utils.thousandSunEncryption.encrypter_obj import Encrypter
from utils.access import Login
from sqlite3 import IntegrityError


class Granter:
    """
    Decides if user is allowed to be granted access based on given password
    """
    def __init__(self, master: str):
        self.master = master
        self.enc = Encrypter(self.master)
        try:
            with DatabaseConnection('Passwords.db') as connection:
                cursor = connection.cursor()

                cursor.execute('INSERT INTO passwords VALUES(?, ?)', ('master', self.enc.encrypted))
        except IntegrityError:
            pass
        self.login = Login(self.master)

    @property
    def granted(self):
        return self.login.access_granted
