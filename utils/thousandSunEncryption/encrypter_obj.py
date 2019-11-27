from utils.thousandSunEncryption.keygen_obj import KeyGen
from cryptography.fernet import Fernet


class Encrypter:
    """
    Encrypts given message
    Modify `keygen_obj.py` to change key settings
    """
    def __init__(self, password: str):
        self.password = password.encode()
        gen = KeyGen()
        self.fernet = Fernet(gen.key)

    @property
    def encrypted(self):
        return self.fernet.encrypt(self.password)
