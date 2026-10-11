# Q4: Login Security System
# The account is locked after three incorrect attempts.

correct_password = "Python123"
attempt = 1
logged_in = False

while attempt <= 3:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful")
        logged_in = True
        break
    else:
        print("Incorrect password.")
        attempt = attempt + 1

if not logged_in:
    print("Account locked after 3 failed attempts.")
