from ecdsa import SigningKey, SECP256k1
import hashlib, binascii

class Wallet:
    def __init__(self):
        self.private_key = SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()
        # create a simple address from public key hash (not real bitcoin address format, but close for demo)
        pub_hex = self.public_key.to_string().hex()
        # address = first 34 chars of sha256(pubkey)
        addr = hashlib.sha256(pub_hex.encode()).hexdigest()[:34]
        # prefix to look like crypto address
        self.address = 'CL' + addr.upper()
        # store keys in hex
        self.private_key_hex = self.private_key.to_string().hex()
        self.public_key_hex = pub_hex

    def sign(self, message: bytes) -> str:
        sig = self.private_key.sign(message)
        return binascii.hexlify(sig).decode()
