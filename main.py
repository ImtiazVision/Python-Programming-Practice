# name = "imtiaz\'s"
# print(name.capitalize())
user_name = input("what is your username?")
password = input("what is your password?")

password_length = len(password)
secret_password = '*' * password_length
print(f"{user_name}  is your username and {secret_password} is your password which is {password_length} characters long")