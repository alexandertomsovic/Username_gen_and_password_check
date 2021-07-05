# first project
# password gen
# by Alexander Tomsovic

import random
company = input("What is your favoite color: ")
print("If your first name is less than 4 characters please enter your full name.")
username = input("What is your first name?: ")


int1 = random.randint(1, 5)
if int1 > 2:
  username = username + username[1:3]
else: username = username[1:] + username[3]

int2 = random.randint(1, 100)
if int2 >= 50:
  username = username + str(int2)
else: 
  username = username + str(int1)

int3 = random.randint(36, 4738)
if int3 % 2 == 0:
  username = username + str(int3)
else:
  username = username + str(int3 - 2) + "AIO"

username = company[0] + company[-1] + username + company[-3:]
print("loading.")
print("loading..")
print("loading...")
print("-------------")
print("Your username is:")
print(username)

print("-------------")
print("You will now be creating a password. Make sure the password has atleast one number at the end, and is greater than seven characters.")

password = input("Enter your password: ")
if password[-1].isnumeric() and len(password) > 7:
  print("Password accepted.")
else:
  print("Your password is invalid")

if password[-1].isnumeric() and len(password) > 7:
  print("----------")
  print("connecting to client.")
  print("connecting to client..")
  print("connecting to client...")
else:
  print("")


username_test = input("What is your username? : ")
password_test = input("What is yout password?: ")
  
if password != password_test or username != username_test:
  print("Incorrect login info")
else:
  print("Login Successful! thanks for using this program.")
