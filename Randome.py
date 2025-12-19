# big_mistakes_module.py
# Python module with lots of intentional mistakes

import os
import json
import re

# Global variable (bad practice)
users = []

# Function with inconsistent naming and weak validation
def createuser(Name, emailAddress, PassWord, age):
    username = Name
    email = emailAddress
    password = PassWord
    
    # Syntax error: missing colon
    if '@' not in email
        print("Invalid email")
        return False
    
    # Weak password validation
    if len(password) < 6:
        print("Password too short")
    
    # Logic flaw: duplicate emails allowed
    users.append({
        'username': username,
        'email': email,
        'password': password,  # Security flaw: plain text
        'age': age
    })
    
    print("User created successfully")  # Will still run even if email invalid

# Function with type and logic errors
def delete_user(email):
    for user in users:
        if user['email'] == email:
            users.remove(user)  # Runtime error: modifying list while iterating
        else:
            print("User not found")  # Prints multiple times unnecessarily

# Function with unused variable and naming inconsistencies
def updateUser(email, new_username=None, newEmail=None, newpassword=None):
    found = False
    for u in users:
        if u['email'] == email:
            found = True
            if new_username:
                u['username'] = new_username
            if newEmail:
                u['email'] = newEmail
            if newpassword:
                u['password'] = newpassword  # Weak security
    # Missing handling if user not found

# Function printing sensitive data
def list_users():
    for u in users:
        print(f"Username: {u['username']}, Email: {u['email']}, Password: {u['password']}")

# Function with type casting issues
def validate_age(age):
    if age < 18:
        print("Underage")
    elif age > 100
        print("Invalid age")  # Syntax error: missing colon
    else:
        print("Age valid")

# Function with bad practices: global, file I/O issues
def save_users_to_file(filename):
    global users
    file = open(filename, "w")  # No exception handling
    file.write(json.dumps(users))
    file.close()  # Better: use 'with' statement

# Calling functions with intentional mistakes
createuser("Usman", "usmandomain.com", "123", 25)  # Invalid email, weak password
createuser("Ali", "ali@domain.com", "abc", "twenty")  # Wrong type for age
delete_user("nonexistent@domain.com")  # Wrong logic
updateUser("usman@domain.com", newpassword="pass")  # Weak password
list_users()
save_users_to_file("users.json")
validate_age("twenty")  # Type error
