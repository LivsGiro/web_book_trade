import bcrypt

def has_password(password):
    password_bytes = password.encode('utf-8')
    has_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return has_password.decode('utf-8')