msg = "Hello Python world!"
print("Hello from Python!")
print(msg)

name = "elaina claus"
print(name.title())
print(name.lower())
print(name.upper())

# skipping ahead to chapter 3 with lists :)
names = name.split(' ')

# using f-strings (> python3.6)
print(f"first name: {names[0].title()}")
print(f"last name {names[1].title()}")

# pre-python 3.6 formats
print("first name: {}".format(names[0].title()))
print("last name: {}".format(names[1].title()))

msg_with_whitespace = "Whitespace    "
print(f"{msg_with_whitespace.strip()}", end='')
print(" this should be right after the previous line")

# some stuff with numbers
universe_age =  14_000_000_000
print(universe_age)

# there is not a constant type (or any types...)
# but python convention is to use all upper case for constants
SOME_CONST = 5000

# playing with numbers
print(2*4)
print(16/2)
print(2**3)
print(4+4)
print(12-4)

meaning_of_life = 42
print(f"the answer we have all be searching for...{meaning_of_life}")

import this