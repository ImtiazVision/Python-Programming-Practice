name = "imtiaz\'s"
print(name.capitalize())
user_name = input("what is your username?")
password = input("what is your password?")

password_length = len(password)
secret_password = '*' * password_length
print(f"{user_name}  is your username and {secret_password} is your password which is {password_length} characters long")

def remove_even(list):
    # Write your code here!

    for item in list:
		if item%2 = 0:
        	print(item)
        #
       # elif item % 2 == 0:
        #    return item.pop(item)
remove_even([1,2,4])

def remove_even(list):

    print([item for item in list if item % 2 != 0])

remove_even([6, 5, 4, 2])

value = input("How much is that doggy in the window? ")
value = int(value)

if value < 10:
    print("That's a great deal!")
elif 10 <= value <= 20:
    print("I'd still pay that...")
else:
    print("Wow! That's too much!")
