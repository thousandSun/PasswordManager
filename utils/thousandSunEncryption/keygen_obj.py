import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class KeyGen:
    """
    Key for encryption/decryption
    Use `modify` functions to change the parameters for the key
    """
    MASTER = b'i(A$\x83H\xbc\xa9@q\x15\x86\xe7\xd5t`\x87\x89\t\x8b\x99\x18?G\xec\t\xe0\xec\x91\xeeuM'
    SALT = b'\x9dc\xee\xb3i|!-dN\x11\x97\xa9N\xf9\x8b'
    LENGTH = 32
    ITERATIONS = 200000

    @property
    def key(self):
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                         length=self.LENGTH,
                         salt=self.SALT,
                         iterations=self.ITERATIONS,
                         backend=default_backend()
                         )

        return base64.urlsafe_b64encode(kdf.derive(self.MASTER))

    @staticmethod
    def modify_master(new: bytes):
        KeyGen.MASTER = new

    @staticmethod
    def modify_salt(new: bytes):
        KeyGen.SALT = new

    @staticmethod
    def modify_len(new: int):
        KeyGen.LENGTH = new

    @staticmethod
    def modify_iterations(new: int):
        KeyGen.ITERATIONS = new
