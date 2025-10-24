# Starting from the modified guest list
guests = ["Elon Musk", "Jeff Bezos", "Bill Gates"]

print("Good news! We found a bigger dinner table, so we can invite more guests.")

# Add guests using insert() and append()
guests.insert(0, "Steve Jobs")        # Add at the beginning
guests.insert(2, "Sundar Pichai")     # Add in the middle
guests.append("Larry Page")           # Add at the end

# Print new invitations
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")
