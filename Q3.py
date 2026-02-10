# Predefined values
correct_username = "admin"
correct_password = "1234"
account_active = True

# User input
username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password and account_active:
    print("Login Successful")

elif username == correct_username and password == correct_password and not account_active:
    print("Account Disabled")

else:
    print("Wrong Credentials")
