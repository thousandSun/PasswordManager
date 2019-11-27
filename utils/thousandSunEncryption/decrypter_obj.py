from utils.thousandSunEncryption.keygen_obj import KeyGen
from cryptography.fernet import Fernet


class Decrypter:
    """Uses the other two files in `thousandSunEncryption`
    to decrypt encrypted message, modify `keygen_obj.py` to change key settings"""
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
