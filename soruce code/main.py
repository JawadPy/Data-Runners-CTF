import sqlite3
from pwinput import pwinput
from platform import system as oss
from sys import gettrace

# connect -> _is_it_fast_
# cursor -> __list__
# result -> __outy__


def db_init():
    _is_it_fast_ = sqlite3.connect(":memory:")
    __list__ = _is_it_fast_.cursor()

    __list__.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    __list__.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("flag", "AOL{W3ll_D0n3_Try_Th3_$tar}"))
    __list__.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user", "pass"))

    _is_it_fast_.commit()

    return __list__

def login(username, password, __list__):
    __list__.execute(f"SELECT id FROM users WHERE username = '{username}' AND password = '{password}'")
    __outy__ = __list__.fetchone()
    if __outy__:
        print(f"Login successful! Welcome, {username}.")
        newuser = input('Enter a new username: ')
        __list__.execute(f"UPDATE users SET username = '{newuser}' WHERE id = {__outy__[0]}")
        return 'Your password has been updated successfully!'

    else:
        return "Login failed. Incorrect username or password."

def main():
    __list__ = db_init()

    while True:
        choice = input("Welcome to Accounts Management DB System\n1. Manage Accounts\n2. Exit\n>> ")

        if choice == "1":
            print("Current users are: ")
            
            __list__.execute(f"SELECT username FROM users")
            for i in enumerate(__list__.fetchall()):
                print(f'{i[0]+1} - {i[1][0]}')
            
            print(
                login(
                    input("Username: "), 
                    pwinput(prompt='Password: ', mask='*'),
                    __list__
                    )
                )

        elif choice == "2":
            print("Thank you for using our system.\n Good Bye")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__" and oss() == "Windows" and gettrace() == None:
    main()