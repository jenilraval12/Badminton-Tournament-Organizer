from database.db_config import create_connection

def sign_in():
    connection = create_connection()
    if not connection:
        print("Database connection failed.")
        return None

    try:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if not user:
            print("Username not found.")
            return None

        if password == user[2]:
            print(f"Welcome back, {username}!")
            return user[0]
        else:
            print("Incorrect password. Please try again.")
            return None
    except Exception as e:
        print(f"Error during sign-in: {e}")
        return None
    finally:
        connection.close()
