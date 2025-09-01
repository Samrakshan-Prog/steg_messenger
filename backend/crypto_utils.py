from cryptography.fernet import Fernet, InvalidToken
def generate_key() -> bytes:
    return Fernet.generate_key()
def encrypt_message(message: str) -> tuple[bytes, bytes]:
    key = generate_key()
    f = Fernet(key)
    token = f.encrypt(message.encode("utf-8"))
    return key, token
def decrypt_message(token: bytes, key: str | bytes) -> str:
    if isinstance(key, str):
        key = key.encode("utf-8")
    f = Fernet(key)
    try:
        plaintext = f.decrypt(token).decode("utf-8")
    except InvalidToken as e:
        raise InvalidToken("Invalid key or corrupted data") from e
    return plaintext

