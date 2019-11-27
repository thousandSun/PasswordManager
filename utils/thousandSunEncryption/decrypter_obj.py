from utils.keygen_obj import KeyGen
from cryptography.fernet import Fernet


class Decrypter:
    def __init__(self, password):
        try:
            self.password = password.encode()
        except AttributeError:
            self.password = password
        gen = KeyGen()
        self.fernet = Fernet(gen.key)

    @property
    def decrypted(self):
        return self.fernet.decrypt(self.password)
