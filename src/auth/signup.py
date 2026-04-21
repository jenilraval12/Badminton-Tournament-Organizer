from database.db_config import create_connection

def sign_up():
    connection = create_connection()
    if not connection:
        print("Database connection failed.")
        return

    try:
        username = input("Enter a unique username (max 14 characters): ").strip()
        password = input("Enter your password (10 characters max): ").strip()

        if len(username) < 1 or len(username) > 14:
            print("Username must be between 1 and 14 characters.")
            return
        if len(password) > 10:
            print("Password cannot exceed 10 characters.")
            return

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            print("Username already exists. Please choose another.")
            return

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)
        )
        connection.commit()
        print("Sign-Up successful! You can now log in.")
    except Exception as e:
        print(f"Error during sign-up: {e}")
    finally:
        connection.close()
