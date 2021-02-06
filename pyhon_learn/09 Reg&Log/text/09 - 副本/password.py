import hashlib
class password_Lock:
    def Lock(string):
        password = hashlib.sha256()
        password.update(string.encode())
        passworded = password.digest()
        return passworded