# creating a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# modifing a list
motorcycles[2] = 'kawasaki'
print(motorcycles)

# adding an item to the end of list
motorcycles.append("suzuki")
print(motorcycles)

# another way to insert an item
motorcycles.insert(0, 'ducati')
motorcycles.insert(0, 'bmw')
print(motorcycles)

# of course you can build a list from scratch
computers = []
computers.append('macOS')
computers.append('GNU/Linux')
computers.append('Windows')
print(computers)

# removing elements from a list
del motorcycles[0] # delete ducati
print (motorcycles)

# remove an item and return the value
trash = computers.pop(2) #Windows
print(computers)
print(f"and the trash {trash}")

# remove by value
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"list of {motorcycles}")
print(f"\nRemoved {too_expensive.title()} because its too expensive for me.")

# sorting a list (in place)
cars = ['bmw', 'audi', 'toyota', 'honda', 'subaru']
print(f"list of cars as entered: {cars}")

# forward sort
cars.sort()
print(f"list of forwarded sorted cars {cars}")

# reverse sort
cars.sort(reverse=True)
print(f"reverse sorted: {cars}")

# sort without touching the original list
print(f"Original list of motorcycles {motorcycles}\nSorted list of motorcycles {sorted(motorcycles)}\nOriginal list again {motorcycles}")

# reverse the contents of a list (not sorting by equality)
print(motorcycles)
motorcycles.reverse()
print(motorcycles)
# apply reverse again to return to the original


print(f"number of motorcycles {len(motorcycles)}")
print(f"number of cars {len(cars)}")


