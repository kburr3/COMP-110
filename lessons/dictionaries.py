"""Demonstations of dictionary capabilities"""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialie to a empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal represention
print(schools)

# Access a value by it's key -- "lookuo"
print(f"UNC has {schools['UNC']} students")

# Remove a key value pair from a dictionary
# by its key.
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstation of dictionary literals

# Empty dictionary literal
schools = {} # Same as dict()
print(schools)
print()

# Alternatively, initalie key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NSCU": 26150}
print(schools)
print(schools["UNC"])

#What happens when a key does not exist?
print()

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")
print()
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")

