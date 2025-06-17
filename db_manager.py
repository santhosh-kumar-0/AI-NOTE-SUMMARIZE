import sqlite3
import hashlib

DATABASE_NAME = 'users.db'

def init_db():
    """Initializes the SQLite database and creates the users table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    """Hashes a password using SHA256 for secure storage."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user_db(username, password_hash):
    """
    Registers a new user in the database.
    Returns True on success, False if username already exists.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                       (username, password_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # This error occurs if the username (which is UNIQUE) already exists
        return False
    finally:
        conn.close()

def authenticate_user_db(username, password_hash):
    """
    Authenticates a user against the database.
    Returns the user's data (e.g., username) on success, None on failure.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users WHERE username = ? AND password_hash = ?",
                   (username, password_hash))
    user = cursor.fetchone()
    conn.close()
    return user # Returns (username,) tuple if found, otherwise None

# Initialize the database when the module is imported
init_db()