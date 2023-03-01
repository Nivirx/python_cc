cars = ['audi', 'bmw', 'honda', 'toyota', 'ford', 'chevy']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else :
        print(car.title())

# checking for equality
# >>> car = 'bmw'
# >>> car == 'bmw'
# True
# >>> car == 'audi'
# False

# Standard conditionals apply to python
# != Not Equal to
# > gt
# < lt
# >= gt|eq
# <= lt|eq

# multiple conditions

ages = [21, 18, 23]

for age in ages:
    if (age >= 21) and (age <= 22):
        print(f"index {ages.index(age)} *IS* >= 21 and <= 22 ")
    else:
        print(f"index {ages.index(age)} is *NOT* >= 21 and <= 22 ")

# conditional for checking the presence of a value
toppings = ['mushrooms', 'onions', 'pineapple']

if 'mushrooms' in toppings:
    print("Mushroom pizza")
if 'ham' not in toppings:
    print("No ham here!")
# you *could* also write if not ('ham' in toppings)

# python also has standard if-elif-else blocks

import random
num = random.randint(1,3)

if num == 1:
    print("1")
elif num == 2:
    print('2')
else:
    print('3')


avilable_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
pizza = []
for req in requested_toppings:
    if req in avilable_toppings:
        print(f"adding {req} to your pizza")
        pizza.append(req)
    else:
        print(f"We don't have {req} right now!")

print(f"Finished with your pizza, it contains {pizza}")
