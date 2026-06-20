import hashlib
from db_config import connection, cursor

# Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Register new user
def register_user(username, password, role):

    hashed_password = hash_password(password)

    query = """
    INSERT INTO users (username, hashed_password, role)
    VALUES (%s, %s, %s)
    """

    values = (username, hashed_password, role)

    cursor.execute(query, values)

    connection.commit()


# Login existing user
def login_user(username, password):

    hashed_password = hash_password(password)

    query = """
    SELECT * FROM users
    WHERE username = %s
    AND hashed_password = %s
    """

    values = (username, hashed_password)

    cursor.execute(query, values)

    return cursor.fetchone()