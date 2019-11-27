from utils.decrypter_obj import Decrypter
from utils.database_connection import DatabaseConnection


class Login:
    def __init__(self, password: str):
        self.password = password
        with DatabaseConnection("Passwords.db") as connection:
            cursor = connection.cursor()

            cursor.execute('SELECT pass FROM passwords WHERE name=?', ('master',))
            p = cursor.fetchone()[0]

        self.master = p.decode()

    def access_granted(self) -> bool:
        dec = Decrypter(self.master)

        return self.password == dec.decrypted.decode()

