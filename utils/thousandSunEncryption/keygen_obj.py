import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class KeyGen:
    def __init__(self):
        self.master = b'i(A$\x83H\xbc\xa9@q\x15\x86\xe7\xd5t`\x87\x89\t\x8b\x99\x18?G\xec\t\xe0\xec\x91\xeeuM'
        self.salt = b'\x9dc\xee\xb3i|!-dN\x11\x97\xa9N\xf9\x8b'

    @property
    def key(self):
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                         length=32,
                         salt=self.salt,
                         iterations=150000,
                         backend=default_backend()
                         )

        return base64.urlsafe_b64encode(kdf.derive(self.master))
