magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"Hey there {magician}! that was a neat trick")

print("\nwow, such tricks, much magic")

# interating over a list of numbers
for v in range(1,11):
    print(v)

numbers = list(range(1,11))
print(numbers)


# range(start, end(non-inclusive), stride)
even_numbers = list(range(2,11,2))
print(even_numbers)

# and instead of doing a range for odd numbers..
odd_numbers = numbers.copy()
for n in even_numbers:
    odd_numbers.remove(n)

print(numbers)
print(even_numbers)
print(odd_numbers)

squares = []
for n in range(1,11):
    squares.append(n**2)

print(f"squares from 1-10: {squares}")
print(f"min number from squares: {min(squares)}")
print(f"max number from squares: {max(squares)}")
print(f"sum of all squares 1-10: {sum(squares)}")

# list comprehensions
cubes = [v**3 for v in range(1,11)]
print(cubes)

# list slices
players = [n for n in range(0,6)]
# elements 0 1 2
print(players)
print(players[0:3])
print(players[:3]) # omitting the first element starts from index 0

# complex example
import math
half = math.floor(len(players)/2)
last_half = players[half:len(players)+1]
print(f"half way point {half}")
print(last_half)


# copying lists
my_fav_foods = ['pizza', 'pasta', 'ramen']
# two ways to copy lists
your_fav_foods = my_fav_foods.copy()
moms_fav_foods = my_fav_foods[:]

your_fav_foods.remove('ramen')
your_fav_foods.append('meatballs')
moms_fav_foods.append('chicken pot pie')

print(my_fav_foods)
print(your_fav_foods)
print(moms_fav_foods)

# WARNING: the following associates the varribles instead of copying
# so any changes to either will show up in both
brothers_fav_foods = my_fav_foods

# tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# not allowed
# dimensions[0] = 250

# but this is
dimensions = (250, 50)
print(dimensions)

# technically this is a valid tuple but you generally won't make one like this
# but it can happen in the case you dynamicly create tuples for instance
# t = (42,)







