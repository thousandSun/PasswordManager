from utils.thousandSunEncryption.decrypter_obj import Decrypter
from utils.database_connection import DatabaseConnection


class Login:
    """
    Class to check whether given constraint is in
    given field of given table in a database
    The SQL statement is hardcoded for now
    """
    def __init__(self, password: str):
        self.password = password
        try:
            with DatabaseConnection("Passwords.db") as connection:
                cursor = connection.cursor()

                cursor.execute('SELECT pass FROM passwords WHERE name=?', ('master',))
                p = cursor.fetchone()[0]
        except TypeError:
            pass
        else:
            self.master = p.decode()

    @property
    def access_granted(self) -> bool:
        dec = Decrypter(self.master)

        return self.password == dec.decrypted.decode()

