print("\nYou're going to create a password-protected account.")
user_name = input("Pick a user name:\n> ")
password = input("Pick a password:\n> ")

num_characters = len(password)
public_version = "*" * num_characters

print(f"\nHi, {user_name}. Your password is: {public_version}. At this point, your data is protected.")

def entry_function():
  print("\nTo get into your account, please type your user name and password below.")
  user_name_try = input("User name: ")
  password_try = input("Password: ")
  if user_name_try == user_name and password_try == password:
    print("\nThank you. You are now inside!")
  else:
    print("\nThat's not right. Please try again.")
    entry_function()

entry_function()
