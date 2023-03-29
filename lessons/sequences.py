

# An exaple of a tuple without type aliasing 
goat: tuple[str, int] = ("MJ", 23)

# Tuples are sequences, so they're 0-indexed
print(goat[0])
print(goat[1])

# Printing a typle produces its litera syntax
print(goat)

# Print both items on same line
print(f"{goat[0]} is number {goat[1]}")

# Sequences have lengths
print(len(goat))

# Sequences are iterable with for...in loops
# <eamomg you can loop over them with for...in
for item in goat:
    print(item)

# Tuples, unlikes lists, are immutable
# Which means we cannot reaggins items, nor append, nor pop, etc
# goat[0] = "LBJ"

# We can "invent" our own type with a type alias
Player = tuple[str, int]

# Once we've aliased a type, we can create variables of that type
unc_poy: Player = ("Bacot", 5)

# In a strange world, where jersey number changes...
unc_poy = (unc_poy[0], unc_poy[1] + 1)

# A range is another common sequence type
ero_to_nine: range = range(0, 10, 1)

# We can access items of the range
print(ero_to_nine[0])
print(ero_to_nine[9])

for i in ero_to_nine:
    print(i)

# We ca have different steps for more control
odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i)


names: list[str] = ["Evan", "Kurt", "Keegan", "Lebron", "Kris"]
for i in range(len(names)):
    print(f"{i}, {names[i]}")


for i in range(0, len(names), 2):
    print(f"{i}, {names[i]}")