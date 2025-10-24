# List of places you'd like to visit (not in alphabetical order)
places = ["Tokyo", "Cairo", "Makkah", "Paris", "Cape Town"]

# Original list
print("Original order:")
print(places)

# Alphabetical order (without modifying the original list)
print("\nAlphabetical order:")
print(sorted(places))

# Confirm the list is still in original order
print("\nStill in original order:")
print(places)

# Reverse alphabetical order (without modifying the list)
print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))

# Confirm the list is still in original order
print("\nStill in original order again:")
print(places)

# Use reverse() to change the list order
places.reverse()
print("\nList after using reverse():")
print(places)

# Use reverse() again to return to original order
places.reverse()
print("\nList after reversing again (back to original):")
print(places)

# Use sort() to change to alphabetical order permanently
places.sort()
print("\nList after using sort() (alphabetical):")
print(places)

# Use sort(reverse=True) to change to reverse-alphabetical order permanently
places.sort(reverse=True)
print("\nList after using sort(reverse=True) (reverse alphabetical):")
print(places)
