import bcrypt

def hash_password(plain_text_password):
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password
    #comment test
    hashed_password = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
    return hashed_password
