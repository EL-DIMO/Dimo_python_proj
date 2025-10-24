# Guest list from Exercise 3-4
guests = ["Elon Musk", "Mark Zuckerberg", "Bill Gates"]

# Guest who can't make it
print(f"Unfortunately, {guests[1]} can't make it to the dinner.")

# Replace the guest with a new one
guests[1] = "Jeff Bezos"

# Print new invitations
print(f"Dear {guests[0]}, you are still invited to dinner.")
print(f"Dear {guests[1]}, you are invited to dinner.")
print(f"Dear {guests[2]}, you are still invited to dinner.")
