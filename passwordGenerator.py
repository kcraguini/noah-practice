import random

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
             "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0","1","2","3","4","5","6","7","8","9"]

symbols = ["~","!","@","#","$","%","*","(",")","_","-","+","=","|","/","?",";",":"]

print("I am here to generate a password for you!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password = []

for char in range(0, nr_letters):
    password.append(random.choice(alphabet))

for char in range(0, nr_symbols):
    password.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password.append(random.choice(numbers))

print(password)
random.shuffle(password)

password_list = ""
for char in password_list():
    password_list += char

print(f"Your random Password: {password_list}\n No Hacker will ever guess it :D")