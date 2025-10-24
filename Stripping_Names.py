# Include whitespace characters
name = "\t Eldimo \n"

# Print with whitespace
print("Original name with whitespace:")
print(name)

# Print stripped versions
print("Using lstrip():", name.lstrip())  # Remove left spaces
print("Using rstrip():", name.rstrip())  # Remove right spaces
print("Using strip():", name.strip())    # Remove both sides
