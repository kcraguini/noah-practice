import random
#lists of the letters, numbers, and desired symbols to set up the password
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
             "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0","1","2","3","4","5","6","7","8","9"]

symbols = ["~","!","@","#","$","%","*","(",")","_","-","+","=","|","/","?",";",":","<",">",".","[","]"]

print("I am here to generate a password for you!")

#user gets to input how long they want their password to be and how many letters, symbols, or numbers the user wants
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password = []

#grabbing the range of every list randomly 
for char in range(0, nr_letters):
    password.append(random.choice(alphabet))

for char in range(0, nr_symbols):
    password.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password.append(random.choice(numbers))

#shuffles the password so it is more difficult to read
random.shuffle(password)

password_string = ""
for char in password: 
    password_string += char

print(f"Your random Password: {password_string}\nNo Hacker will ever guess it :D")