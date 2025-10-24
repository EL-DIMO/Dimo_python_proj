# List of programming languages
languages = ["Python", "JavaScript", "C++", "Rust", "Go"]

# Print the original list
print("Original list:", languages)

# Access elements
print("\nFirst language:", languages[0])
print("Last language:", languages[-1])

# Modify an element
languages[2] = "C#"
print("\nAfter modifying one element:", languages)

# Add elements using append()
languages.append("Java")
print("\nAfter appending:", languages)

# Insert an element
languages.insert(2, "TypeScript")
print("\nAfter inserting an element:", languages)

# Remove an element using del
del languages[3]
print("\nAfter deleting one element:", languages)

# Remove an element using pop()
popped = languages.pop()
print(f"\nRemoved '{popped}' using pop():", languages)

# Remove by value using remove()
languages.remove("Rust")
print("\nAfter removing 'Rust':", languages)

# Sort alphabetically
languages.sort()
print("\nSorted alphabetically:", languages)

# Sort in reverse order
languages.sort(reverse=True)
print("\nSorted in reverse:", languages)

# Reverse list
languages.reverse()
print("\nAfter reverse():", languages)

# Get length of list
print("\nNumber of languages:", len(languages))
