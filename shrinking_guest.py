# Continue from Exercise 3-6
guests = ["Steve Jobs", "Elon Musk", "Sundar Pichai", "Jeff Bezos", "Bill Gates", "Larry Page"]

print("Bad news! The new dinner table won't arrive in time, so I can only invite two people.")

# Remove guests until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can’t invite you to dinner this time.")

# Print message to the two remaining guests
for guest in guests:
    print(f"{guest}, you are still invited to dinner!")

# Remove the last two guests to make the list empty
del guests[0]
del guests[0]

# Print the empty list to confirm
print("Final guest list:", guests)
