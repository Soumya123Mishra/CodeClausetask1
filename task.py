import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz@#$&*?/."
length_password =int(input("Enter the   password length"))
x="".join(random.sample(password,length_password))
print(f"This is your Password:",{x})