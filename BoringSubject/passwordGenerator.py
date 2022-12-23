import string
import random

dictionary = string.ascii_letters + string.digits + string.punctuation

password_length = int(input("pls enter password length!\n"))

password = "".join(random.sample(dictionary, password_length))

print(password)